#!/usr/bin/python
from selenium import webdriver
from random import randint
import time
import os
 
f = open("./links.txt")
startAddress = f.readlines()
 
while True :
   if os.path.exists('/usr/lib/chromium-browser/chromedriver'):
        driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')
   else:
        number=randint(0,2)
        if number == 0:
           driver = webdriver.Chrome(executable_path='./chromedriver')
        elif number == 1:
           driver = webdriver.Firefox(executable_path='./geckodriver')
        else:
           driver = webdriver.Ie(executable_path='./IEDriverServer.exe')
       
   try:
        ranAddress = randint(0, len(startAddress)-1)
        address = startAddress[ranAddress]
        driver.get(address)
        try:
           for x in range(0, 5):
              links = driver.find_elements_by_tag_name("a")
              if len(links) > 1:
                 lnum = randint(0, len(links)-1)
                 browseTo=(links[lnum].get_attribute('href'))
                 time.sleep(1)
                 if "http" not in browseTo:
                    driver.get(address)
                 else:
                    driver.get(browseTo)
        except Exception:
           pass
   except Exception:
     pass
   try:
     driver.close()
   except Exception:
     pass
   os.system("killbrowsers.bat")
