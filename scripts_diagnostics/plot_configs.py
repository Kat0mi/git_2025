
# Call this script using the following to define plot presets:

# from plot_configs import *


configs = {

    # >> Customise as needed

    'custom': {
        'col': 'log_bayes.agn.luminosity',
        'cmap': 'Spectral',
        'bar': 'log AGN luminosity',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_custom.png',
        'title': 'Custom AGN Luminosity'
    },
    


    # >> 'Spectral' continuous colourbar using bayesian AGN luminosity values

    'lum': {
        'col': 'log_bayes.agn.luminosity',
        'cmap': 'Spectral',
        'bar': 'log AGN luminosity',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_bayes_lum.png',
        'title': 'Cigale AGN Luminosity'
    },

    # >> 0 (white)/1 (orange) discrete colourbar using Cigale AGN contributions

    'cig10': {
        'col': 'Cigale_10',
        'cmap': 'Oranges',
        'bar': '1: Cigale frac > 0.10, 0: Cigale frac < 0.10',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_cigale10.png',
        'title': 'Cigale AGN Contribution > 10%'
    },

    'cig25': {
        'col': 'Cigale_25',
        'cmap': 'Oranges',
        'bar': '1: Cigale frac > 0.25, 0: Cigale frac < 0.25',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_cigale25.png',
        'title': 'Cigale AGN Contribution > 25%'
    },

    'cig50': {
        'col': 'Cigale_50',
        'cmap': 'Oranges',
        'bar': '1: Cigale frac > 0.50, 0: Cigale frac < 0.50',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_cigale50.png',
        'title': 'Cigale AGN Contribution > 50%'
    },

    'cig75': {
        'col': 'Cigale_75',
        'cmap': 'Oranges',
        'bar': '1: Cigale frac > 0.75, 0: Cigale frac < 0.75',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_cigale75.png',
        'title': 'Cigale AGN Contribution > 75%'
    },

    'cig90': {
        'col': 'Cigale_90',
        'cmap': 'Oranges',
        'bar': '1: Cigale frac > 0.90, 0: Cigale frac < 0.90',
        'save_path': '/Users/jess/Desktop/git_2025_overflow/plot_outputs/{diagnostic}/{diagnostic}_{field}_cigale90.png',
        'title': 'Cigale AGN Contribution > 90%'
    }

}
