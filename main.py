import selenium
from selenium import webdriver
from selenium.webdriver import Keys


# Set Up

PATH = "C:\Program Files (x86)\chromedriver.exe"
#Must download chrome driver and add it to the above location or copy its location to the path variable

#Mirta Link
website = "https://voice.planet.net/pbx/login.php"

#Credentials
username = input("Please Enter Username--> ")
password = input("Please Enter Password--> ")
twoFa = input("Please Enter twoFa ---> ")

# username = "avelino@planet.net"
# password = "LssVPdJm"


driver = webdriver.Chrome(PATH)
driver.get(website)
search = driver.find_element_by_name("username")
search.send_keys(username)
search = driver.find_element_by_name("password")
search.send_keys(password)
search.send_keys(Keys.RETURN)
search = driver.find_element_by_name("2facode")
print("Break")

search.send_keys(twoFa)
search.send_keys(Keys.RETURN)

# id
# name
# class


