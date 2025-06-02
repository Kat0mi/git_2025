# This script runs all diagnostic scripts for the desired plot presets!

from plot_configs import *
from base_uvj import *
from pkg_uvj import *

master_fields = {
    'cdfs': uvj_cdfs,
    'cosmos': uvj_cosmos,
    'uds': uvj_uds
}

diagnostic = {
    'uvj': plot_uvj
}

# >> Desired Presets

presets = ['lum', 'cig10', 'cig25', 'cig50', 'cig75', 'cig90']

# >> Redshift bins (label, lower bound, upper bound)

redshift_bins = [
    ("z0.2_0.8", 0.2, 0.8),
    ("z0.8_1.8", 0.8, 1.8),
    ("z1.8_3.2", 1.8, 3.2),
    ("z3.2_max", 3.2, 20)
]

plot_count = 0

for diag_name, plot_func in diagnostic.items():
    for preset in presets:
        config = configs[preset]

        if preset == 'lum':
            vmin, vmax = 34, 40

        else:
            vmin, vmax = 0, 1

        for name, df in master_fields.items():
            for z_label, z_min, z_max in redshift_bins:
                filtered_df = df[
                    (df['log_bayes.agn.luminosity'] >= 34) &
                    (df['log_bayes.agn.luminosity'] <= 40) &
                    (df['lmass'] >= 10) &
                    (df['z'] >= z_min) &
                    (df['z'] < z_max) 
                ]

                save_path = config['save_path'].format(field = name, diagnostic = diag_name)
                save_path = save_path.replace(".png", f"_{z_label}.png")
                title = f"{config['title']} ({z_label.replace('_', ' to ')})"

                plot_func(filtered_df, name, config['col'], config['cmap'], config['bar'], save_path, title, vmin, vmax)

                plot_count += 1

print(f"\nSuccessfully output {plot_count} plots.")