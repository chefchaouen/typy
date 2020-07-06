from PIL import Image, ImageFilter
from selenium import webdriver
from bs4 import BeautifulSoup
from IPython import embed
import numpy as np
import urllib.request as ur
import cv2, lxml, re

img_links = []

#get pictures of pets
driver = webdriver.Safari()
driver.get("https://pets-kojima.com/small_list/?topics_group_id=4&group=&shop%5B%5D=&freeword=&price_bottom=&price_upper=&order_type=2")
driver.maximize_window()
soup = BeautifulSoup(driver.page_source, 'lxml')
img_links += [tag['src'] for tag in soup.find_all('img', src=re.compile("http"))]
imgs = [Image.open(ur.urlopen(img_link)) for img_link in img_links]
edge_imgs = [np.asarray(img.filter(ImageFilter.FIND_EDGES)) for img in imgs]
embed()
Image.fromarray(cv2.vconcat(edge_imgs)).show()