from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#import test


class Dropdown:
    
    def action(self,sentence,driver):
       
        array = sentence.split("'")
        flag = 0
        
        try :
            if(flag==0):
                flag =1 
                temp = "//*[@title = '"+array[3]+"']"
                elem = driver.find_element_by_xpath(temp)
                print('@title')
        except NoSuchElementException:
                flag=0
                pass
         
        
        try :
            if(flag==0):
                flag =1 
                temp = "//*[text()  = '"+array[3]+"']"
                elem = driver.find_element_by_xpath(temp)
                print('text')
        except NoSuchElementException:
                flag=0
                pass
            
        try:
            if(flag==0):
                flag=1
                temp = "//*[text()='"+ array[1]+"']/.."
                elem = driver.find_element_by_xpath(temp)
                print('super')
        except NoSuchElementException:
                flag=0
                pass
            
            
        #print(array[1])
        #print(array[3])
        #temp = "//*[text()='"+ array[3]+"']/.."
        
        if(elem.is_enabled()):
            dropdown = Select(elem)
            dropdown.select_by_visible_text(array[1])
            print("Yo")