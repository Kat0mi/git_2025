
# Call this script uisng the following to access the KIM plot base:

# from kim import *


import matplotlib.pyplot as plt
import numpy as np

def plot_kim(df, field, col, cmap, bar, save_path, title, vmin = None, vmax = None):

    xd, yd = '45_80_in', '80_24_in'
    xlim, ylim = [-1.5, 2.5], [-2.5, 3.5]
    xtick, ytick = np.arange(-1.5, 2.5, 1.0), np.arange(-2.5, 3.5, 1.0)
    
    x1, x2 = np.linspace(-0.4, 0.8, 100), np.linspace(0.8, 2.5, 100)
    y1, y2, y3 = -2.9 * x1 + 2.8, 0.5, 4.5  

    fig, ax = plt.subplots(figsize = (18, 10))

    scatter = ax.scatter(df[xd], df[yd], c = df[col], cmap = cmap, s = 80, zorder = 3, vmin = vmin, vmax = vmax)
    cbar = plt.colorbar(scatter)
    cbar.set_label(bar, rotation = 270, labelpad = 20)

    ax.set_title(f'{field.upper()}, {title}', size = '15', pad = 20)
    ax.set_facecolor('#e0e8ff')
    ax.axhline(0.5, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)
    ax.axvline(0.5, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)

    ax.set_xlim(xlim); ax.set_ylim(ylim)
    ax.set_xticks(xtick); ax.set_yticks(ytick)
    ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")
    ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

    ax.set_ylabel('$[8.0] - [24] (AB)$', size = '20')
    ax.set_xlabel('$[4.5] - [8.0] (AB)$', size = '20')

    ax.fill_between(x1, y1, y3, color = 'w', alpha = 0.3, zorder = 2)
    ax.fill_between(x2, y2, y3, color = 'w', alpha = 0.3, zorder = 2)

    ax.plot([0.8, -0.4], [0.5, 4], color = 'black', linewidth = 1, linestyle = '-', zorder = 4)
    ax.plot([0.8, 2.5], [0.5, 0.5], color = 'black', linewidth = 1, linestyle = '-', zorder = 4)

    plt.savefig(save_path, bbox_inches = 'tight', dpi = 300, facecolor = 'white')
    plt.close()
