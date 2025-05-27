
# Call this script uisng the following to access the RAI plot base:

# from rai import *


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

def plot_rai(df, field, col, cmap, bar, save_path, title):

    xd, yd = 'z', 'RAI'
    xlim, ylim = [0, 4.5], [0.1, 1000]
    xtick, ytick = np.arange(0, 4.5, 0.5), [0.1, 1, 10, 100, 1000]
    
    x = np.linspace(0, 2, 100)

    fig, ax = plt.subplots(figsize = (18, 10))

    scatter = ax.scatter(df[xd], df[yd], c = df[col], cmap = cmap, s = 80, zorder = 3)
    cbar = plt.colorbar(scatter)
    cbar.set_label(bar, rotation = 270, labelpad = 20)

    ax.set_title(f'{field.upper()}, {title}', size = '15', pad = 20)
    ax.set_facecolor('#e0e8ff')

    ax.set_xlim(xlim); ax.set_ylim(ylim)

    ax.set_yscale("log")
    ax.set_xticks(xtick); ax.set_yticks(ytick)
    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda y, _: f"$10^{{{int(np.log10(y))}}}$"))
    ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")
    ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

    ax.set_ylabel('Radio AGN Activity Index')
    ax.set_xlabel('Redshift', size = '20')

    ax.fill_between(x = np.linspace(ax.get_xlim()[0], ax.get_xlim()[1], 100), y1 = 3, y2 = ax.get_ylim()[1], color = 'white', alpha = 0.5, zorder = 0)

    ax.axhline(3, color = 'white', linewidth = 3, linestyle = '-', zorder = 1)
    ax.axhline(3, color = 'k', linewidth = 1, linestyle = '--', zorder = 1)


    plt.savefig(save_path, bbox_inches = 'tight', dpi = 300, facecolor = 'white')
    plt.close()
