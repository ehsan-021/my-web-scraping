from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas

chrome_driver_path = "/usr/bin/chromedriver"  


service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://divar.ir/s/tehran/car?q=%D8%B3%D9%85%D9%86%D8%AF%20lx")
car_name=[]
car_describtion=[]
car_prise=[]
car_location=[]




last_highet=driver.execute_script("return document.body.scrollHeight")
while True:
    car_names=driver.find_elements(By.CLASS_NAME,"kt-post-card__title")
    car_info=driver.find_elements(By.CLASS_NAME,"kt-post-card__description")
    car_loc=driver.find_elements(By.CLASS_NAME,"kt-post-card__bottom-description")
    counter=0
    for i in car_loc:
       car_location.append(i.text)
    for i in car_names:
       car_name.append(i.text)
   

    for i in car_info:     
      if counter%2==0:
              car_describtion.append(i.text)
              counter=counter+1
      else:
              car_prise.append(i.text)
              counter=counter+1 

    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        


          
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_highet:
        print("break")
       
        break
    print(last_highet,new_height)

    last_highet=new_height











               
print(len(car_name),"car name:",car_name)
print(len(car_describtion),"car description:",car_describtion)
print(len(car_prise),"car price:",car_prise)
print(len(car_location),"car location:",car_location)
data=[]
for a,b,c,d in zip(car_name,car_describtion,car_prise,car_location):
       d={
        "name": a,
        "price":c,
        "description":b,
        "location":d
              
       }
       data.append(d)

driver.quit()
df=pandas.DataFrame(data)
file_name="car.xlsx"
df.to_excel(file_name,index=True)



    
