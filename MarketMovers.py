from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from prettytable import PrettyTable
#from ticker import getTickData
import time

######################################################
#used by all commands
options = Options()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.headless = True
options.add_argument('log-level=3')

commands = {"!gainers" : "top-stock-gainers", 
            "!losers" : "top-stock-losers", 
            "!high" : "52-week-high", 
            "!low" : "52-week-low", 
            "!active" : "most-active-stocks", 
            "!commands" : "commands",  
            "!quit" :"quit" }

def printCommands():
    print("Commands are case-sensitive:\n")
    print("!gainers - retrieves the top 10 %% gainers")
    print("!losers - retrieves the top 10 %% losers")
    print("!high - the top 10 stocks that are at their 52 week high")
    print("!low - the top 10 stocks currently at their 52 week low")
    print("!active - the top 10 most active stocks via trade volume")

CHROME_DRIVER_PATH  = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

while(True):
    command = input("Enter your command:")

    if command in commands:
        if command == "!commands":
            printCommands()
            continue
        elif command == "!quit":
            break
        else:
            url = commands.get(command)
    else:
        print("Command does not exist type !commands for list of commands")
        continue
    start = time.time()
    driver.get("https://ca.investing.com/equities/{0}".format(url))
    newUrl = driver.find_elements_by_xpath('//*[@id="stockPageInnerContent"]/table/tbody')
    rows = newUrl[0].find_elements_by_tag_name("tr")

    data = []
    for row in rows[:10]:
        cols = row.find_elements_by_tag_name("td")
        innerList = []
        for col in cols[1:9]:
            innerList.append(col.text)
        
        data.append(innerList)

    x = PrettyTable()
    x.field_names = ["Name", "Last" , "High", "Low", "Change", "Change %", "Volume", "Time"]

    for row in data:
        x.add_row(row)
    print(x)
    end = time.time()
    elapsed = end - start
    print("time elapsed: %.2f seconds" % elapsed)

driver.quit()
