from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains



class Button:
        
    def action(self,sentence,driver):  
            
        array = sentence.split("'")
       
        flag = 0
        driver.implicitly_wait(1)
        
  
            
        try :
            if(flag==0):
                temp ="//button[@class='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is by //button_@class')
        except NoSuchElementException :
            flag =0
            pass 

        
        try:
           
            if(flag==0):
               elem = driver.find_element_by_link_text(array[1])
               flag=1 
               print('this is by link text()')
       
        except NoSuchElementException:
           
           flag =0
           pass
       
        try :
            if(flag==0):
                temp= "//*[@class='"+array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is by @class')
                
        except NoSuchElementException :
            flag =0
            pass 
        try :
            if(flag==0):
                temp ="//button[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is by //button_text()')
               
        except NoSuchElementException :
            flag =0
            pass 
       
        try :
            if(flag==0):
                temp ="//*[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is by text')
                
        except NoSuchElementException :
            flag =0
            pass 
        
        try:
            if(flag==0):
               temp = "//*[contains(@value,'"+array[1]+"')]"
               elem = driver.find_element_by_xpath(temp)
               flag=1
               print(temp)
               print('this is by contains @value')
        except NoSuchElementException:
            flag=0
            pass   
            

        driver.implicitly_wait(1)
        
        validFlag = 0 
        
        if(flag==1):
             try:
                if(elem.is_displayed()):
                    print('pass')
                    validFlag = 1 
             except:
                print('valid flag didnt work')
                pass
        else:
            print('element not found')
        
            
        try:
            elem.click()
            print("click")
        except ElementNotInteractableException:
            Hover = ActionChains(driver).move_to_element(elem).click().perform()
            
            print("NotInteractable Hover")
        except ElementClickInterceptedException:
            Hover = ActionChains(driver).move_to_element(elem).click().perform()
            print("Intercepted hover")
       
        
            
        windowhandle = driver.window_handles
        if(len(windowhandle)>1):
            switchwindow = driver.window_handles[-1]
            driver.switch_to_window(switchwindow)
            
        
        
        return flag and validFlag    
            
               
            
            
            
            
            
            