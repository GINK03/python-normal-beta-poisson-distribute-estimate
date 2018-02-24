import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

from scipy.misc import factorial

data = np.random.poisson(2, 10000)

d_freq = {}
for d in data.tolist():
  if d_freq.get(d) is None:
    d_freq[d] = 0
  d_freq[d] += 1
for d, freq in sorted( d_freq.items(), key=lambda x:x[0]):
  #print(d, freq)
  ...
entries, bin_edges, patches = plt.hist(data, bins=11, range=[-0.5, 10.5], normed=True)

# set bin middle
bin_middles = 0.5*(bin_edges[1:] + bin_edges[:-1])

# フィットに用いる関数をを設定することができるので、
# poassonを書く未知をパラメータ未知のママ扱う
def poisson(k, lamb):
  return (lamb**k/factorial(k)) * np.exp(-lamb)

# fit with curve_fit
# paramtersでポアソン分布のパラメータ(lamb,)が出る
parameters, cov_matrix = curve_fit(poisson, bin_middles, entries) 
print(parameters, cov_matrix)

# poisson関数に決定した変数お埋め込む
x_plot = np.linspace(0, 20, 1000)
po = poisson(x_plot, *parameters)
#print(po)

