whsapp_mssge = """
Replace text with bulk message to be sent


"""

from selenium import webdriver
import time
import pandas as pd 
import numpy as np
from pynput.keyboard import Key, Controller

keyboard = Controller()
#excel file extraction
#Insert complete path to the excel file and index of the worksheet, or simply file name in the same folder
df = pd.read_excel("DB_1.xlsx", sheet_name=0)
# insert the name of the column as a string in brackets, therfore make a row with title of the column-heads
list1 = list(df['A']) 
list_number = list(df['B'])
print(list_number)

#browser operation
driver = webdriver.Firefox(executable_path=r'D:\Anaconda\Lib\site-packages\selenium\webdriver\common\geckodriver.exe')
driver.get('https://web.whatsapp.com')
#7 seconds for you to scan the QR code and for the browser to load
time.sleep(7)
for wtsp_float in list_number:
    wtsp_number = int(wtsp_float)
    driver.get('https://web.whatsapp.com/send?phone=91'+str(wtsp_number)+'&text&app_absent=0and')
    time.sleep(7)
    
    
    try :
        #entering message
        #inspect source of text box and accordingly put values in "inp_xpath"
        inp_xpath = '//div[@class="_2_1wd copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
        input_box = driver.find_element_by_xpath(inp_xpath)
        #pressing enter button to send message
        input_box.send_keys(whsapp_mssge)
        time.sleep(3)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
        time.sleep(5)
    except:
        continue
driver.close()
