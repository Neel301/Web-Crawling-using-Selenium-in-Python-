from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

email = "neel34430@gmail.com"
password = "Neel@1234"

driver = webdriver.Chrome()
driver.get("https://www.amazon.de/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.de%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=deflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_css_selector("input[type = \"submit\" i]").click()
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector("input[type = \"submit\" i]").click()

print("logged in successfully")

searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbar.send_keys("home appliances")
searchbar.send_keys(Keys.ENTER)
time.sleep(3)

product = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[1]/div/span[3]/div[2]/div[7]/div/span/div/div/span/div/div[1]/div/div/div/ol/li[2]/div/div/div[2]/h2/a/span").click()
