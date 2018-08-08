import big_data_tools.bokeh_tools
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
from bokeh.models import NumeralTickFormatter
import csv
import big_data_tools.bokeh_tools.histogram
p = figure(plot_width=800, plot_height=300, title="Title")
from scipy import stats

#show(p)
f  = []
with open('moisture_temps/part-00000-3cd03f51-a846-4a24-8fa4-f8342d2ab672-c000.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for line in csv_reader:
        try:
            x = float(line[1])
            y = float(line[2])
            if y > 100:
                continue
            f.append((x, y))
        except ValueError:
            continue
f = sorted(f)
x = [x[0] for x in f]
y = [x[1] for x in f]
p.line(x, y, line_width =2,legend=None )
p.yaxis.formatter=NumeralTickFormatter(format="0,")
#big_data_tools.bokeh_tools.histogram.hist([x for x in y if x != None])
show(p)
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print(p_value)
