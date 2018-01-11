
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier


# In[100]:


train=pd.read_csv('C:/Users/Purva Sawant/Desktop/training_v2.csv',usecols=['pct.deaths.5y','PCV13.Price'])
train


# In[10]:


train['Type']='Train' #Create a flag 
train.head


# In[92]:


train[['pct.deaths.5y','PCV13.Price']].describe()


# In[13]:


ID_col=['REF_NO']


# In[14]:


target_col=["Account.Satstus"]


# In[1]:


train.index


# In[24]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


# In[25]:


regr = linear_model.LinearRegression()


# In[50]:


test=pd.read_csv('C:/Users/Purva Sawant/Desktop/testing_v2.csv',usecols=['pct.deaths.5y','PCV13.Price'])
test


# In[51]:


test[test['PCV13.Price'] - test['PCV13.Price']>0]


# In[59]:


regr = linear_model.LinearRegression()


# In[53]:


regr.fit(train)


# In[101]:


target=train['pct.deaths.5y']


# In[102]:


del train['pct.deaths.5y']


# In[103]:


target=pd.DataFrame(target, columns=['pct.deaths.5y'])


# In[104]:


target.shape


# In[73]:


get_ipython().magic(u'pinfo regr.fit')


# In[118]:


train1=np.array(train['PCV13.Price']).reshape((1,-1))


# In[119]:


target1=np.array(target['pct.deaths.5y']).reshape((1,-1))


# In[120]:


regr.fit(train1,target1)


# In[110]:


train=train[~train['PCV13.Price'].isnull()]


# In[112]:


train.shape


# In[115]:


target.loc[83]


# In[116]:


target=target[~target['pct.deaths.5y'].isnull()]


# In[117]:


target.shape


# In[122]:


predictions = regr.predict(train1)


# In[124]:


predictions.shape


# In[126]:


m = regr.coef_


# In[127]:


b = regr.intercept_


# In[128]:


print "formula: y = {0}x + {1}".format(m, b) 


# In[129]:


m


# In[130]:


plt.scatter(train1, target1,  color='black')


# In[131]:


plt.show


# In[132]:


get_ipython().magic(u'matplotlib notebook')


# In[133]:


import matplotlib as mpl


# In[134]:


import matplotlib.pyplot as plt


# In[143]:


plt.figure()
plt.scatter(train1, target1,  color='black')


# In[136]:


np.corrcoef(train1,target1)


# In[142]:


plt.plot(train1, predictions, color='blue',linewidth=3)
plt.show()

