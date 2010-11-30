import pylab
import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../src'))


from loess import loess_query

X = np.fromfile('q2x.dat', sep='\n')
y = np.fromfile('q2y.dat', sep='\n')

X = np.mat(X).T

pylab.cla()
pylab.scatter(X, y)
pylab.hold(True)

x_axis = pylab.arange(min(X), max(X), 0.1)
y_axis = []
for x in x_axis:
  y_axis.append(loess_query(x, X, y, 0.35))

y_axis = np.array(y_axis)

pylab.plot(x_axis, y_axis, linewidth=1.0)
pylab.show()