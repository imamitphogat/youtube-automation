import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# initialize the Chrome driver

PATH = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=PATH)

# navigate to YouTube
driver.get('https://www.youtube.com')

# search for a video
search_box = driver.find_element(By.NAME, 'search_query')
search_box.send_keys('New earning app today')
time.sleep(2)
search_box.submit()

# wait for search results to load
time.sleep(5)

title = "🤑2023 BEST SELF EARNING APP | EARN DAILY FREE PAYTM CASH WITHOUT INVESTMENT | NEW EARNING APP TODAY"

# click the first video in the search results
videos = driver.find_elements(By.CSS_SELECTOR, '#contents ytd-video-renderer')

for i in range(4):
    try:
        first_video = driver.find_element(By.XPATH, title )
        first_video.click()
    except:

        ActionChains(driver).send_keys(Keys.END).perform()
    time.sleep(5)

# wait for the video to load
time.sleep(5)


# wait for the video to finish
time.sleep(30)

# close the browser window
driver.quit()