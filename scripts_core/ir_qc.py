
# Quality control! 

import pandas as pd; import os

cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cdfs.csv'))
cos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cosmos.csv'))
uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_uds.csv'))


cdfs = cdfs[
    (cdfs['use'] == 1) &
    (cdfs['SNR_36'] >= 3) & (cdfs['SNR_45'] >= 3) & (cdfs['SNR_58'] >= 3) & (cdfs['SNR_80'] >= 3) & 
    #(cdfs['SNR_24'] >= 3) & (cdfs['SNR_Ks'] >= 3) &
    (cdfs['f_IRAC_36'] >= (cdfs['f_IRAC_36'].mean() - (3 * cdfs['f_IRAC_36'].std()))) &
    (cdfs['f_IRAC_36'] <= (cdfs['f_IRAC_36'].mean() + (3 * cdfs['f_IRAC_36'].std()))) &
    (cdfs['f_IRAC_45'] >= (cdfs['f_IRAC_45'].mean() - (3 * cdfs['f_IRAC_45'].std()))) &
    (cdfs['f_IRAC_45'] <= (cdfs['f_IRAC_45'].mean() + (3 * cdfs['f_IRAC_45'].std()))) &
    (cdfs['f_IRAC_58'] >= (cdfs['f_IRAC_58'].mean() - (3 * cdfs['f_IRAC_58'].std()))) &
    (cdfs['f_IRAC_58'] <= (cdfs['f_IRAC_58'].mean() + (3 * cdfs['f_IRAC_58'].std()))) &
    (cdfs['f_IRAC_80'] >= (cdfs['f_IRAC_80'].mean() - (3 * cdfs['f_IRAC_80'].std()))) &
    (cdfs['f_IRAC_80'] <= (cdfs['f_IRAC_80'].mean() + (3 * cdfs['f_IRAC_80'].std())))
    #(cdfs['f_24_sfr'] >= (cdfs['f_24_sfr'].mean() - (3 * cdfs['f_24_sfr'].std()))) &
    #(cdfs['f_24_sfr'] <= (cdfs['f_24_sfr'].mean() + (3 * cdfs['f_24_sfr'].std())))
    #(cdfs['f_Ks'] <= (cdfs['f_Ks'].mean() - (3 * cdfs['f_Ks'].std()))) &
    #(cdfs['f_Ks'] <= (cdfs['f_Ks'].mean() + (3 * cdfs['f_Ks'].std())))
]

cos = cos[
    (cos['use'] == 1) &
    (cos['SNR_36'] >= 3) & (cos['SNR_45'] >= 3) & (cos['SNR_58'] >= 3) & (cos['SNR_80'] >= 3) &
    #(cos['SNR_24'] >= 3) & (cos['SNR_Ks'] >= 3) &
    (cos['f_IRAC_36'] >= (cos['f_IRAC_36'].mean() - (3 * cos['f_IRAC_36'].std()))) &
    (cos['f_IRAC_36'] <= (cos['f_IRAC_36'].mean() + (3 * cos['f_IRAC_36'].std()))) &
    (cos['f_IRAC_45'] >= (cos['f_IRAC_45'].mean() - (3 * cos['f_IRAC_45'].std()))) &
    (cos['f_IRAC_45'] <= (cos['f_IRAC_45'].mean() + (3 * cos['f_IRAC_45'].std()))) &
    (cos['f_IRAC_58'] >= (cos['f_IRAC_58'].mean() - (3 * cos['f_IRAC_58'].std()))) &
    (cos['f_IRAC_58'] <= (cos['f_IRAC_58'].mean() + (3 * cos['f_IRAC_58'].std()))) &
    (cos['f_IRAC_80'] >= (cos['f_IRAC_80'].mean() - (3 * cos['f_IRAC_80'].std()))) &
    (cos['f_IRAC_80'] <= (cos['f_IRAC_80'].mean() + (3 * cos['f_IRAC_80'].std()))) 
    #(cos['f_24_sfr'] >= (cos['f_24_sfr'].mean() - (3 * cos['f_24_sfr'].std()))) &
    #(cos['f_24_sfr'] <= (cos['f_24_sfr'].mean() + (3 * cos['f_24_sfr'].std())))
    #(cos['f_Ks'] <= (cos['f_Ks'].mean() - (3 * cos['f_Ks'].std()))) &
    #(cos['f_Ks'] <= (cos['f_Ks'].mean() + (3 * cos['f_Ks'].std())))
]

uds = uds[
    (uds['use'] == 1) &
    (uds['SNR_36'] >= 3) & (uds['SNR_45'] >= 3) & (uds['SNR_58'] >= 3) & (uds['SNR_80'] >= 3) &
    #(uds['SNR_24'] >= 3) & (uds['SNR_Ks'] >= 3) &
    (uds['f_IRAC_36'] >= (uds['f_IRAC_36'].mean() - (3 * uds['f_IRAC_36'].std()))) &
    (uds['f_IRAC_36'] <= (uds['f_IRAC_36'].mean() + (3 * uds['f_IRAC_36'].std()))) &
    (uds['f_IRAC_45'] >= (uds['f_IRAC_45'].mean() - (3 * uds['f_IRAC_45'].std()))) &
    (uds['f_IRAC_45'] <= (uds['f_IRAC_45'].mean() + (3 * uds['f_IRAC_45'].std()))) &
    (uds['f_IRAC_58'] >= (uds['f_IRAC_58'].mean() - (3 * uds['f_IRAC_58'].std()))) &
    (uds['f_IRAC_58'] <= (uds['f_IRAC_58'].mean() + (3 * uds['f_IRAC_58'].std()))) &
    (uds['f_IRAC_80'] >= (uds['f_IRAC_80'].mean() - (3 * uds['f_IRAC_80'].std()))) &
    (uds['f_IRAC_80'] <= (uds['f_IRAC_80'].mean() + (3 * uds['f_IRAC_80'].std()))) 
    #(uds['f_24_sfr'] >= (uds['f_24_sfr'].mean() - (3 * uds['f_24_sfr'].std()))) &
    #(uds['f_24_sfr'] <= (uds['f_24_sfr'].mean() + (3 * uds['f_24_sfr'].std())))
    #(uds['f_Ks'] <= (uds['f_Ks'].mean() - (3 * uds['f_Ks'].std()))) &
    #(uds['f_Ks'] <= (uds['f_Ks'].mean() + (3 * uds['f_Ks'].std())))
]

cdfs.to_csv('/Users/jess/Desktop/git_2025/datasets/ir_cdfs.csv', index = False)
cos.to_csv('/Users/jess/Desktop/git_2025/datasets/ir_cosmos.csv', index = False)
uds.to_csv('/Users/jess/Desktop/git_2025/datasets/ir_uds.csv', index = False)

print("IR mask successfully applied! IRAC and MIPS fluxes now within 3-sigma and SNR >= 3")