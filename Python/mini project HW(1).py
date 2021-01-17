#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plot
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot
from datetime import datetime 
df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv',index_col=0)

df1=df.groupby(['date'])['cases'].count()
df1.tail(30)#figure out last 30days
df2=df.loc[('2020-12-16'):('2021-1-16')]#Filtering a months data
df2


# In[69]:


df3=df2[df2['state']=='New York']
df3.fillna(method='ffill')# fill with previous data if missing data
df3_copy= df3.copy()# copy df3 
df3


# In[70]:


df4=df3[df3['county']=='Wayne']# restrict into one county
df5=df4.copy()#Copy df4 to df5 
df4.drop('fips',axis=1,inplace=True)# remove fipsplot()
df4.plot()# cases increases
start = datetime(2020,12,16)
end = datetime(2021,1,16)    

f = df3.DataReader(df, 'cases',start,end)
df5 = pd.DataFrame(f.to_frame().stack()).reset_index()
df.columns = ['Date', 'cases', 'deaths']

sns.tsplot(df, time='date', unit='case', value='deaths')


# In[71]:


df4.drop('cases',axis=1,inplace=True)# remove cases()
df4.plot()# deaths increases


# Try  manipulate data as a state
# 

# In[29]:


df3['new_cases']=df3['cases']-df3['cases'].shift(58).fillna(0)
df3
#there are 58 state in NYC, so the datafrequency is 58


# In[30]:


df3['new_deaths']=df3['deaths']-df3['deaths'].shift(58).fillna(0)
df3


# In[31]:


new=df3.drop(['2020-12-16','2021-01-16'], axis=0)
new
#drop two end data, first day data droped because there are no previous case, the last day data dropped because the last day data is not completed


# In[32]:


new.describe()


# In[33]:


new.drop('cases',axis=1,inplace=True)
new.drop('deaths',axis=1,inplace=True)
new.drop('fips',axis=1,inplace=True)
new.drop('state',axis=1,inplace=True)
new


# In[34]:


new.describe()


# there are 232 cases and 2.7 deaths in each county perday 

# In[36]:


new2=new.groupby(['county'])[['new_cases','new_deaths']].sum()
new2


#  that means the raw data is not accumulated

# In[40]:


case = new2.plot.bar(rot=0)


# new york city has most cases in the last thirty days

# In[44]:


new2.drop('new_cases',axis=1,inplace=True)
death = new2.plot.bar(rot=0)


# In[54]:


sns.pairplot(new)


# New_deaths are lead by new cases

# In[ ]:




