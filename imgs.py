from PIL import Image, ImageDraw, ImageFilter
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from IPython import embed
import numpy as np
import urllib.request as ur
import cv2, lxml, re, io, time

driver = webdriver.Safari()
driver.get("https://www.mercari.com/jp/")
embed()