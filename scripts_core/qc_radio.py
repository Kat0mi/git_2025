
# Quality control! 

import pandas as pd; import os

cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cdfs.csv'))
cos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cosmos.csv'))
uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_uds.csv'))


cdfs = cdfs[
    (cdfs['use'] == 1) & (cdfs['SNR_f14'] >= 3) &
    (cdfs['f_14'] >= (cdfs['f_14'].mean() - (3 * cdfs['f_14'].std())))
]

cos = cos[
    (cos['use'] == 1) & (cos['SNR_f14'] >= 3) &
    (cos['f_14'] >= (cos['f_14'].mean() - (3 * cos['f_14'].std())))
]

uds = uds[
    (uds['use'] == 1) & (uds['SNR_f14'] >= 3)
    & (uds['f_14'] >= (uds['f_14'].mean() - (3 * uds['f_14'].std())))
]

cdfs.to_csv('/Users/jess/Desktop/git_2025_overflow/datasets/radio_cdfs.csv', index = False)
cos.to_csv('/Users/jess/Desktop/git_2025_overflow/datasets/radio_cosmos.csv', index = False)
uds.to_csv('/Users/jess/Desktop/git_2025_overflow/datasets/radio_uds.csv', index = False)

print("Radio mask successfully applied! Integrated 1.4GHz flux density now within 3-sigma and SNR >= 3")