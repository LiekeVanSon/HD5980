import numpy as np
import os, sys
from astropy.table import Table
import matplotlib.pyplot as plt
from matplotlib import colorbar as cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes

cmap = plt.cm.plasma(np.linspace(0,1,20)) #3rd num is the number of colours
cmap = cmap[::-1]
purples = ListedColormap(cmap[0:14])

cmap = plt.cm.autumn(np.linspace(0,1,20)) #3rd num is the number of colours
cmap = cmap[::-1]
YlRed = ListedColormap(cmap[5:18])



#Plot the HR diagram with different colour values
def HR_diagram(history, colour_by = 'star_age',save_loc = './', colors = 'rainbow',numdir=0,  Vmin = 'auto', Vmax = 'auto', x_lim = (3.9,4.5), y_lim = (1.25, 4.25)):
    colors = ['rainbow', r'rainbow']#[purples, YlRed]
    msizes = [7,1]
        
    if history == None:
        return None
    
    fig, ax = plt.subplots(figsize=(10,10))

    mzams = 'M$_{i}$ '+str(round(history['star_mass'][0],2) )+'M$_{\odot}$'
    try:
        Pzams = 'P$_{i}$ '+str(round(history['period_days'][0],1) )+ 'd'
    except:
        Pzams = 'P$_{i}$ '+str(-1)+ 'd'
       
    print(mzams, Pzams)
    if Vmin == 'auto':
        Vmin = min(history[colour_by])
#             print('Vmin',Vmin)
    if Vmax == 'auto':
        Vmax = min(history[colour_by]) + 1 #max(history[colour_by])   
#             print('Vmax',Vmax)

    history['star_age'] = history['star_age']*1e-6 #in Myr
    history['dM']  = history['star_mass'][0] - history['star_mass']

    #############    #############    ############# 
    ax.scatter(history['log_Teff'][0], history['log_L'][0],marker = '*',s = 200, edgecolor = 'k',label = None,c = 'yellow',alpha = 1., zorder = 50) 
    ax.text(history['log_Teff'][-1], history['log_L'][-1], str(numdir), size = 15, zorder = 50) 
    ax.text(history['log_Teff'][0]- 0.01, history['log_L'][0], mzams+', '+Pzams)

    im = ax.scatter(history['log_Teff'], history['log_L']\
                ,marker = 'o',s = 7,label = None, c = history[colour_by], cmap = colors[0] ,alpha = 0.75,vmin=Vmin, vmax= Vmax) # 
    cb = plt.colorbar(im, ax = ax)
    cb.set_label(mzams + colour_by, size = 25)
    cb.ax.tick_params(labelsize=20)

    if y_lim:
        ax.set_ylim(y_lim)
    if x_lim:
        ax.set_xlim(x_lim)

    ax.set_ylabel('log$_{10}$(L/L$_{\odot}$)',fontsize = 22)
    ax.set_xlabel('log$_{10}$(T$_{eff}$/K)',fontsize = 22)
    ax.tick_params(axis='both', which='major', labelsize=20)
#     ax.legend(loc = 'lower left', fontsize = 'large')
    ax.invert_xaxis()
    plt.tight_layout()
#     try:
#         plt.savefig(basedir+ save_loc+'HR'+colour_by+'.png')
#     except:
#         os.mkdir(basedir + save_loc)#,0o775)
#         plt.savefig(basedir+ save_loc+'HR'+colour_by+'.png')

#     plt.close()
#     plt.show()
    return im
    