from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Products
import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Spectral6
from bokeh.embed import components
from bokeh.models import HoverTool, ColumnDataSource, LassoSelectTool, WheelZoomTool
# Create your views here.

def home(request):
    first_graph = "Various Bokeh Graphs And Plots Will Be Rendered On Separate Pages !"
    return HttpResponse(first_graph)

def graph(request):
    title = 'Example Graph with tools'
    plot = figure(title=title)
    plot.star([0, 3, 6, 9], [0, 3, 6, 9], size=64, color="gold")

    script, div = components(plot)

    return render(request, 'home.html', {'script': script, 'div': div})


def graph2(request):
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 8, 9, 12]
    title = 'My Learning Graph'

    plot = figure(title=title,
                  x_axis_label='High and Lows',
                  y_axis_label='Learning Topics',
                  plot_width=700,
                  plot_height=700, tools="",
                  toolbar_location=None,)

    #formating graph
    cr = plot.circle(x, y, size=10, color="green", fill_color="blue", hover_fill_color='firebrick',
                     fill_alpha=0.05, hover_alpha=0.9,
                     line_color=None, hover_line_color="white")
    plot.add_tools(HoverTool(tooltips=None, renderers=[cr], mode='hline'))
    plot.title.text_font_size = '20pt'
    plot.line(x, y, legend='Learning Line', line_width=4, line_color="brown", line_dash='dashed')
    plot.background_fill_color ="lightgrey"
    plot.border_fill_color ='whitesmoke'
    plot.min_border_left = 40
    plot.min_border_right = 40
    plot.outline_line_width = 7
    plot.outline_line_alpha = 0.2
    plot.outline_line_color = "purple"

    #store components
    script, div = components(plot)

    return render(request, 'learnGraph.html', {'script': script, 'div':div})


def combo(request):
    # prepare data
    x = [0.1, 0.5, 1.0, 1.5, 2.7, 2.5, 3.0]
    # using list comprehension to create 3 other data sets
    y0 = [i**7 for i in x]
    y1 = [10**i for i in x]
    y2 = [10**(i**2) for i in x]

    # create new plot
    p = figure(
    tools="pan,box_zoom,wheel_zoom,tap,hover,reset,save",  # this gives tools
    toolbar_location="right",
    y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
    x_axis_label='sections', y_axis_label='particles'
    )

    # add renderers
    p.line(x, x, legend="y=x")  # thin blue line
    p.circle(x, x, legend="y=x", fill_color="white", size=8)  # add circles to y=x line
    p.line(x, y0, legend="y=x^2", line_width=3)  # thick blue line
    p.line(x, y1, legend="y=10^x", line_color="red")  # red line
    p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)  # adds red circles
    p.line(x, y2, legend="10^x^2", line_color="orange", line_dash="7 7") # orange dotted line

    script, div = components(p)

    return render(request, 'combog.html', {'script': script, 'div': div})


def pop(request):
    lang = ['Python', 'JavaScript', 'C#', 'PHP', 'C++', 'Go']
    counts = [25, 30, 8, 22, 12, 17]

    p = figure(x_range=lang, plot_height=450, title="Programming Languages Popularity",
          toolbar_location="above", tools="pan,wheel_zoom,box_zoom,reset,hover,tap,crosshair")

    source = ColumnDataSource(data=dict(lang=lang, counts=counts, color=Spectral6))
    p.add_tools(LassoSelectTool())
    p.add_tools(WheelZoomTool())
    
    p.vbar(x='lang', top='counts', width=.8, color='color', legend="lang", source=source)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    
    p.xgrid.grid_line_color = "black"
    p.y_range.start = 0
    p.line(x=lang, y=counts, color="green", line_width=3)
    
    script, div = components(p)
    
    return render(request, 'programming.html', {'script': script, 'div': div})

 
def products(request):

    shoes = 0
    belts = 0
    shirts = 0
    counts = []
    items = ["Shoes", "Belts", "Shirts"]
    prod = Products.objects.values()

    for i in prod:
        if "Shoes" in i.values() :
            shoes += 1
        elif "Belts" in i.values():
            belts += 1
        elif "Shirts" in i.values():
            shirts += 1
    counts.extend([shoes, belts, shirts])

    plot = figure(x_range=items, plot_height=600, title="Products",
        toolbar_location="right", tools="pan,wheel_zoom,box_zoom,reset,hover,tap,crosshair")
    plot.title.text_font_size = '20pt'

    plot.xaxis.major_label_text_font_size = "14pt"
    plot.vbar(items, top=counts, width=.4, color="green", legend="ProductCounts")
    plot.legend.label_text_font_size = '14pt'

    script, div = components(plot)

    return render(request, 'products.html' , {'script': script, 'div': div})
