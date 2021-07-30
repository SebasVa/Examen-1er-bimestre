#!/usr/bin/env python
# coding: utf-8

# In[1]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[2]:


ckey = "XpWZj1B7FfuWKUEFlZsejTqaS"
csecret = "ostfedeyrmkRtlTIa8yXM9XfbLoQ8HhLOyqLjlQVbGOT6vPnvU"
atoken = "1072159494971539456-v1dpnbcfgjEkQxcqGDOoUJdD8FW3nT"
asecret = "1gbUNF9fZse5cxoBPCJopPB0RHVWFXwl13bpWNgor8zBa"


# In[3]:


class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("ya existe")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

server=couchdb.Server('http://sebas:18102412@127.0.0.1:5984')
try:
    db = server.create('track')
except:
    db = server['track']
      
twitterStream.filter(track=['juegos olimpicos'])


# In[ ]:




