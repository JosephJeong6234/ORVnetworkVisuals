import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#virtual env is python3 -m venv ./
#might be faster just to do source bin/activate

driver = webdriver.Chrome("scraping/bin/chromedriver")
page_url = "https://omniscient-readers-viewpoint.fandom.com/wiki/Category:Characters"
driver.get(page_url)
time.sleep(3)
#might need to do something for the spoiler pop up


rawChars = driver.find_elements(By.CLASS_NAME, 'category-page__member-link')
cleanChars = [c for c in rawChars if ':' not in c.text]
names = []
for i in cleanChars:
    names.append(i.text)

poggersNames = pd.DataFrame(names)
poggersNames.to_csv('names.csv')