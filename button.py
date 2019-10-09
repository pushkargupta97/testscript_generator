from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#import test


class Button:
        
    def action(self,sentence,driver):
            
        array = sentence.split("'")
        flag = 0
        driver.implicitly_wait(2)
        try :
            if(flag==0):
                temp= "//*[@class='"+array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is @class')
                
        except NoSuchElementException :
            flag =0
            pass 
        
            
        try :
            if(flag==0):
                temp ="//*[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is text')
             
        except NoSuchElementException :
            flag =0
            pass 
        
        try :
            if(flag==0):
                temp ="//button[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is text() button')
               
        except NoSuchElementException :
            flag =0
            pass 
        
        try :
            if(flag==0):
                temp ="//button[@class='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is @class button')
                
        except NoSuchElementException :
            flag =0
            print("no element "+array[1]+" was found")
            return flag
        
        try:
            elem.click()
        except ElementNotInteractableException:
            Hover = ActionChains(driver).move_to_element(elem)
            Hover.click()
               
        return flag  
            
            
            
            
            