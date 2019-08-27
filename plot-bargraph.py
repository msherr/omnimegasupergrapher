"""
Written by Micah Sherr <msherr@cs.georgetown.edu>
Georgetown University
"""

import numpy as np
import matplotlib
matplotlib.use('Agg') # for systems without X11
import matplotlib.pyplot as plt
import plotdefaults as defaults





"""
plots a bar plot

arguments:
  num_colors : number of different colors
  color_labels : labels for the colors
  num_values : number of values for a given color 
          (i.e., number of bars across the x-axis)
  values[color][values_across_x_axis] : for each color, 
          the values across the x axis
  lerrs[color][values_across_x_axis] : for each color, 
          the lower error bar value across the x axis
  herrs[color][values_across_x_axis] : for each color, 
          the higher error bar value across the x axis
returns:
  the plot
"""
def make_bar_plot():
    # create plot
    defaults.set_default_plot_options()
    defaults.set_plot_size(10,4)

    fig, ax = plt.subplots()
    index = np.arange(num_values)
    bar_width = 1.0 / (num_colors+1)
    opacity = 0.8

    # STOPPED HERE
    counter = 0
    for color in range(0,num_colors):
        name = os.path.basename(color)
        if args.names is not None: name = args.names[counter]

        # compute the values for this service across the different sites
        vals = []
        lerrs = []
        herrs = []
        for ext in urls:                   # e.g., netflix, hulu
            vals += [ data_idx_by_ext[ext][color] ]
            lerrs += [ lerr_idx_by_ext[ext][color] ]
            herrs += [ herr_idx_by_ext[ext][color] ]

        # plot the actual bar
        plt.bar(
            index + (bar_width * counter),
            list(vals),
            bar_width,
            alpha=opacity,
            label=name,
            yerr = [ lerrs, herrs ],
            error_kw = {
                'elinewidth' : 0.5,
                'capsize' : 1.5
            }
        )

        counter += 1

    plt.xticks(rotation=45)
    plt.xlabel( 'Site' )
    plt.ylabel( 'Fetch time (s)' )
    plt.xticks(
        index + bar_width,
        urls)
    plt.legend()

    if args.lineafter is not None:
        xpos = bar_width * (len(args.inputfiles)+1) * args.lineafter
        xpos -= bar_width 
        ax.axvline( xpos, color='blue', ls='-.' )

    plt.tight_layout()
    plt.savefig( args.output )
    # plt.show()
"""
    
    
if __name__== "__main__":
    make_bar_plot()
    


