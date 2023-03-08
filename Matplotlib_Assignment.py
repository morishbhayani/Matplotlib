#!/usr/bin/env python
# coding: utf-8

# #Q1
# Ans. Matplotlib is a data visualization tool used to plot and draw graphs which help in better understanding of the subject and analyzing of problems.
# Five plots that can be plotted are:-
# 1.plt.plot()- Plots line plot.
# 2.plt.bar()- Plots bar graph.
# 3.plt.scatter()- Plots scatter plot.
# 4.plt.pie()- Plots pie plot.
# 5.plt.hist()- Plots histogram.
# 

# #Q2
# Ans.Scatter plot is expressed as a collection of data points.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))


# In[6]:


plt.scatter(x,y)
plt.xlabel('Random_X')
plt.ylabel('Random_Y')
plt.title("Scatter")


# #Q3
# Ans.Subplot is used to compare two or more graphs in a single plot

# In[16]:


x1 = np.array([0, 1, 2, 3, 4, 5]) 
y1 = np.array([0, 100, 200, 300, 400, 500])
plt.subplot(2,2,1)
plt.plot(x1,y1)
x2 = np.array([0, 1, 2, 3, 4, 5]) 
y2 = np.array([50, 20, 40, 20, 60, 70])
plt.subplot(2,2,2)
plt.plot(x2,y2)
x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])
plt.subplot(2,2,3)
plt.plot(x3,y3)
x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])
plt.subplot(2,2,4)
plt.plot(x4,y4)


# #Q4
# Ans.Bar plot is used to plot bar graph.

# In[19]:


company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.barh(company,profit)


# #Q5
# Ans.Box plot is used to find median,quartile range,inter quartile range and outliers in a dataset.
# 

# In[25]:


box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
box = [box1,box2]
plt.boxplot(box)


# In[ ]:




