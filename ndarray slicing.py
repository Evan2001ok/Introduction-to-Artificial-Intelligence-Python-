#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np

x = np.arange(1,17).reshape(4,4)
z = x[1:, 1:].copy()
z[2,2] = 100
print(x)


# In[ ]:




