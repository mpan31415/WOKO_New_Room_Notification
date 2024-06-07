from selenium import webdriver
import yaml
from os import getcwd
from time import sleep


####################### INTERACTION FUNCTIONS #######################
def login(url, username_key, username, password_key, password, submit_button_key):
    driver.get(url)
    # driver.find_element_by_id(usernameId).send_keys(username)
    # driver.find_element_by_id(passwordId).send_keys(password)
    # driver.find_element_by_id(submit_buttonId).click()
    driver.find_element(by="name", value=username_key).send_keys(username)
    driver.find_element(by="name", value=password_key).send_keys(password)
    driver.find_element(by="name", value=submit_button_key).click()
    
    print("\n Logged in! Sleeping for 3 seconds!\n")
    sleep(3)
    print("\n Finished sleeping!\n")
    
#####################################################################
def search(search_button_key):
    driver.find_element(by="name", value=search_button_key).click()
    
    print("\n Searched! Sleeping for 3 seconds!\n")
    sleep(3)
    print("\n Finished sleeping!\n")
    
#####################################################################


###### load the login credentials ######
credentials_path = getcwd() + "\\website_login\\credentials.yml"
conf = yaml.safe_load(open(credentials_path))
my_username = conf['wohnen_user']['username']
my_password = conf['wohnen_user']['password']


###### Chrome driver and login function ######
driver = webdriver.Chrome()


###### web HTML keys ######
username_field_name = "User"
password_field_name = "Passwort"
submit_button_name = "Loginx"

search_button_name = "Submit"


###### run ######
login("https://wohnen.ethz.ch/index.php?act=searchoffer", username_field_name, my_username, password_field_name, my_password, submit_button_name)

search(search_button_name)