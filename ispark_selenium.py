import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://online.ispark.istanbul/")
driver.save_screenshot("screenshot.png")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2) #sayfanın aşağısına inme 

txtPlate=driver.find_element("name",'txtPlate')
tbCode=driver.find_element("name",'tbCode')

giris_yap= driver.find_element("xpath", '//*[@id="trQuery"]/section/div[2]/div/div[4]')

txtPlate.send_keys("34 DNS 40")
tbCode.send_keys("7psu")
giris_yap.click()

