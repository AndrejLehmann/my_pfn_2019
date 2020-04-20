from math import ceil, floor
import numpy as np
from bokeh.plotting import figure as bokeh_plot
from bokeh.layouts import row as bokeh_row
from bokeh.layouts import column as bokeh_column
from bokeh.models import ColumnDataSource, Label
from bokeh.models.widgets import Slider
from bokeh.io import curdoc

def update_cd_source(cd_source,cd_eval,cd_circle,func,args,first,second,colors):
  x_vectors, y_vectors = func(args)
  auc = x_vectors[first + second + 1]
  fpr = x_vectors[first + second]
  tpr = y_vectors[first + second]
  cd_source.data = {'x_vectors': x_vectors[:first],
                    'y_vectors': y_vectors[:first],
                    'colors' : colors[:first]}
  cd_eval.data = {'x_evals': x_vectors[first:first + second],
                  'y_evals': y_vectors[first:first + second],
                  'eval_colors' : colors[first:first+second]}
  cd_circle.data = {'t_current_x' : [fpr],
                    't_current_y' : [tpr],
                    'fpr_tpr_text' : ['(fpr(t),tpr(t))=({:.3f},{:.3f})'
                                       .format(fpr,tpr)],
                    'auc' : ['AUC = {:.3f}'.format(auc)]}

class MultiInteractivePlot:
  def __init__(self,plt_titles,first,second,colors,func,sliders_spec):
    sliders = list()
    init_args = list()
    consts = list()
    for s_desc, s_name, s_min, s_max, s_init, s_step in sliders_spec:
      sliders.append(Slider(title='{}{}'.format(s_desc,s_name),
                            value=s_init,start=s_min,end=s_max,
                            step=s_step))
      init_args.append(s_init)
      consts.append('{} <= {} <= {}'.format(s_min,s_name,s_max))
    x_vectors, y_vectors = func(init_args)
    x_values = [x for x_vector in x_vectors[:first] for x in x_vector]
    x_min, x_max = floor(min(x_values)), ceil(max(x_values))
    y_values = [y for y_vector in y_vectors[:first] for y in y_vector]
    y_min, y_max = floor(min(y_values)), ceil(max(y_values))
    plot = bokeh_plot(plot_width=600,
                      plot_height=600,
                      title='{} for {}'
                             .format(plt_titles[0],', '.join(consts)),
                      x_range=[x_min,x_max],
                      y_range=[y_min,y_max])
    eval_plot = bokeh_plot(plot_width=600,
                           plot_height=600,
                           title=plt_titles[1],
                           x_range=[0,1],
                           y_range=[0,1],
                           x_axis_label='false positive rate',
                           y_axis_label='true positive rate')
    cd_source = ColumnDataSource()
    cd_eval = ColumnDataSource()
    cd_circle = ColumnDataSource()
    update_cd_source(cd_source,cd_eval,cd_circle,func,init_args,
                     first,second,colors)
    plot.multi_line(xs='x_vectors',ys='y_vectors',source=cd_source,
                    line_width=0.6,line_color='colors',line_alpha=1)
    eval_plot.multi_line(xs='x_evals',ys='y_evals',source=cd_eval,
                         line_width=0.6,line_color='eval_colors',line_alpha=1)
    eval_plot.circle(x='t_current_x',y='t_current_y',source=cd_circle,
                     color='blue',radius=0.01)
    eval_plot.add_layout(Label(x=0.6, y=0.35,text='fp(t): red >= t'))
    eval_plot.add_layout(Label(x=0.6, y=0.3,text='tp(t): green >= t'))
    eval_plot.text(x=0.6,y=0.2,text='auc',source=cd_circle,legend='AUC')
    eval_plot.text(x=0.6,y=0.25,text='fpr_tpr_text',source=cd_circle)
    def update_data(attr,new,old):
      slider_values = [slider.value for slider in sliders]
      update_cd_source(cd_source,cd_eval,cd_circle,func,slider_values,
                       first,second,colors)
    for slider in sliders:
      slider.on_change('value',update_data)
    first_column = bokeh_column(sliders)
    curdoc().add_root(bokeh_row(first_column, plot, eval_plot,width=800))
