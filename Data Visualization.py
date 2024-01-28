#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib
from matplotlib.backends.backend_agg import FigureCanvas as FigureCanvas
from matplotlib.figure import Figure
fig= Figure()
canvas= FigureCanvas(fig)
import numpy as np
x= np.random.randn(10000)
ax= fig.add_subplot(111)
ax.hist(x, 100)
ax.set_title('Normal distrubation')
fig.savefig('matplotlib_histogram1.jpeg')


# In[21]:


import matplotlib.pyplot as plt
import numpy as np
x= np.random.randn(10000)
plt.title('Normal distrubation')
plt.savefig('matplotlib_histogram.jpeg')
plt.show()


# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.plot(5,5,'o')
plt.show()


# In[28]:


fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x));


# In[27]:


plt.plot(x, np.sin(x));


# In[25]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
fig = plt.figure()
ax = plt.axes()


# In[29]:


plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x));


# In[30]:


plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported


# In[31]:


plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted');

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':');  # dotted


# In[32]:


plt.plot(x, x + 0, '-g')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r');  # dotted red


# In[33]:


plt.plot(x, np.sin(x))

plt.xlim(-1, 11)
plt.ylim(-1.5, 1.5);


# In[34]:


plt.plot(x, np.sin(x))

plt.xlim(10, 0)
plt.ylim(1.2, -1.2);


# In[35]:


plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5]);


# In[36]:


plt.plot(x, np.sin(x))
plt.axis('tight');


# In[37]:


plt.plot(x, np.sin(x))
plt.axis('equal');


# In[38]:


plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)");


# In[39]:


plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')

plt.legend();


# In[40]:


ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot');


# In[ ]:




