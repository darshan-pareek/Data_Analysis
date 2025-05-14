#!/usr/bin/env python
# coding: utf-8~

# In[55]:


import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# In[57]:


data=pd.read_csv("data.csv")


# In[59]:


data


# In[61]:


df=pd.read_csv("Big_data.csv")


# In[63]:


df


# In[ ]:





# In[66]:


st.title("Dashboard......")


# In[68]:


cluster=data["cluster"].unique()


# In[70]:


select_cluster=st.selectbox("Select a cluster",cluster)


# In[72]:


filter_data=data[data["cluster"]==select_cluster]


# In[ ]:





# In[75]:


st.write(f"no of records in cluster{select_cluster}: {len(filter_data)}")


# In[79]:


st.write(filter_data.describe())


# In[83]:


st.subheader("Cluster Visualization")
fig, ax = plt.subplots()
sns.scatterplot(data=filter_data, x="GDP (nominal, 2023)", y="GDP Growth", hue="cluster", palette="tab10", ax=ax)
st.pyplot(fig)


# In[85]:





# In[ ]:




