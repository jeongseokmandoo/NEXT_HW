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
time.sleep(2)

# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com")
time.sleep(2)

# 좋아하는 영화 검색 -> 제목, 감독, 스크롤 내려서 평점 + 리뷰 개수
xbtn = driver.find_element(By.XPATH, '//*[@id="noti_popup"]/div[1]/button')
xbtn.click()
time.sleep(2)

searchbox = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
searchbox.send_keys("coda")
time.sleep(3)

moviefig = driver.find_element(By.XPATH, '//*[@id="jAutoMV"]/ul/li[1]/a/p/img')
moviefig.click()
time.sleep(2)

file = open('naver3.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["moviename", "director", "grade", "review"])
time.sleep(1)

moviename = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
grade = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
review = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text

print(moviename, director, grade, review)
writer.writerow([moviename, director, grade, review])
file.close()