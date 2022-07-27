#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='latin-1')


# In[7]:


df.head()


# In[11]:


df['Item'].unique()


# In[18]:


animal_fats_df = df[df['Item'] == 'Animal fats']


# In[20]:


animal_fats_df['Y2017'].sum(), animal_fats_df['Y2014'].sum()


# In[22]:


round(df['Y2015'].mean(), 3), round(df['Y2015'].std(),3)


# In[26]:


df['Y2016'].isna().sum(), round(df['Y2016'].isna().sum()/len(df['Y2016']), 2)


# In[27]:


df.corr()


# In[44]:


import_df = df[df['Element'] == 'Import Quantity']
year_df = import_df[['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018']]
year_df.sum()


# In[45]:


sop_df = df[df['Element'] == 'Production']
sop_df['Y2014'].sum()


# In[60]:


df[['Y2018', 'Element']].groupby(['Element']).sum().sort_values(ascending=True, by='Y2018')


# In[57]:


import_df[import_df['Area'] == 'Algeria']['Y2018'].sum()


# In[32]:


algeria_df = df[df['Area'] == 'Algeria']


# In[33]:


algeria_df['Y2018'].sum()


# In[35]:


df['Area'].nunique()


# In[42]:


df['Element'].unique()


# In[ ]:




