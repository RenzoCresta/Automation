from selenium import webdriver

USERNAME = 'cresta.renzo@gmail.com'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://accounts.google.com/signin')

user_input = driver.find_element_by_id('identifierId')
user_input.send_keys(USERNAME)

search_button = driver.find_element_by_id('identifierNext')
search_button.click()
