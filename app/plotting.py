import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.ticker import NullFormatter
from matplotlib.backend_bases import FigureCanvasBase as FigureCanvas
import math
plt.rcParams['axes.color_cycle'] = ['r', 'g', 'b', 'c']
plt.rcParams['lines.color'] = 'r'
plt.rcParams['figure.figsize'] = (15, 5)

spines = ['bottom','top','left','right']

def get_scatter():
	ratios = {}
	ratios['hits_over_searches'] = pd.read_csv('hits_over_searches.csv')
	ratios['searches_over_stops'] = pd.read_csv('searches_over_stops.csv')
	# the random data
	x = np.random.randn(1000)
	y = np.random.randn(1000)

	nullfmt = NullFormatter()         # no labels

	# definitions for the axes
	left, width = 0.1, 0.65
	bottom, height = 0.1, 0.65
	bottom_h = left_h = left + width + 0.02

	rect_scatter = [left, bottom, width, height]
	rect_histx = [left, bottom_h, width, 0.2]
	rect_histy = [left_h, bottom, 0.2, height]

	# start with a rectangular Figure
	fig = plt.figure(1, figsize=(8, 8))

	axScatter = plt.axes(rect_scatter)
	axHistx = plt.axes(rect_histx)
	axHisty = plt.axes(rect_histy)
	for spine in spines:
	    axScatter.spines[spine].set_color('white')

	# no labels
	axHistx.xaxis.set_major_formatter(nullfmt)
	axHisty.yaxis.set_major_formatter(nullfmt)

	alpha = 1. #.5

	hits = {}
	hits['black'] = ratios['hits_over_searches']['black'].values
	hits['white'] = ratios['hits_over_searches']['white'].values
	searches = {}
	searches['black'] = ratios['searches_over_stops']['black'].values
	searches['white'] = ratios['searches_over_stops']['white'].values
	axScatter.set_ylabel('Hits / Searches',color='white')
	axScatter.set_xlabel('Searches / Stops',color='white')
	black = axScatter.scatter(searches['black'],hits['black'],color='r',alpha=alpha,label='Black Drivers')
	white = axScatter.scatter(searches['white'],hits['white'],color='b',alpha=alpha,label='White Drivers')
	axScatter.tick_params(axis='x', colors='white')
	axScatter.tick_params(axis='y', colors='white')

	#plt.legend([black,white])




	# now determine nice limits by hand:
	ylim = [0,.8]
	xlim = [0,.25]
	axScatter.set_xlim(xlim)
	axScatter.set_ylim(ylim)
	xbinwidth = 0.025
	ybinwidth = .1
	binsx = np.arange(xlim[0], xlim[1] + xbinwidth, xbinwidth)
	binsy = np.arange(ylim[0], ylim[1] + ybinwidth, ybinwidth)
	print binsy
	density_hits = {}
	density_hits['black'] = stats.kde.gaussian_kde(hits['black'])
	density_hits['white'] = stats.kde.gaussian_kde(hits['white'])
	density_searches = {}
	density_searches['black'] = stats.kde.gaussian_kde(searches['black'])
	density_searches['white'] = stats.kde.gaussian_kde(searches['white'])

	x = np.arange(xlim[0],xlim[1], .001)

	y = np.arange(ylim[0],ylim[1], .001)
	axHisty.plot(density_hits['black'](y),y,color='r',alpha=alpha) #,orientation='horizontal') # bins=binsy,facecolor='r',alpha=alpha,edgecolor='r',orientation='horizontal',histtype='step')
	axHisty.plot(density_hits['white'](y),y,color='b',alpha=alpha) #,orientation='horizontal') # bins=binsy,facecolor='r',alpha=alpha,edgecolor='r',orientation='horizontal',histtype='step')
	axHistx.plot(x,density_searches['black'](x),color='r',alpha=alpha) #,orientation='horizontal') # bins=binsy,facecolor='r',alpha=alpha,edgecolor='r',orientation='horizontal',histtype='step')
	axHistx.plot(x,density_searches['white'](x),color='b',alpha=alpha) #,orientation='horizontal') # bins=binsy,facecolor='r',alpha=alpha,edgecolor='r',orientation='horizontal',histtype='step')

	#axHisty.hist(hits['black'], bins=binsy,facecolor='r',alpha=alpha,edgecolor='r',orientation='horizontal',histtype='step')
	#axHisty.hist(hits['white'], bins=binsy,facecolor='b',alpha=alpha,edgecolor='b',orientation='horizontal',histtype='step')
	#axHistx.hist(searches['black'], bins=binsx,facecolor='r',alpha=alpha,edgecolor='r',histtype='step')
	#axHistx.hist(searches['white'], bins=binsx,facecolor='b',alpha=alpha,edgecolor='b',histtype='step')


	axHistx.set_xlim(axScatter.get_xlim())
	#axHistx.set_ylim([0,40])
	axHistx.set_ylabel('Density of Agencies in NC',color='white')
	axHistx.tick_params(axis='x', colors='white')
	axHistx.tick_params(axis='y', colors='white')


	axHisty.set_ylim(axScatter.get_ylim())
	#axHisty.set_xlim([0,50])
	#axHisty.set_xlabel('Agencies in NC')
	axHisty.set_xlabel('Density of Agencies in NC',color='white')
	axHisty.tick_params(axis='x', colors='white')
	axHisty.tick_params(axis='y', colors='white')

	for spine in spines:
	    axHistx.spines[spine].set_color('white')
	    axHisty.spines[spine].set_color('white')


	canvas = FigureCanvas(fig)
	img = BytesIO()
	#fig.patch.set_facecolor('red')
	
	fig.savefig(img,transparent=True)
	img.seek(0)
	return img
