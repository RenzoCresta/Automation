from selenium import webdriver

SEARCH = 'Gibson SG'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.bing.com/?scope=images&nr=1&FORM=NOFORM')

user_input = driver.find_element_by_id('sb_form_q')
user_input.send_keys(SEARCH)

search_button = driver.find_element_by_id('search_icon')
search_button.click()
