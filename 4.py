#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests
from pymongo import MongoClient
from facebook_scraper import get_posts
import json
import time


# In[30]:


client = MongoClient('mongodb+srv://sebas310:18102412@cluster0.htzof.mongodb.net/test')
db=client.nuevo
nombredb='nuevo'
db=client[nombredb]


# In[28]:


i=1
for post in get_posts('olimpics', pages=1000, extra_info=True):
    print(i)
    i=i+1
    time.sleep(5)
    
    id=post['post_id']
    doc={}
     
    doc['id']=id
    
    mydate=post['time']
    
    try:
        doc['texto']=post['text']
        doc['date']=mydate.timestamp()
        doc['likes']=post['likes']
        doc['comments']=post['comments']
        doc['shares']=post['shares']
        try:
            doc['reactions']=post['reactions']
        except:
            doc['reactions']={}

        doc['post_url']=post['post_url']
        db.save(doc)

    
        print("guardado exitosamente")

    except Exception as e:    
        print("no se pudo grabar:" + str(e))


# In[19]:





# In[20]:





# In[22]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




