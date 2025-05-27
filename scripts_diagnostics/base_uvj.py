
# Call this script uisng the following to access the UVJ plot base:

# from uvj import *


import matplotlib.pyplot as plt
import numpy as np

def plot_uvj(df, field, col, cmap, bar, save_path, title):

    xd, yd = 'V_J', 'U_V'
    xlim, ylim = [0, 2], [0, 2.5]
    xtick, ytick = np.arange(0, 2, 0.5), np.arange(0, 2.5, 0.5)

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

    ax.set_ylabel('Restframe U - V', size = '20')
    ax.set_xlabel('Restframe V - J', size = '20')

    # -- Quiescent/SF Boundary --

    ax.plot([-0.5, 0.85], [1.3, 1.3], 'w-', linewidth = 3)
    ax.plot([0.85, 1.6], [1.3, 1.95], 'w-', linewidth = 3)
    ax.plot([1.6, 1.6], [1.95, 2.5], 'w-', linewidth = 3)

    ax.plot([-0.5, 0.85], [1.3, 1.3], 'k-', linewidth = 1.5)        
    ax.plot([0.85, 1.6], [1.3, 1.95], 'k-', linewidth = 1.5)
    ax.plot([1.6, 1.6], [1.95, 2.5], 'k-', linewidth = 1.5)

    # -- SF/Dusty SF Boundary --

    ax.plot([1.2, 1.2], [0, 1.6], 'w-', linewidth = 3)
    ax.plot([1.2, 1.2], [0, 1.6], 'k-', linewidth = 1.5)

    # -- Colour Regions --

    ax.fill_between([-0.5, 0.85, 1.6], [1.3, 1.3, 1.95], [2.5, 2.5, 2.5], color = 'xkcd:salmon', alpha = 0.05)
    ax.fill_between([-0.5, 0.85, 1.2], [1.3, 1.3, 1.6], [0, 0, 0], color = 'xkcd:periwinkle blue', alpha = 0.05)
    ax.fill_between([1.2, 1.6, 1.6, 2.1], [1.6, 1.95, 2.5, 2.5], [0, 0, 0, 0], color = 'xkcd:hospital green', alpha = 0.05)

    # -- Region labels --

    ax.text(0.1, 1.5, 'Quiescent', fontsize = 24, ha = 'left', color = 'xkcd:salmon')
    ax.text(0.1, 1.1, 'Star Forming', fontsize = 24, ha = 'left', color = 'xkcd:periwinkle blue')
    ax.text(1.9, 0.1, 'Dusty', fontsize = 24, ha = 'right', color = 'xkcd:hospital green')


    plt.savefig(save_path, bbox_inches = 'tight', dpi = 300, facecolor = 'white')
    plt.close()
