import os

from selenium import webdriver


os.environ['PATH'] += r";C:/SeleniumDerivers"
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")


driver.implicitly_wait(8)
searchElement = driver.find_element_by_name('q')
searchElement.send_keys("www..com ")
searchElement.click()
searchElement2 = driver.find_element_by_class_name('wM6W7d')
searchElement2.click()
#driver.close()

#<div class="eIPGRd"><div class="sbic sb43"></div><div class="pcTkSc" role="option">
# <div class="wM6W7d"><span>www<b>.</b>facebook<b>.</b>com<b> patrika brainpower</b>
# </span></div><div class="ClJ9Yb" style="display: none;"><span></span></div></div>
# <div class="AQZ9Vd" style="display: none;"><div class="sbai">Delete</div></div></div>
