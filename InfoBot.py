from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

import time

######################################################
#used by all commands
options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
#options.headless = True
options.add_argument('log-level=3')
CHROME_DRIVER_PATH  = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
######################################################

#ticker = input("Enter Ticker:")

#driver.get("https://investing.com/search/?q={0}".format(ticker))
driver.get("https://investing.com/search/?q=msft")

newURL = driver.find_elements_by_xpath('//*[@id="fullColumn"]/div/div[2]/div[2]/div[1]/a[1]') #error checking for if none found
driver.get(newURL[0].get_attribute('href'))

element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'chartWrap')))
element.screenshot('gallery.png')

#x = PrettyTable()

time.sleep(15)
driver.quit()