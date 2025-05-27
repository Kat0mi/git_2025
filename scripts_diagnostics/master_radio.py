# This script runs all diagnostic scripts for the desired plot presets!

from plot_configs import *
from base_rai import *
from pkg_radio import *

master_fields = {
    'cdfs': radio_cdfs,
    'cosmos': radio_cosmos,
    'uds': radio_uds
}

diagnostic = {
    'rai': plot_rai
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

            save_path = config['save_path'].format(field = name, diagnostic = diag_name)
            plot_func(filtered_df, name, config['col'], config['cmap'], config['bar'], save_path, config['title'])

            plot_count += 1

print(f"\nSuccessfully output {plot_count} plots.")
