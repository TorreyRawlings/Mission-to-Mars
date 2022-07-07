#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Import Splinter and BeautifulSoup
from selenium import webdriver
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1) 
#we're searching for elements with a specific combination of tag (div) and attribute (list_text). As an example, ul.item_list would be found in HTML as <ul class="item_list">.
#Secondly, we're also telling our browser to wait one second before searching for components. The optional delay is useful because sometimes dynamic pages take a little while to load, especially if they are image-heavy.


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[9]:


#find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[11]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
#An img tag is nested within this HTML, so we've included it.
#.get('src') pulls the link to the image.
img_url_rel


# In[12]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[13]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[14]:


df.to_html()


# In[15]:





# # Hemisphere Images & Titles

# In[22]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[25]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = {}

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for i in range(4):
    html = browser.html
    parser_soup = soup(html, "html.parser")
    
    title = parser_soup.find_all("h3")[i].get_text()
    browser.find_by_tag('h3')[i].click()
    
    html = browser.html
    parser_soup = soup(html, "html.parser")
    
    img_url = parser_soup.find("img", class_="wide-image")["src"]
    
    hemisphere_image_urls.append({
        "title": title,
        "img_url": "https://marshemispheres.com/" + img_url
    })
    browser.back()
    hemisphere_image_urls

browser.quit()


# In[26]:


hemisphere_image_urls


# In[ ]:




