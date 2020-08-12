# Automation Testing	

Automation Testing means using an automation tool to execute your test case suite. On the contrary, Manual Testing is performed by a human sitting in front of a computer carefully executing the test steps.

The automation software can also enter test data into the system under test , compare expected and actual results and generate detailed test reports.

### GOAL ?

Goal of automation is to reduce number of test cases to be run manually and not eliminate manual testing all together.

### Why Automated Testing ??

1. Manual testing of all work flows,all fields,all negative scenarios is time and cost consuming.
2. It is difficult to test for multilingual sites commonly.
3. Automation doesn't require human intervention you can run automated test unattended(Overnight).
4. Automation increases speed of test execution and test coverage.
5. Manual testing can be boring and hence error prone.

### Which test case to Automate ??

1. Test cases that are executed repeatedly.
2. Test cases that are very tedious or difficult to perform manually.
3. Test cases which are time consuming.
4. High Risk-Business critical test cases.

### Automated Testing Process

1. Test Tool Selection
2. Define Scope of Automation
3. Planning,Design and Development
4. Text Execution
5. Maintenance

####  Automation Tools

- QTP
- Rational Robot
- Selenium 

### Selenium with Python

Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.

Best tools for browser automation. It gives us the ability to browse or use a browser without a human involvement just through code we can act and move around the mouse click on buttons and interact with the websites.

**Downloading Selenium**

```
	pip install selenium
```

**Downloading Drivers**
Selenium requires a driver to interface with chosen browser. Depending upon the browser we need to download the drivers. [Clickme](https://selenium-python.readthedocs.io/installation.html#drivers)

- Extract the zip file in the project folder

This drivers allows selenium to be able to open up our chrome browser and manipulate that browser.

### Basic Functionalities

- Import the Selenium web-driver
- Use the downloaded chrome driver.

```python
from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')
print(chrome_browser)
```

Save the file in same project folder containing chromedriver .

To Run :

- Open your terminal
- Type filename.py

##### Wohoo..! The chrome browser opened. (If any error occurs please update your browser)

######  To Maximize the Chrome Windows

```
from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
print(chrome_browser)
```

#### Save this , Run it  and explore it

```python
from selenium import webdriver
chrome_browser = webdriver.Chrome('./chromedriver')
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
```

