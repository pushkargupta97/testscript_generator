from get import Get
from button import Button
from textfield import Textfield
from dropdown import Dropdown
import model
import pandas as pd

from selenium import webdriver

from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25537))

driver = webdriver.Chrome()

df = pd.read_excel(r"C:\Users\pusgupta\Desktop\testcases.xlsx", sheet_name=0) # can also index sheet by name or fetch all sheets
mylist = df['Actions'].tolist()

print(mylist)


sample = mylist

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