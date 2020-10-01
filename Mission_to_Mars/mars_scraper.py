from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd

def browser_in():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scraper():
    browser=browser_in()
    nasa_url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    jpl_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    twitter_url='https://twitter.com/marswxreport?lang=en'
    table_url='https://space-facts.com/mars/'
    response=requests.get(nasa_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    div1=soup.find_all('div',class_='grid_layout')
    a=div1[1].find_all('a')
    title=a[1].text.replace('\n','')
    paragraph=div1[1].find('div',class_='rollover_description_inner').text.replace('\n','')
    browser.visit(jpl_url)
    html1=browser.html
    jpl_soup=BeautifulSoup(html1,'html.parser')
    img=jpl_soup.find_all('a',class_='button fancybox')
    full_img_url='www.jpl.nasa.gov/'+img[0].get('data-fancybox-href')
    hemi_urls=[
    {'title':'Cerberus','url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
    {'title':'Schiaparelli','url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
    {'title':'Syrtis','url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
    {'title':'Valles Marineris','url':'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}
    ]
    scraped_dict={
        'hemi_urls': hemi_urls,
        'new_title': title,
        'paragraph': paragraph,
        'ft_img': full_img_url
    }
    return scraped_dict