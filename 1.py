#!/usr/bin/env python
# coding: utf-8

# In[3]:


import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


# In[4]:


ckey = "caducado"
csecret = "caducado"
atoken = "caducado"
asecret = "caducado"


# In[5]:


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
    db = server.create('juegosolimpicos')
except:
    db = server['juegosolimpicos']
      
twitterStream.filter(locations=[139.604012,35.604659,139.907529,35.784567])  
twitterStream.filter(track=['tokio','juegos olimpicos'])


# In[ ]:




