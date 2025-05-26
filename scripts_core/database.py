
# -- Imports and Path/Extension Definitions --

import os; import pandas as pd; import numpy as np; from functools import reduce; import warnings
warnings.filterwarnings("ignore", category = RuntimeWarning, message = "invalid value encountered in log10")

base_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_data', 'raw')
save_path = os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets')

field_dirs = {'cdfs': os.path.join(base_path, 'cdfs'), 'cosmos': os.path.join(base_path, 'cosmos'), 'uds': os.path.join(base_path, 'uds')}
extensions = ('.cat', '.fout', '.zout', '.txt')


# -- Build Dataframes --

def read_and_merge_field_data(field_name, folder_path):

    dfs = []                                                                    # Empty list to store dataframes

    for file in os.listdir(folder_path):                                        # Iterate over files in the directory

        if file.endswith(extensions):                                           # Limit to relevant file types
            
            file_path = os.path.join(folder_path, file)

            try:                                                                # Read the file into a DataFrame
                df = pd.read_csv(file_path, sep = '\s+', engine = 'python')

                if 'id' in df.columns:                                          # Check if 'id' exists for merging
                    dfs.append(df)                                              # Append DataFrame to the list if so

            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # >> Perform field-specific outer merges

    merged_df = reduce(lambda left, right: pd.merge(left, right, on = 'id', how = 'outer'), dfs)
    merged_df['field'] = field_name
    merged_df.replace([-99, -999, -99000], np.nan, inplace = True)

    return merged_df


# -- Log10 Handling Function --

def safe_log10(x):
    return np.log10(x.replace(0, np.nan)) if isinstance(x, pd.Series) else np.log10(np.where(x == 0, np.nan, x))


# -- Dataframe Customisation Function --

def process_dataframe(data):

    # >> Custom z column that uses z_spec when available
    
    if 'z_spec_zout' in data.columns and 'z_peak_zout' in data.columns:
        data['z'] = data['z_spec_zout'].combine_first(data['z_peak_zout'])

    # >> Convert MIPS 24um flux and error to Jy

    for col in ['f_24_sfr', 'e_24_sfr']:
        if col in data.columns:
            data[col] *= 1000

    # >> Convert UVJ fluxes to AB magnitudes (zp = 23.9)

    ab_rest = ['f_U_rf', 'e_U_rf', 'f_V_rf', 'e_V_rf', 'f_B_rf', 'e_B_rf', 'f_J_rf', 'e_J_rf']

    for col in ab_rest:
        if col in data.columns:
            data[col] = -(5 / 2) * safe_log10(data[col]) + 23.9

    # >> Convert IRAC fluxes to AB magnitudes (zp = 16.4)

    ab_flux = ['f_IRAC_36', 'e_IRAC_36', 'f_IRAC_45', 'e_IRAC_45', 'f_IRAC_58', 'e_IRAC_58', 'f_IRAC_80', 'e_IRAC_80', 'f_24_sfr', 'e_24_sfr', 'f_Hs', 'e_Hs', 'f_Hl', 'e_Hl', 'f_Ks', 'e_Ks']

    for col in ab_flux:
        if col in data.columns and col.startswith('f_'):
            ab_col = col.replace('f_', 'AB_')
            data[ab_col] = -(5 / 2) * safe_log10(data[col]) + 16.4

    # >> Calculate RAI column

    if 'l_14' in data.columns and 'sfr_uvir' in data.columns:
        data['RAI'] = (3.18e-22 * data['l_14']) / data['SFR_UVIR']

    # >> Emission Ratios

    if 'f_IRAC_80' in data.columns and 'f_IRAC_45' in data.columns:
        data['80_45'] = safe_log10(data['f_IRAC_80'] / data['f_IRAC_45'])
    if 'f_IRAC_58' in data.columns and 'f_IRAC_36' in data.columns:
        data['58_36'] = safe_log10(data['f_IRAC_58'] / data['f_IRAC_36'])
    if 'f_IRAC_80' in data.columns and 'f_IRAC_36' in data.columns:
        data['80_36'] = safe_log10(data['f_IRAC_80'] / data['f_IRAC_36'])

    # >> Magnitude Indices

    subtract_pairs = {
        '36_45_in': ['AB_IRAC_36', 'AB_IRAC_45'],
        '58_80_in': ['AB_IRAC_58', 'AB_IRAC_80'],
        '45_80_in': ['AB_IRAC_45', 'AB_IRAC_80'],
        'Ks_45_in': ['AB_Ks', 'AB_IRAC_45'],
        '80_24_in': ['AB_IRAC_80', 'AB_24_sfr'],
        'U_V': ['AB_U_rf', 'AB_V_rf'],
        'V_J': ['AB_V_rf', 'AB_J_rf'],
        'U_B': ['AB_U_rf', 'AB_B_rf']
    }

    for new_col, (col1, col2) in subtract_pairs.items():
        if col1 in data.columns and col2 in data.columns:
            data[new_col] = data[col1] - data[col2]

    # >> Boolean Diagnostic Columns

    def has_cols(cols): return all(c in data.columns for c in cols)

    if has_cols(['58_36', '80_45']):
        data['Lacy'] = np.where(
            (data['58_36'] > -0.1) & (data['80_45'] > -0.2) & (data['80_45'] < 0.8 * data['58_36'] + 0.5),
            1, 0
        )

    if has_cols(['58_36', '80_45', 'f_IRAC_45', 'f_IRAC_36', 'f_IRAC_58', 'f_IRAC_80']):
        data['Donley'] = np.where(
            (data['58_36'] > 0.08) & (data['80_45'] > 0.15) &
            (data['80_45'] > (1.21 * data['58_36'] - 0.27)) &
            (data['80_45'] < (1.21 * data['58_36'] + 0.27)) &
            (data['f_IRAC_45'] > data['f_IRAC_36']) &
            (data['f_IRAC_58'] > data['f_IRAC_45']) &
            (data['f_IRAC_80'] > data['f_IRAC_58']),
            1, 0
        )

    if has_cols(['45_80_in', 'Ks_45_in']):
        data['KI'] = np.where(
            (data['45_80_in'] > 0) & (data['Ks_45_in'] > 0),
            1, 0
        )

    if has_cols(['80_24_in', '45_80_in']):
        data['KIM'] = np.where(
            (data['80_24_in'] > 0.5) & (data['80_24_in'] > (-2.9 * data['45_80_in'] + 2.8)),
            1, 0
        )

    if has_cols(['U_V', 'V_J']):
        data['Quiescent'] = np.where(
            (data['U_V'] > 1.23) & (data['V_J'] < 1.67) & (data['U_V'] < (data['V_J'] * 0.98 + 0.38)),
            1, 0
        )

    # >> Log Bayes AGN Luminosity

    if 'bayes.agn.luminosity' in data.columns:
        data['log_bayes.agn.luminosity'] = safe_log10(data['bayes.agn.luminosity'])

    # >> AN Contribution Columns

    if 'bayes.agn.fracAGN' in data.columns:
        for thresh in [0.1, 0.25, 0.5, 0.75, 0.9]:
            col_name = f"Cigale_{int(thresh * 100)}"
            data[col_name] = np.where(data['bayes.agn.fracAGN'] >= thresh, 1, 0)

    # >> SNR Columns

    snr_pairs = {
        '36': ('f_IRAC_36', 'e_IRAC_36'),
        '45': ('f_IRAC_45', 'e_IRAC_45'),
        '58': ('f_IRAC_58', 'e_IRAC_58'),
        '80': ('f_IRAC_80', 'e_IRAC_80'),
        '24': ('f_24_sfr', 'e_24_sfr'),
        'Hs': ('f_Hs', 'e_Hs'),
        'Hl': ('f_Hl', 'e_Hl'),
        'Ks': ('f_Ks', 'e_Ks'),
        'U': ('f_U_rf', 'e_U_rf'),
        'V': ('f_V_rf', 'e_V_rf'),
        'J': ('f_J_rf', 'e_J_rf'),
        'B': ('f_B_rf', 'e_B_rf')
    }

    for name, (flux_col, error_col) in snr_pairs.items():
        if flux_col in data.columns and error_col in data.columns:
            snr_col = f'SNR_{name}'
            data[snr_col] = data[flux_col] / data[error_col]

    return data


# -- Merge and Save Dataframes --

for field, path in field_dirs.items():
    print(f"Merging files for: {field}")
    merged_df = read_and_merge_field_data(field, path)

    if merged_df is not None:
        merged_df = process_dataframe(merged_df)
        output_path = os.path.join(save_path, f'raw_{field}.csv')
        merged_df.to_csv(output_path, index = False)
    else:
        print(f"No data saved for {field}") 

print("Successfully merged!")