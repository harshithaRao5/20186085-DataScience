#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np # imports a fast numerical programming library
import scipy as sp #imports stats functions, amongst other things
import matplotlib as mpl # this actually imports matplotlib
import matplotlib.cm as cm #allows us easy access to colormaps
import matplotlib.pyplot as plt #sets up plotting under plt
import pandas as pd #lets us handle data as dataframes
#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns #sets up styles and gives us more plotting options


# In[7]:


df=pd.read_csv("https://raw.githubusercontent.com/cs109/2015lab1/master/all.csv", header=None,
               names=["rating", 'review_count', 'isbn', 'booktype','author_url', 'year', 'genre_urls', 'dir','rating_count', 'name'],
)
df.head()


# In[8]:


df.dtypes


# In[9]:


df.shape


# In[10]:


df.shape[0], df.shape[1]


# In[11]:



df.columns


# In[12]:


type(df.rating), type(df)


# In[24]:


df.query("rating < 3")


# In[14]:


np.sum(df.rating < 3)


# In[16]:


print(1*True, 1*False)


# In[17]:


np.sum(df.rating < 3)/df.shape[0]


# In[19]:


np.sum(df.rating < 3)/(df.shape[0])


# In[20]:


np.mean(df.rating < 3.0)


# In[21]:


(df.rating < 3).mean()


# In[22]:


df.query("rating > 4.5")


# In[23]:


df[df.year < 0]


# In[25]:


df[(df.year < 0) & (df.rating > 4)]


# In[26]:


df[df.year.isnull()]


# In[27]:


df = df[df.year.notnull()]
df.shape


# In[31]:


df['rating_count']=df.rating_count.astype(int)
df['review_count']=df.review_count.astype(int)
df['year']=df.year.astype(int)


# In[32]:


df.dtypes


# In[33]:


df.rating.hist();


# In[36]:


sns.set_context("notebook")
meanrat=df.rating.mean()
#you can get means and medians in different ways
print(meanrat, df.rating.median())
with sns.axes_style("whitegrid"):
    df.rating.hist(bins=30, alpha=0.4);
    plt.axvline(meanrat, 0, 0.75, color='r', label='Mean')
    plt.xlabel("average rating of book")
    plt.ylabel("Counts")
    plt.title("Ratings Histogram")
    plt.legend()
    #sns.despine()


# In[42]:


df.review_count.hist(bins=np.arange(0, 40000, 400))


# In[43]:


df.review_count.hist(bins=100)
plt.xscale("log");


# In[44]:


plt.scatter(df.year, df.rating, lw=0, alpha=.08)
plt.xlim([1900,2010])
plt.xlabel("Year")
plt.ylabel("Rating")


# In[ ]:




