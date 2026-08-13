from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas

# مسیر chromedriver را مشخص کنید
chrome_driver_path = "/usr/bin/chromedriver"  # مسیری که در مرحله‌ی قبل پیدا کردید




# ایجاد سرویس و مرورگر
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://divar.ir/s/tehran/car/pride/sedan/petrol?q=%D9%85%D8%A7%D8%B4%DB%8C%D9%86&sort=sort_date")

last_highet=driver.execute_script("return document.body.scrollHeight")
while True:
   
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
            button = driver.find_element(By.CLASS_NAME,"kt-button kt-button--primary kt-nav-button nav-bar__submit-btn-fbb11")
            button.click()
            time.sleep(2)
            print("button clicked")
    except:
            pass
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_highet:
        print("break")
        break
    print(last_highet==new_height)

    last_highet=new_height





car_name=[]
car_describtion=[]
car_prise=[]
car_location=[]
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





               
print(car_name)
print(car_describtion)
print(car_prise)
print(car_location)
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



    
