import random
import datetime
import matplotlib.pyplot as plt

from matplotlib.pyplot import style
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.dates import DateFormatter

style.use('dark_background')
color_pattern_red = ['brown', 'firebrick', 'maroon', 'darkred', 'red']
color_patter_traffic = ['red', 'orange', 'darkgreen']
color_pattern_hide = ['black', 'black', 'black', 'black', 'black']
color_pattern_blue = ['skyblue', 'lightskyblue', 'steelblue', 'dodgerblue', 'cadetblue']
color_pattern_red_blue = ['skyblue', 'lightskyblue', 'steelblue', 'darkred', 'red']
color_pattern_fade_red = ['maroon', 'firebrick', 'darkorange', 'orange']

def Create_Pie():

	fig = plt.Figure()
	ax = fig.add_subplot(111)
	# service_df.plot.pie()
	ax.pie(service_df, colors=color_pattern_fade_red, labels=service_df.index, explode=(0.05, 0.05, 0.05))
	# added to crop central part of pie
	ax.pie(range(0, 3), colors=color_pattern_hide, radius=0.75)  # , explode=(0.05, 0.05, 0.05, 0.05, 0.05))

	# Add next layer of pie chart
	# ax.pie(service_df,  colors=color_pattern_red_blue, radius=0.6, labels=service_df.index)
	#       explode=(0.05, 0.05, 0.05))
	# added to crop central part of pie
	# ax.pie(range(0, 3), colors=color_pattern_hide, radius=0.35) #, explode=(0.05, 0.05, 0.05, 0.05, 0.05) )
	FigureCanvas(fig)

	# Set figure size
	fig.set_size_inches(width, height)

	# save the figure to file
	file_path = 'images/' + file_name + '.png'
	fig.savefig("static/" + file_path)

	return file_path

def Create_Bar():


	fig = plt.Figure()
	ax = fig.add_subplot(111)
	x = []
	y = []
	now = datetime.datetime.now()
	delta = datetime.timedelta(days=1)
	for i in range(100):
		x.append(now)
		now += delta
		y.append(random.randint(0, 1000))

	bars = ax.bar(x, y, color='firebrick', align='center', linewidth=4)
	ax.tick_params(bottom='off', top='off', left='off', right='off', labelleft='off', labelbottom='off')
	for spine in ax.spines.values():
		spine.set_visible(False)
	ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
	fig.autofmt_xdate()

	for bar in bars:
		ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, str(int(bar.get_height())),
		        ha='center', color='w', fontsize=6)


	FigureCanvas(fig)

	# Set figure size
	fig.set_size_inches(width, height)

	# save the figure to file
	file_path = 'images/' + file_name + '.png'
	fig.savefig("static/" + file_path)

	return file_path