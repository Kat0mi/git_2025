

#               |           
#        __ \   |  /   _` | 
#        |   |    <   (   |                            
#    _)  .__/  _|\_\ \__, | 
#       _|           |___/              >> Call using: from pkg import *


# >> Package Imports (Alphabetical Order)

#import astropy.io.fits as fits
#import astropy.stats as stats
import decimal
import importlib.util
import inspect
import matplotlib as mpl
import matplotlib.gridspec as GridSpec
import matplotlib.lines as Line2D
import matplotlib.patches as patches
import matplotlib.patches as PathPatch
import matplotlib.patheffects as PathEffects
import matplotlib.pyplot as plt
#import matplotlib_venn
import mpl_toolkits.axes_grid1 as axes_grid1
import mpl_toolkits.axes_grid1.inset_locator as inset_axes
import numpy as np
import os
import pandas as pd
#import seaborn as sns
#import sklearn.decomposition as PCA
#import sklearn.preprocessing as StandardScaler
import sys
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import tkinter.simpledialog as simpledialog


# >> Read Data

raw_cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cdfs.csv'))
raw_cosmos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_cosmos.csv'))
raw_uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'raw_uds.csv'))

ir_cdfs = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'ir_cdfs.csv'))
ir_cosmos = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'ir_cosmos.csv'))
ir_uds = pd.read_csv(os.path.join('/', 'Users', 'jess', 'Desktop', 'git_2025_overflow', 'datasets', 'ir_uds.csv'))


# >> Standard KDE/Scatter Plot Parameters

kde_params = {'cmap': 'Greys', 'fill': False, 'alpha': 0.7, 'zorder': 0, 'linewidths': 2}
b_param, bw_param = {'s': 180, 'color': 'xkcd:periwinkle blue', 'marker': 's', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3}, {'s': 230, 'color': 'xkcd:white', 'marker': 's', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3}
g_param, gw_param = {'s': 160, 'color': 'xkcd:hospital green', 'marker': 'D', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3}, {'s': 210, 'color': 'xkcd:white', 'marker': 'D', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3}
r_param, rw_param = {'s': 150, 'color': 'xkcd:salmon', 'marker': 'o', 'edgecolor': 'k', 'linewidth': 0.5, 'zorder': 3}, {'s': 200, 'color': 'xkcd:white', 'marker': 'o', 'edgecolor': 'w', 'linewidth': 2, 'zorder': 3}


# >> Common Loop Parameters

rgb_params, w_params = [b_param, g_param, r_param], [bw_param, gw_param, rw_param]
datasets, fields = [ir_cdfs, ir_cosmos, ir_uds], ['cdfs', 'cos', 'uds']
agn_types, agn_labels = ['xray_agn', 'radio_agn', 'ir_agn'], {'xray_agn': 'X-Ray AGN', 'radio_agn': 'Radio AGN', 'ir_agn': 'IR AGN'}