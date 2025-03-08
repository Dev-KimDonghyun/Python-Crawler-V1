from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 

service = Service(ChromeDriverManager().install()) # Chrome Driver Install

driver = webdriver.Chrome(service = service)

# Code of Importing Modules Code by ChatGPT

import time
import json

targetUrl = 'https://gall.dcinside.com/mgallery/board/lists/?id=vanced&exception_mode=recommend'

driver.get(targetUrl)

postNumber = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[2]/td[1]')).text
postTag = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[3]/td[2]')).text
time.sleep(1)
postTitle = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[3]/td[3]/a[1]')).text
postWriter = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[4]/td[4]/span/em')).text
time.sleep(1.25)
postUploadedTime = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[3]/td[5]')).text
time.sleep(0.6)
postViewed = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[3]/td[6]')).text
postRecommended = (driver.find_element(By.XPATH, '//*[@id="container"]/section[1]/article[2]/div[2]/table/tbody/tr[3]/td[7]')).text

print(postNumber, postTag, postTitle, postWriter, postUploadedTime, postViewed, postRecommended) 
    
driver.quit()