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
time.sleep(3)

chrome_driver = '/Users/jeongseogmin/Desktop/NEXT/NEXT_HW/Session5/chromedriver'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)
time.sleep(2)

# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com")
time.sleep(2)

# 랭킹 1-20위
rankbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a/strong')
rankbtn.click()
time.sleep(2)

file = open('naver1.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["영화명", "개요", "감독", "평점"])

for i in range(2, 8):
    time.sleep(1)
    moviename = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
    time.sleep(1)
    movie_name = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a')
    movie_name.click()
    time.sleep(1)
    outline = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]').text
    time.sleep(1)
    director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
    time.sleep(1)
    grade = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text
    time.sleep(1)

    print(moviename, outline, director, grade)
    rankbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a/strong')
    rankbtn.click()
    writer.writerow([moviename, outline, director, grade])
file.close()
