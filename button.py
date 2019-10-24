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
        driver.implicitly_wait(2)
        
  
            
        try :
            if(flag==0):
                temp ="//button[@class='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is @class button')
        except NoSuchElementException :
            flag =0
            pass 

        
        try:
           
            if(flag==0):
               elem = driver.find_element_by_link_text(array[1])
               flag=1 
               print('this is link text() button')
       
        except NoSuchElementException:
           
           flag =0
           pass
       
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
                temp ="//button[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is text() button')
               
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
        
        try:
            if(flag==0):
               temp = "//*[contains(@value,'"+array[1]+"')]"
               elem = driver.find_element_by_xpath(temp)
               flag=1
               print(temp)
               print('this is @contains value')
        except NoSuchElementException:
            flag=0
            pass   
            

        driver.implicitly_wait(2)
        
        validFlag = 0 
        
            
             try:
                elem.click()
                print("click")
             except ElementNotInteractableException:
                Hover = ActionChains(driver).move_to_element(elem).click().perform()
                
                print("NotInteractable Hover")
             except ElementClickInterceptedException:
                Hover = ActionChains(driver).move_to_element(elem).click().perform()
                print("Intercepted hover")
       
        else:
            print('element not found')
            
        windowhandle = driver.window_handles
        if(len(windowhandle)>1):
            switchwindow = driver.window_handles[-1]
            driver.switch_to_window(switchwindow)
            
        if(flag==1):
             try:
                if(elem.is_enabled()):
                    print('pass')
                    validFlag = 1 
             except:
                print('valid flag didnt work')
                pass
        
        return flag and validFlag    
            
               
            
            
            
            
            
            