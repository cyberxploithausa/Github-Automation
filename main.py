############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: GITHUB AUTOMATION                  #####
##### PROJECT ID: CYBX005                              #####
#####                                                  #####
############################################################


#Importing the modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import cred #my credentials
import time


#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://github.com/login")

username = driver.find_element_by_xpath("//*[@id='login_field']")
username.send_keys(cred.git_user)     #replace cred.git_user with your github username

password = driver.find_element_by_xpath("//*[@id='password']")
password.send_keys(cred.git_pass)   #replace cred.git_pass with your github password

sign_in = driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[12]")
sign_in.click()

time.sleep(3)
New_repo = driver.find_element_by_xpath("/html/body/div[1]/header/div[6]/details/summary/span")
New_repo.click()

time.sleep(3)
Click_repo = driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div:nth-child(6) > details > details-menu > a:nth-child(1)")
Click_repo.click()

time.sleep(3)
repo = driver.find_element_by_xpath("//*[@id='repository_name']")
repo.send_keys("Github-Automation")         #name of repository

time.sleep(2)
create_repo = driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
create_repo.click()
