# A python script to find migration data.

import time
import pickle
import numpy as np
from selenium import webdriver

def MigrationScrap(ControlNumber,DataDecided,DataSubmitted,ValidNumber,ValidCount,DecidedNumber,DecidedCount):
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
        DecisionMadeIndex = DecisionElement.text.find("has made a")
        if DecisionMadeIndex != -1:
            try:
                DataDecided[TextElement.text[YearIndex:]]+=1
                
            except:
                DataDecided[TextElement.text[YearIndex:]] = 1
            #pickle.dump(Data,DataFile)
            DecidedCount += 1
            DecidedNumber.append(ControlNumber)
            np.save("DecidedNumbers",DecidedNumber)
            
            DataFile = open("MigrationDataDecided.txt","wt")
            DataFile.write(str(DataDecided))
            DataFile.close()
        else:
            try:
                DataSubmitted[TextElement.text[YearIndex:]]+=1
                
            except:
                DataSubmitted[TextElement.text[YearIndex:]] = 1
            #pickle.dump(Data,DataFile)
            ValidCount +=1
            ValidNumber.append(ControlNumber)
            np.save("ValidNumbers",ValidNumber)
            
            DataFile = open("MigrationDataSubmitted.txt","wt")
            DataFile.write(str(DataSubmitted))
            DataFile.close()
        
        print("",ControlNumber,"Valid",":",TextElement.text[YearIndex:],":",DecisionElement.text[DecisionIndex:])
    browser.quit()
    return [ValidCount, DecidedCount]
    

if (__name__ == "__main__"):
    num = 0
    DataDecided = {}
    DataSubmitted = {}
    ValidNumber = []
    ValidCount = 0
    
    DecidedNumber = []
    DecidedCount = 0

    ValidNumbers = np.load('ValidNumbers.npy')
    #Baseline 435 106 541
    for i in ValidNumbers:
        try:
            Total = ValidCount + DecidedCount
            print("Valid Numbers: ",ValidCount," Decided Numbers: ",DecidedCount," Total Applications: ",Total )
            [ValidCount,DecidedCount] = MigrationScrap(num+i,DataDecided,DataSubmitted,ValidNumber,ValidCount,DecidedNumber,DecidedCount)
        except:
            try:
                print("1st")
                [ValidCount,DecidedCount] = MigrationScrap(num+i,DataDecided,DataSubmitted,ValidNumber,ValidCount,DecidedNumber,DecidedCount)
                
            except:
                try:
                    print("2nd")
                    [ValidCount,DecidedCount] = MigrationScrap(num+i,DataDecided,DataSubmitted,DataDecided,ValidNumber,ValidCount,DecidedNumber,DecidedCount)
                    
                except:
                    try:
                        print("3rd")
                        [ValidCount,DecidedCount] = MigrationScrap(num+i,DataDecided,DataSubmitted,ValidNumber,ValidCount,DecidedNumber,DecidedCount)
                        
                    except:
                        try:
                            print("4th")
                            [ValidCount,DecidedCount] = MigrationScrap(num+i,DataDecided,DataSubmitted,ValidNumber,ValidCount,DecidedNumber,DecidedCount)
                            
                        except:
                            print("5th")
                            [ValidCount,DecidedCount] = MigrationScrap(num+i,DataDecided,DataSubmitted,ValidNumber,ValidCount,DecidedNumber,DecidedCount)
                            
                            
                    
    
