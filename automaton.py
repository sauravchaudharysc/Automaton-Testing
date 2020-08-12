from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Automaton Testing')
show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
#We use assert to assert is the statement error free, 
#if error occurs it gives an assertion error or simply run the code and exit if no erroe.
print(output_message.get_attribute('innerHTML'))
assert 'Automaton Testing' in output_message.Text

chrome_browser.quit()