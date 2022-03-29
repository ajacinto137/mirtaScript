import selenium
from selenium import webdriver
from selenium.webdriver import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://voice.planet.net/pbx/login.php")
search = driver.find_element_by_name("username")
search.send_keys("avelino@planet.net")
search = driver.find_element_by_name("password")
search.send_keys("LssVPdJm")
search.send_keys(Keys.RETURN)
search = driver.find_element_by_name("2facode")
print("Break")
twoFa = input("Please Enter twoFa:    ")
search.send_keys(twoFa)
search.send_keys(Keys.RETURN)

# id
# name
# class


