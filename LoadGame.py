from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

firefox_binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
executable_path = "./geckodriver.exe"
opt = webdriver.FirefoxOptions()
service = Service(executable_path=executable_path)
driver = webdriver.Firefox(firefox_binary=firefox_binary,service=service,options=opt)

driver.get("www.baidu.com")
time.sleep(10)
driver.quit()