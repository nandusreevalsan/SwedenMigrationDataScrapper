# A python script to find migration data.

import time
from selenium import webdriver

def MigrationScrap(ControlNumber):
    browser = webdriver.Chrome('/Users/Nandu/Downloads/chromedriver 2')
    browser.get("https://www.migrationsverket.se/English/Contact-us/My-page-and-Check-your-application/Check-your-application-without-login.html")
    #time.sleep(4)
    ControlNumberSelect = browser.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/form/div/div[1]/div/div[2]/div[2]/input')
    ControlNumberSelect.click()
    #time.sleep(1)
    ControlNumberTab = browser.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/form/div/div[3]/div/input')
    #ControlNumberTab.click()
    ControlNumberTab.send_keys(str(ControlNumber))
    #time.sleep(1)
    browser.find_element_by_xpath('//*[@id="svid12_2e150b9f1743f689cbff0"]/div[2]/div[1]/form/div/div[4]/input').click()
    time.sleep(1)
    try:
        ControlNumberSelect.click()
        print("",ControlNumber,"Not valid")
    except:
        TextElement = browser.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/h2/a/span[1]')
        YearIndex = TextElement.text.find('2')

        DecisionElement = browser.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div[2]/div/div/div/div/div[1]/ul')
        DecisionIndex = DecisionElement.text.find("has made")
        print("",ControlNumber,"Valid",":",TextElement.text[YearIndex:],":",DecisionElement.text[DecisionIndex:])
        
    browser.quit()

if (__name__ == "__main__"):
    num = 58191290
    for i in range(9000):
        MigrationScrap(num+i)
    
