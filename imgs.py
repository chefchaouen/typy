from PIL import Image, ImageDraw, ImageFilter
from imageio import imread
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from IPython import embed
import numpy as np
import urllib.request as ur
import random, cv2, lxml, re, io, time

class Product(object):
    def __init__(self,product_web_element):
        self.delimiter = product_web_element.text.index('¥')
        self.name = product_web_element.text[0:self.delimiter]
        self.price = product_web_element.text[self.delimiter:len(product_web_element.text)]
        self.image = Image.fromarray(imread(product_web_element.screenshot_as_png))

driver = webdriver.Safari()
driver.get("https://www.mercari.com/jp/category/1156/?page=2")
links = driver.find_elements_by_tag_name("a")
product_elements = [link for link in links if "¥" in link.text]
products = [Product(product_element) for product_element in product_elements]

embed()