
# ----- Lacy Wedge w/ Colourbar -----

from pkg import *

# >> Adjust Here

field = uds_400

#col = 'Cigale_10'
#cmap = 'Oranges'
#bar = '1: Cigale frac > 0.10, 0: Cigale frac < 0.10'
# save_path = '/Users/jess/Desktop/cigale_10_in_lacy_uds.png'

col = 'log_bayes.agn.luminosity'
cmap = 'Spectral'
bar = 'log AGN luminosity'
save_path = '/Users/jess/Desktop/lacy_all_cuts_uds.png'



df = field[(field['log_bayes.agn.luminosity'] >= 34) & (field['log_bayes.agn.luminosity'] <= 40) & (field['lmass'] >= 10)]

xd, yd = '58_36', '80_45'

#xlim, ylim = [-0.7, 0.7], [-0.7, 0.7]
#xtick, ytick = np.arange(-0.7, 0.7, 0.1), np.arange(-0.7, 0.7, 0.1)

xlim, ylim = [-1, 1.5], [-1, 1.5]
xtick, ytick = np.arange(-1, 1.5, 0.5), np.arange(-1, 1.5, 0.5)

x1 = np.linspace(-0.1, 1.5, 100)
y1, y2 = -0.2, 0.8 * x1 + 0.5

fig, ax = plt.subplots(figsize = (18, 10))



# --- Plot ---

scatter_t1 = ax.scatter(df[xd], df[yd], c = 'white', s = 130, zorder = 3)
scatter_t1 = ax.scatter(df[xd], df[yd], c = df[col], cmap = cmap, s = 80, zorder = 3)

# >> Add Color Bar for Alpha Values

cbar_t1 = plt.colorbar(scatter_t1)
cbar_t1.set_label(bar, rotation = 270, labelpad = 20)

# >> General Aesthetics

ax.set_title('UDS, use = 1, lmass > 10, 3 sigma, snr >= 3', size = '15', pad = 20)

ax.set_facecolor('#e0e8ff')
ax.axhline(0.25, color = 'w', linewidth = 1, linestyle = '--', zorder = 1); ax.axvline(0.25, color = 'w', linewidth = 1, linestyle = '--', zorder = 1)

ax.set_xlim(xlim); ax.set_ylim(ylim)

ax.set_xticks(xtick); ax.set_yticks(ytick)
xticks = ax.xaxis.get_major_ticks(); yticks = ax.yaxis.get_major_ticks()
xticks[0].label1.set_visible(False); yticks[0].label1.set_visible(False)
ax.tick_params(axis = "x", direction = "in"); ax.tick_params(axis = "y", direction = "in")

ax.xaxis.labelpad = 15; ax.yaxis.labelpad = 15

ax.set_ylabel('$log (S_{8.0}/S_{4.5})$', size = '20'); ax.set_xlabel('$log (S_{5.8}/S_{3.6})$', size = '20')

# >> Lacy wedge

x1 = np.linspace(-0.1, 1.5, 100)
y1, y2 = -0.2, 0.8 * x1 + 0.5

ax.fill_between(x1, y1, y2, color = 'w', alpha = 0.3, zorder = 2)
ax.fill_between(x1, y1, y2, color = 'none', edgecolor = 'white', alpha = 1, zorder = 4, linewidth = 3.5)
ax.fill_between(x1, y1, y2, color = 'none', edgecolor = 'black', alpha = 1, zorder = 4, linewidth = 1.5)

# >> Donley

line_params_black = {'color': 'black', 'linewidth': 1.5, 'linestyle': '-', 'zorder': 5}
line_params_white = {'color': 'white', 'linewidth': 3.5, 'linestyle': '-', 'zorder': 5}
donley_scatter_params = {'s': 50, 'color': 'black', 'marker': 'o', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 5}

ax.plot([0.1, 0.61], [0.13, 0.75], color = 'black', linewidth = 1, linestyle = '-', zorder = 5)
ax.scatter([0.1, 0.202, 0.304, 0.406, 0.508, 0.61], [0.13, 0.254, 0.378, 0.502, 0.626, 0.75], **donley_scatter_params)
    
lines = [([0.35, 0.93], [0.15, 0.85]), ([0.93, 0.7], [0.85, 1.12]), ([0.7, 0.08], [1.12, 0.36]), 
        ([0.08, 0.08], [0.36, 0.15]), ([0.08, 0.35], [0.15, 0.15])]
        
for x, y in lines:
    ax.plot(x, y, **line_params_white)

for x, y in lines:
    ax.plot(x, y, **line_params_black)  

#ax.legend()


# >> Show Plot

plt.savefig(save_path, bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)
  
plt.show()