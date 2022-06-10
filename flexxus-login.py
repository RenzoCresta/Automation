from selenium import webdriver

USERNAME = 'username'
PASSWORD = 'password'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://soporte.flexxus.com.ar/')

user_input = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')
password_input.send_keys(PASSWORD)

sign_in_button = driver.find_element_by_class_name('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/div[3]/input[1]')
sign_in_button.click()
sign_in_button.click()
