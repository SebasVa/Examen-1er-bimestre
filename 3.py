#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://www.elcomercio.com/search?s=juegos+olimpicos'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:




