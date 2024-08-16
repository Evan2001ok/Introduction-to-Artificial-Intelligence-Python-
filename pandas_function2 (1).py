#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import numpy as np

#pd.set_option('precision', 1)

books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])
user_1 = pd.Series(data = [3.2, np.nan ,2.5,np.nan,np.nan])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8, np.nan])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4,np.nan])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

dat = {'Book Title' : books,'Author' : authors,'User 1' : user_1,'User 2' : user_2,'User 3' : user_3,'User 4' : user_4}

book_ratings = pd.DataFrame(dat)
#NaN is mean of columns values
numeric_cols = book_ratings.select_dtypes(include=[np.number])
book_ratings[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())

book_ratings


# In[ ]:




