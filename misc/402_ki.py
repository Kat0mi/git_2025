
# ----- Lacy Wedge w/ Colourbar -----

from purge_pkg import * 

# >> Adjust Here

field = uds

#col = 'Cigale_10'
#cmap = 'Oranges'
#bar = '1: Cigale frac > 0.10, 0: Cigale frac < 0.10'
# save_path = '/Users/jess/Desktop/cigale_10_in_lacy_uds.png'

col = 'log_bayes.agn.luminosity'
cmap = 'Spectral'
bar = 'log AGN luminosity'
save_path = '/Users/jess/Desktop/ki_all_cuts_uds.png'



df = field[(field['log_bayes.agn.luminosity'] >= 34) & (field['log_bayes.agn.luminosity'] <= 40) & (field['lmass'] >= 10) & (field['z'] > 0.2) & (field['z'] < 1.8)]

xd, yd = '45_80_in', 'Ks_45_in'

xlim, ylim = [-1.5, 2.5], [-2, 2]
xtick, ytick = np.arange(-1.5, 2.5, 1.0), np.arange(-2, 2, 1.0)

x1 = np.linspace(0, 2.5, 100)
y1, y2 = 0, 4.5  

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

ax.set_ylabel('$[Ks] - [4.5] (AB)$', size = '20'); ax.set_xlabel('[4.5] - [8.0] (AB)', size = '20')

# >> Messias Boundary

ax.fill_between(x1, y1, y2, color = 'w', alpha = 0.3, zorder = 2)
ax.fill_between(x1, y1, y2, color = 'none', edgecolor = 'black', alpha = 1, zorder = 4)

#ax.legend()


# >> Show Plot

plt.savefig(save_path, bbox_inches = 'tight', dpi = 300, facecolor = 'white', transparent = False)
  
plt.show()