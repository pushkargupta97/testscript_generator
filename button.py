from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import test


class Button:
        
    def action(self,sentence,driver):
            
        array = sentence.split("'")
        flag = 0
        
        try :
            if(flag==0):
                temp= "//*[@class='"+array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is @class')
                elem = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "'"+temp+"'")))
        except NoSuchElementException :
            flag =0
            pass 
            
        try :
            if(flag==0):
                temp ="//*[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is text')
                elem = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "'"+temp+"'")))
        except NoSuchElementException :
            flag =0
            pass 
        
        try :
            if(flag==0):
                temp ="//button[text()='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is text() button')
                elem = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "'"+temp+"'")))
        except NoSuchElementException :
            flag =0
            pass 
        
        try :
            if(flag==0):
                temp ="//button[@class='"+ array[1]+"']"
                elem = driver.find_element_by_xpath(temp)
                flag=1 
                print('this is @class button')
                elem = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "'"+temp+"'")))
        except NoSuchElementException :
            flag =0
            pass 
        
       

        
        
        elem.click()
               
            
            
            
            
            
            