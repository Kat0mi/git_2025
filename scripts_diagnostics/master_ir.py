# This script runs all diagnostic scripts for the desired plot presets!

from plot_configs import *
from base_lacy import *
from base_ki import *
from base_kim import *
from pkg_ir import *

master_fields = {
    'cdfs': ir_cdfs,
    'cosmos': ir_cosmos,
    'uds': ir_uds
}

diagnostic = {
    'lacy': plot_lacy,
    'ki': plot_ki,
    'kim': plot_kim
}

# >> Desired Presets

presets = ['lum', 'cig10', 'cig25', 'cig50', 'cig75', 'cig90']

plot_count = 0

for diag_name, plot_func in diagnostic.items():
    for preset in presets:
        config = configs[preset]

        for name, df in master_fields.items():
            filtered_df = df[
                (df['log_bayes.agn.luminosity'] >= 34) &
                (df['log_bayes.agn.luminosity'] <= 40) &
                (df['lmass'] >= 10)
            ]

            if diag_name == 'ki':
                filtered_df = filtered_df[(filtered_df['z'] > 0.2) & (filtered_df['z'] < 1.8)]
                
            elif diag_name == 'kim':
                filtered_df = filtered_df[(filtered_df['z'] > 0.5) & (filtered_df['z'] < 2.5)]

            save_path = config['save_path'].format(field = name, diagnostic = diag_name)
            plot_func(filtered_df, name, config['col'], config['cmap'], config['bar'], save_path, config['title'])

            plot_count += 1

print(f"\nSuccessfully output {plot_count} plots.")
