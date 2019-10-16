from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Textfield:
    
    def action(self,sentence,driver):
       
        array = sentence.split("'")
        flag = 0 ;
        try :
            if(flag == 0):
                flag = 1
                temp = "//input[contains(@text,'"+array[3]+"')]"
                inputbox = driver.find_element_by_xpath(temp)
                print('this is contains text')
        except NoSuchElementException :
            flag =0
            pass
        
        try :
            if(flag == 0):
                flag = 1
                temp = "//input[@title = '"+array[3]+"']"
                inputbox = driver.find_element_by_xpath(temp)
                print('this is title')
        except NoSuchElementException :
            flag =0
            pass
        
        try :
            if(flag == 0):
                flag = 1
                temp = "//input[contains(@name,'"+array[3]+"')]"
                inputbox = driver.find_element_by_xpath(temp)
                print('this is contains name')
        except NoSuchElementException :
            flag =0
            pass
        
        validFlag = 0
        
        if(flag == 1):
            inputbox.clear()
            inputbox.send_keys(array[1])
            
        try:
            if(inputbox.is_displayed()):
                print("Yo")
                validFlag = 1
        except:
            print("Neh")
            
        return flag and validFlag
        #inputbox.send_keys(Keys.ENTER)
        