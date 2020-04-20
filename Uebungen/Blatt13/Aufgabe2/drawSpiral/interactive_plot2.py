from math import ceil, floor
from bokeh.plotting import figure as bokeh_plot
from bokeh.layouts import row as bokeh_row
from bokeh.layouts import column as bokeh_column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.io import curdoc

def update_cd_source(cd_source,func,args):
  x_vector, y_vector = func(args)
  cd_source.data = {'x_vec' : x_vector, 'y_vec' : y_vector}

class InteractivePlot2:
  def __init__(self,plt_title,color,func,sliders_spec):
    sliders = list()
    init_args = list()
    consts = list()
    for s_desc, s_name, s_min, s_max, s_init, s_step in sliders_spec:
      sliders.append(Slider(title='{}{}'.format(s_desc,s_name),
                            value=s_init,start=s_min,end=s_max,
                            step=s_step))
      init_args.append(s_init)
      consts.append('{} <= {} <= {}'.format(s_min,s_name,s_max))
    x_vector, y_vector = func(init_args)
    x_min, x_max = floor(min(x_vector)), ceil(max(x_vector))
    y_min, y_max = floor(min(y_vector)), ceil(max(y_vector))
    plot = bokeh_plot(plot_width=600,
                      plot_height=600,
                      title='{} for {}'
                             .format(plt_title,', '.join(consts)),
                      x_range=[x_min,x_max],
                      y_range=[y_min,y_max])
    cd_source = ColumnDataSource()
    update_cd_source(cd_source,func,init_args)
    plot.line(x='x_vec', y='y_vec', source=cd_source, line_width=0.6,
              line_color=color,line_alpha=1)
    def update_data(attr,new,old):
      slider_values = [slider.value for slider in sliders]
      update_cd_source(cd_source,func,slider_values)
    for slider in sliders:
      slider.on_change('value',update_data)
    first_column = bokeh_column(sliders)
    curdoc().add_root(bokeh_row(first_column, plot, width=800))
