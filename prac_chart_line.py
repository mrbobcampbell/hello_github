#line graph
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.random.randn(400)
num_bins = 30
n, bins, patches = plt.hist(x, num_bins, facecolor='blue')
plt.show()

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(100)

n, bins, patches = plt.hist(x, 10, normed=1, facecolor='blue', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram')
plt.axis([40, 160, 0, 0.08])
plt.grid(True)

plt.show()


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.random.randn(400)
num_bins = 30
n, bins, patches = plt.hist(x, num_bins, facecolor='blue')
plt.show()
