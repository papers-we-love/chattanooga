#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd


# In[21]:


df = pd.read_csv('Modules.csv')


# In[22]:


def FuelCalc(Mod):
    return int(Mod/3)-2    


# In[23]:


df['Fuel']= df.Mods.apply(FuelCalc)


# In[24]:


df.head()


# In[25]:


df.Fuel.sum()


# In[ ]:




