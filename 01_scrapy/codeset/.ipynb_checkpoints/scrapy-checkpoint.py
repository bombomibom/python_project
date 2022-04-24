#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. 라이브러리 선언 및 html 수집
import requests
import bs4
import pandas as pd
import datetime as dt

targetUrl = "https://www.samsung.com/sec/"

try:
    resp = requests.get(targetUrl)
except Exception as e:
    print(e)

bs = bs4.BeautifulSoup(resp.text, 'html.parser')


# In[3]:


# 2. 수집하려는 소스 찾아가기
divTag = bs.find(name = "div", attrs = {"class":"footer-content"})
divTag

liTag = divTag.find(name = "li", attrs = {"class":"over"})
liTag

aTag = liTag.findAll("a")
aTag


# In[4]:


# 3. for문 돌리기 및 list 맨 앞 데이터 빼기
aTagLen = len(aTag)-1
aTagLen

nameList = []
linkList = []

for i in range(0, aTagLen):
    tagTextName = aTag[i].text
    if aTag[i].attrs["href"][1] == "#": # 링크의 시작문자가 #이면
        tagLinkInfo = targetUrl + aTag[1].attrs["href"]
    else:
        tagLinkInfo = aTag[i].attrs["href"]
   
    nameList.append(tagTextName)
    linkList.append(tagLinkInfo)

nameList = nameList[1:]
linkList = linkList[1:]


# In[5]:


# 4. 데이터프레임 만들기
finalDf = pd.DataFrame(zip(nameList, linkList), columns=["제품명","링크"])
finalDf


# In[7]:


# 5. dataset에 수집 정보 넣기
currentData = dt.datetime.now()
timelog = "_{}_{}_{}".format(currentData.hour,
                            currentData.minute,
                            currentData.second)

finalDf.to_csv("../dataset/samsung_scrapy{}.txt".format(timelog), encoding="ms949")


# In[ ]:




