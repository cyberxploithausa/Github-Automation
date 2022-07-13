############################################################
#####                   CYBERXPLOIT                    #####
##### PROJECT NAME: GITHUB AUTOMATION                  #####
##### PROJECT ID: CYBX005                              #####
#####                                                  #####
############################################################
import time
# Importing the modules
import os
from selenium import webdriver
import cred  # my credentials


stable_repo = input("Enter the name of the repository: ")

os.environ['PATH'] += r"C:/SeleniumDriver"
#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://github.com/login")

# can say time.sleep(5) but implicitly_wait does the job without completing the full time
# if the browser load faster before the specified wait time.
driver.implicitly_wait(5)

username = driver.find_element_by_xpath("//*[@id='login_field']")
<<<<<<< HEAD
# replace cred.git_user with your github username
username.send_keys(cred.git_user)

password = driver.find_element_by_xpath("//*[@id='password']")
# replace cred.git_pass with your github password
password.send_keys(cred.git_pass)
=======
username.send_keys("Your Username")  #Enter your github username

password = driver.find_element_by_xpath("//*[@id='password']")
password.send_keys("Your password")  #Enter your github password


sign_in = driver.find_element_by_name("commit")
sign_in.click()

time.sleep(3)
New_repo = driver.find_element_by_xpath(
    "/html/body/div[1]/header/div[6]/details/summary/span")
New_repo.click()

time.sleep(3)
Click_repo = driver.find_element_by_css_selector(
    "body > div.position-relative.js-header-wrapper > header > div:nth-child(6) > details > details-menu > a:nth-child(1)")
Click_repo.click()

time.sleep(3)
repo = driver.find_element_by_xpath("//*[@id='repository_name']")
repo.send_keys(stable_repo)  # name of repository

time.sleep(5)
create_repo = driver.find_element_by_xpath(
    "//*[@id='new_repository']/div[4]/button")
create_repo.click()
