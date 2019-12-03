#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv('Modules.csv')


# In[8]:


def FuelCalc(Mod):
    fuel = int(Mod/3)-2
    
    if fuel > 0:
        total_fuel = fuel
    else: total_fuel = 0
    
    while fuel >=0:
        fuel = int(fuel/3)-2
        
        if fuel > 0:
            total_fuel = total_fuel + fuel
            
    return total_fuel
        


# In[10]:


df['Fuel']= df.Mods.apply(FuelCalc)


# In[11]:


df.head()


# In[12]:


FuelCalc(100756)


# In[13]:


df.Fuel.sum()


# In[ ]:




