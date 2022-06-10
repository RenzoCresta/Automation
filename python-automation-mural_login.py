from selenium import webdriver

USERNAME = 'quack.testing@gmail.com'
PASSWORD = 'canyouquack'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://app.mural.co/signin')

user_input = driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')
user_input.send_keys(USERNAME)

sign_in_button = driver.find_element_by_class_name('ui-button-spinner')
sign_in_button.click()
sign_in_button.click()

password_input = driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
password_input.send_keys(PASSWORD)

sign_in_button = driver.find_element_by_class_name('ui-button-spinner')
sign_in_button.click()
sign_in_button.click()
