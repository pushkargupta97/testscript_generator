from get import Get
from button import Button
from textfield import Textfield
from dropdown import Dropdown
import model
from selenium import webdriver

#sample= ["open 'www.mfs.com'","click on 'Menu'","click on 'Products & Strategies'", "click on 'Mutual Funds'", "Select 'Massachusetts Investors Trust' from 'Select a Fund' dropdownlist"]
#sample = ["opem 'www.mfs.com'", "click on 'Search'","enter text 'Mutual Fund' in the 'Search' box"]
#sample = ["open 'www.mfs.com'","click on 'left-container'", "select 'Australia' from 'Change your location' dropdown list'"]
sample = ["open 'www.mfs.com'",
          "click on 'Register'",
          "click on 'Investment Professional'",
          "click on 'UNITED STATES'",
          "click on 'Financial Advisor'",
          "click on 'I Agree'",
          "enter 'password' in 'Password'"
          ]



driver = webdriver.Chrome()

for sen in sample:
    
    sample1 = [sen]
    sample1 = vectorizer.transform(sample1).toarray()
    print(classifier.predict(sample1))
    
    if(classifier.predict(sample1) ==0):
        print("button")
        button = Button()
        button.action(str(sen),driver) 
        
    if(classifier.predict(sample1) ==3):
        print("dropdown")
        dropdown = Dropdown()
        dropdown.action(str(sen),driver)
        
    if(classifier.predict(sample1) ==1):
        print("get")
        get = Get()
        get.browse(str(sen),driver)
        
    if(classifier.predict(sample1) ==2):
        
        print("textfield")
        textfield = Textfield()
        textfield.action(str(sen),driver)