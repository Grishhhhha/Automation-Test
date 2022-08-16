from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

s = Service("C:\chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

#basicauth
driver.get('https://admin:admin@practice-cybertekschool.herokuapp.com/basic_auth')

#checkbox
driver.get('https://practice-cybertekschool.herokuapp.com')
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/ul/li[7]/a').click()
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/input[2]').click()
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/input[1]').click()
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/input[2]').click()