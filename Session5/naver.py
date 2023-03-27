import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = '/Users/jeongseogmin/Desktop/NEXT/NEXT_HW/Session5/chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://movie.naver.com/")

# 멜론 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, '')
chartbtn.click()

