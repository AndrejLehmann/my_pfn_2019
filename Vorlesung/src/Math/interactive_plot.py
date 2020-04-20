import numpy as np
from bokeh.plotting import figure as bokeh_plot
from bokeh.layouts import row as bokeh_row
from bokeh.layouts import column as bokeh_column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.io import curdoc

def update_cd_source(cd_source,func,args,np_x_vec):
  np_y_vec = np.array([func(args,x) for x in np_x_vec])
  cd_source.data = {'x_vec' : np_x_vec, 'y_vec' : np_y_vec}

class InteractivePlot:
  def __init__(self,plt_title,x_min,x_max,color,func,sliders_spec):
    sliders = list()
    init_args = list()
    consts = list()
    for s_desc, s_name, s_min, s_max, s_init in sliders_spec:
      sliders.append(Slider(title='{}{}'.format(s_desc,s_name),
                            value=s_init,start=s_min,end=s_max,
                            step=(s_max-s_min)/100))
      init_args.append(s_init)
      consts.append('{} <= {} <= {}'.format(s_min,s_name,s_max))
    num_points = 200
    np_x_vec = np.linspace(x_min,x_max,num_points)
    np_y_vec = np.array([func(init_args,x) for x in np_x_vec])
    y_min, y_max = min(np_y_vec), max(np_y_vec)
    plot = bokeh_plot(plot_width=600,
                      plot_height=400,
                      title='{} for {}'
                             .format(plt_title,', '.join(consts)),
                      x_range=[x_min,x_max],
                      y_range=[y_min,y_max])
    cd_source = ColumnDataSource()
    update_cd_source(cd_source,func,init_args,np_x_vec)
    plot.line(x='x_vec', y='y_vec', source=cd_source, line_width=1,
              line_color=color,line_alpha=0.6)
    def update_data(attr,new,old):
      slider_values = [slider.value for slider in sliders]
      update_cd_source(cd_source,func,slider_values,np_x_vec)
    for slider in sliders:
      slider.on_change('value',update_data)
    first_column = bokeh_column(sliders)
    curdoc().add_root(bokeh_row(first_column, plot, width=800))
