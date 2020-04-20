def prepare_plot_data(f,x_min,x_max,
                      numpoints):
  stepwidth = (x_max - x_min)/numpoints
  x_list = list()
  y_list = list()
  for p in range(numpoints+1):
    x = x_min + p * stepwidth
    x_list.append(x)
    y_list.append(f(x))
  return x_list, y_list

def prepare_plot_data_lc(f,x_min,x_max,numpoints):
  stepwidth = (x_max - x_min)/numpoints
  x_list = [x_min + p * stepwidth for p in range(numpoints+1)]
  y_list = [f(x) for x in x_list]
  return x_list, y_list
