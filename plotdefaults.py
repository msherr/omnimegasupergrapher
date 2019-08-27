"""
Written by Micah Sherr <msherr@cs.georgetown.edu>
Georgetown University
"""

import numpy as np
import matplotlib
matplotlib.use('Agg') # for systems without X11
import matplotlib.pyplot as plt


def set_default_plot_options():
    options = {
        #'backend': 'PDF',
        'font.size': 14,
        'figure.figsize': (4,2.67),
        'figure.dpi': 100.0,
        'figure.subplot.left': 0.20,
        'figure.subplot.right': 0.97,
        'figure.subplot.bottom': 0.20,
        'figure.subplot.top': 0.90,
        'grid.color': '0.1',
        'grid.linestyle': ':',
        #'grid.linewidth': 0.5,
        'axes.grid' : True,
        #'axes.grid.axis' : 'y',
        #'axes.axisbelow': True,
        'axes.titlesize' : 'x-small',
        'axes.labelsize' : 'small',
        'axes.formatter.limits': (-4,4),
        'xtick.labelsize' : 10,
        'ytick.labelsize' : 10,
        'lines.linewidth' : 2.0,
        'lines.markeredgewidth' : 0.5,
        'lines.markersize' : 10,
        'legend.fontsize' : 9,
        'legend.fancybox' : False,
        'legend.shadow' : False,
        'legend.borderaxespad' : 0.5,
        'legend.numpoints' : 1,
        'legend.handletextpad' : 0.5,
        'legend.handlelength' : 1.6,
        'legend.labelspacing' : .75,
        'legend.markerscale' : 1.0,
        # turn on the following to embedd fonts; requires latex
          'ps.useafm' : True,
        'pdf.use14corefonts' : True,
        'text.usetex' : True,
    }

    for option_key in options:
        matplotlib.rcParams[option_key] = options[option_key]


def set_plot_param( param, value ):
    matplotlib.rcParams[param] = value


def set_plot_size( width, height ):
    set_plot_param( 'figure.figsize', (width,height) )


