# -*- coding: utf-8 -*-

# -- Sheet --

# After eating chocolate bars your whole life, you’ve decided to go on a quest to find the greatest chocolate bar in the world.
# 
# You’ve found a website that has over 1700 reviews of chocolate bars from all around the world. It’s displayed in the web browser on this page.
# 
# The data is displayed in a table, instead of in a csv or json. Thankfully, we have the power of BeautifulSoup that will help us transform this webpage into a DataFrame that we can manipulate and analyze.


# Some questions we thought about when we found this dataset were:
# 
# **Where are the best cocao beans grown?**
# 
# **Which countries produce the highest-rated bars?**
# 
# **What’s the relationship between cocao solids percentage and rating?**



from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# **Let’s make a request to this site to get the raw HTML, which we can later turn into a BeautifulSoup object.**


webpage =  requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content,"html.parser")

# **How many terrible chocolate bars are out there? And how many earned a perfect 5?**


b = soup.find_all(attrs={'class':'Rating'})
#print(b)

ratings = []
ctr = 0

for i in b:
  a = BeautifulSoup.get_text(i)
  if ctr == 0:
    ctr += 1
    continue
  ratings.append(float(a))


#print(ratings)
plt.hist(ratings)
plt.show()



comp = soup.select(".Company")

complist = []
for i in comp:
  a = BeautifulSoup.get_text(i)
  complist.append(a)
complist.pop(0)


# **We want to now find the 10 most highly rated chocolatiers.
# One way to do this is to make a DataFrame that has the chocolate companies in one column, and the ratings in another. Then, we can do a groupby to find the ones with the highest average rating.**


d = {"Ratings":ratings,"Company":complist}
your = pd.DataFrame.from_dict(d)
y = your.groupby("Company").Ratings.mean()
best = y.nlargest(10)
print(best)

# **Checking the highest Cocoa Percentage in Chocolate Bars with respect to the ratings by creating the Best-Fit over the scatterplot with basic Numpy commands**


cocoa = soup.select(".CocoaPercent")
cocalist = []
for i in cocoa:
  a = BeautifulSoup.get_text(i)
  cocalist.append(a)
cocalist.pop(0)
coca = list(map(lambda x: x[:-1],cocalist))
coca = list(map(float,coca))

d["CocoaPercentage"] = coca
yours = pd.DataFrame.from_dict(d)
print(yours)

d["CocoaPercentage"] = coca
yours = pd.DataFrame.from_dict(d)
print(yours)

plt.clf()
plt.scatter( yours.CocoaPercentage,yours.Ratings)
z = np.polyfit(yours.CocoaPercentage, yours.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(yours.CocoaPercentage, line_function(yours.CocoaPercentage), "r--")
plt.show()

a = soup.select(".Origin")
b = soup.select(".CocoaPercent")
threebroadbean = []
for i in a:
  text = BeautifulSoup.get_text(i)
  threebroadbean.append(text)
  
threebroadbean.pop(0)

# **Now let's hop on to find which regions cultivate the best beans of them all. We will operate by taking the already computed Origin and Percent values in a dictionary and then Grouping them by percent.**


newd = dict()
newd["Origin"] = threebroadbean
newd["Percent"] = coca
ogperc = pd.DataFrame.from_dict(newd)
ogperc = ogperc.groupby("Percent").sum()
res = ogperc[::-1]
print(res["Origin"])

# **In this module, we will scale the companies with highest amount of chocolate bar production with the us of Python libraries like Numpy and Matplotlib.**


#print(coca) #Coca Percent
print(complist)
nd = {"Companies":complist}

