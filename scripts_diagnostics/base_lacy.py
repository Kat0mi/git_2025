
# Call this script uisng the following to access the Lacy plot base:

# from lacy import *


import matplotlib.pyplot as plt
import numpy as np

def plot_lacy(df, field, col, cmap, bar, save_path, title):

    xd, yd = '58_36', '80_45'
    xlim, ylim = [-1, 1.5], [-1, 1.5]
    xtick, ytick = np.arange(-1, 1.5, 0.5), np.arange(-1, 1.5, 0.5)
    
    x1 = np.linspace(-0.1, 1.5, 100)
    y1, y2 = -0.2, 0.8 * x1 + 0.5

    fig, ax = plt.subplots(figsize = (18, 10))

    scatter = ax.scatter(df[xd], df[yd], c = df[col], cmap = cmap, s = 80, zorder = 3)
    cbar = plt.colorbar(scatter)
    cbar.set_label(bar, rotation = 270, labelpad = 20)

    ax.set_title(f'{field.upper()}, {title}', size = '15', pad = 20)
    ax.set_facecolor('#e0e8ff')
    ax.axhline(0.25, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)
    ax.axvline(0.25, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)

    ax.set_xlim(xlim); ax.set_ylim(ylim)
    ax.set_xticks(xtick); ax.set_yticks(ytick)
    ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")
    ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

    ax.set_ylabel('$log (S_{8.0}/S_{4.5})$', size = '20')
    ax.set_xlabel('$log (S_{5.8}/S_{3.6})$', size = '20')

    ax.fill_between(x1, y1, y2, color = 'w', alpha = 0.3, zorder = 2)
    ax.fill_between(x1, y1, y2, color = 'none', edgecolor = 'white', alpha = 1, zorder = 4, linewidth = 3.5)
    ax.fill_between(x1, y1, y2, color = 'none', edgecolor = 'black', alpha = 1, zorder = 4, linewidth = 1.5)

    line_params_black = {'color': 'black', 'linewidth': 1.5, 'linestyle': '-', 'zorder': 5}
    line_params_white = {'color': 'white', 'linewidth': 3.5, 'linestyle': '-', 'zorder': 5}
    donley_scatter_params = {'s': 50, 'color': 'black', 'marker': 'o', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 5}

    ax.plot([0.1, 0.61], [0.13, 0.75], **line_params_black)
    ax.scatter([0.1, 0.202, 0.304, 0.406, 0.508, 0.61], [0.13, 0.254, 0.378, 0.502, 0.626, 0.75], **donley_scatter_params)

    lines = [([0.35, 0.93], [0.15, 0.85]), ([0.93, 0.7], [0.85, 1.12]),
             ([0.7, 0.08], [1.12, 0.36]), ([0.08, 0.08], [0.36, 0.15]),
             ([0.08, 0.35], [0.15, 0.15])]

    for x, y in lines:
        ax.plot(x, y, **line_params_white)
    for x, y in lines:
        ax.plot(x, y, **line_params_black)


    plt.savefig(save_path, bbox_inches = 'tight', dpi = 300, facecolor = 'white')
    plt.close()
