import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# initialize the Chrome driver

PATH = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=PATH)

# navigate to YouTube
driver.get('https://www.youtube.com')

# search for a video
search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys('TECH GODAPEX')
time.sleep(2)
search_box.submit()

# wait for search results to load
time.sleep(5)

# click the first video in the search results
videos = driver.find_elements(By.CSS_SELECTOR, '#contents ytd-video-renderer')
first_video = videos[0].find_element(By.CSS_SELECTOR, '#thumbnail')
first_video.click()

# wait for the video to load
time.sleep(5)


# wait for the video to finish
time.sleep(30)

# close the browser window
driver.quit()