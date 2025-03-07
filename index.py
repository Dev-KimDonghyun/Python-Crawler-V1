from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 

service = Service(ChromeDriverManager().install()) # Chrome Driver Install

driver = webdriver.Chrome(service = service)

# Code of Importing Modules Code by ChatGPT

import time

userInputSearchValue = input('検索ワードを入力してください：')
userInputRegionValue = input('検索エリアを日本語で正しく入力してください：')

targetUrl = 'https://jp.indeed.com/'

driver.get(targetUrl)

def mainFunction ():
    print('Loading...')
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="text-input-what"]').click()
    time.sleep(5) 
    driver.find_element(By.XPATH, '//*[@id="text-input-what"]').send_keys(userInputSearchValue)
    time.sleep(5) 
    driver.find_element(By.XPATH, '//*[@id="text-input-where"]').click()
    time.sleep(5) 
    driver.find_element(By.XPATH, '//*[@id="text-input-where"]').send_keys(userInputRegionValue)
    time.sleep(5) 
    driver.find_element(By.XPATH, '//*[@id="jobsearch"]/div/div[2]/button').click()
    time.sleep(1)
    element1 = driver.find_element(By.XPATH, '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/h2/span/text()')
    print(element1.text)
    driver.quit()


if userInputSearchValue == '' or userInputRegionValue == '':
    print('値を入力してください')
else:
    mainFunction()