#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[16]:


csv="../../data/external/libimseti/out.tsv"


# In[22]:


df=pd.read_csv(csv,sep='\t', header=0)


# In[18]:


print(df.loc[[1]])


# In[19]:


def create_list(df):

    return df["Initial"].unique().tolist()


# In[ ]:


df=pd.pivot_table(df,columns=["contact"],index=["Initial"])


# In[21]:


print(df)


# In[ ]:




