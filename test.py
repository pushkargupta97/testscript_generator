from get import Get
from button import Button
from textfield import Textfield
from dropdown import Dropdown
import model

from selenium import webdriver

from py4j.java_gateway import JavaGateway, GatewayParameters


sample1= ["open 'www.mfs.com'",
         "click on 'Menu'",
         "click on 'Products & Strategies'", 
         "click on 'Mutual Funds'", 
         "Select 'Massachusetts Investors Trust' from 'Select a Fund' dropdownlist"]

sample2 = ["opem 'www.mfs.com'", 
          "click on 'Search'",
          "enter text 'Mutual Fund' in the 'Search' box"]


sample3 = ["open 'www.mfs.com'",
          "click on 'left-container'", 
          "select 'Australia' from 'Change your location' dropdown list'"]

sample4 = ["open 'www.mfs.com'",
          "click on 'Register'",
          "click on 'INVESTMENT PROFESSIONAL'",
          "click on 'UNITED STATES'",
          "click on 'Financial Advisor'",
          "click on 'I AGREE'",
          "enter 'password' in 'password'",
          "ENTER 'BAT123' IN 'userName'",
          ]
  
sample5 = ["click on 'Investment Professional'"
         "select 'UNITED STATES' from 'Change your location' dropdown",
         "select 'INDIVIDUAL INVESTOR' from 'Select your role'"
         ]



gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25537))
driver = webdriver.Chrome()

sample = sample4 

for sen in sample:
    
    
    
    testcase = [sen]
    testcase = vectorizer.transform(testcase).toarray()
   
    print(classifier.predict(testcase))
    
    if(classifier.predict(testcase) ==0):
        print("button")
        button = Button()
        status_flag  = button.action(str(sen),driver) 
        if(status_flag == 1 ):
            gateway.entry_point.reportPass('testcase :'+sen+' is succesful')
        else:
            gateway.entry_point.reportFail('testcase :'+sen+' is fail')
            break
            
        
    if(classifier.predict(testcase) ==3):
        print("dropdown")
        dropdown = Dropdown()
        status_flag = dropdown.action(str(sen),driver)
        if(status_flag == 1 ):
            gateway.entry_point.reportPass('testcase :'+sen+' is succesful')
        else:
            gateway.entry_point.reportFail('testcase :'+sen+' is fail')
            break
        
    if(classifier.predict(testcase) ==1):
        print("get")
        get = Get()
        status_flag = get.browse(str(sen),driver)
        if(status_flag == 1 ):
            gateway.entry_point.reportPass('testcase :'+sen+' is succesful')
        else:
            gateway.entry_point.reportFail('testcase :'+sen+' is fail')
            break
        
    if(classifier.predict(testcase) ==2):
        
        print("textfield")
        textfield = Textfield()
        status_flag = textfield.action(str(sen),driver)
        if(status_flag == 1 ):
            gateway.entry_point.reportPass('testcase :'+sen+' is succesful')
        else:
            gateway.entry_point.reportFail('testcase :'+sen+' is fail')
            break
        
gateway.entry_point.endAll()
print('program has ended')