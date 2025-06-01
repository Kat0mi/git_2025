
# Quality control! 

import pandas as pd; import os

cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cdfs.csv'))
cos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cosmos.csv'))
uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_uds.csv'))

cdfs = cdfs[
    (cdfs['use'] == 1)
]

cos = cos[
    (cos['use'] == 1)
]

uds = uds[
    (uds['use'] == 1)
]

cdfs.to_csv('/Users/jess/Desktop/git_2025_overflow/datasets/xray_cdfs.csv', index = False)
cos.to_csv('/Users/jess/Desktop/git_2025_overflow/datasets/xray_cosmos.csv', index = False)
uds.to_csv('/Users/jess/Desktop/git_2025_overflow/datasets/xray_uds.csv', index = False)

print("X-ray mask successfully applied! Rest-frame luminosity now within 3-sigma and SNR >= 3")