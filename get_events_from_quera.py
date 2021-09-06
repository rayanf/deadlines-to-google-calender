from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# myExecutable = FirefoxBinary(r'C:\Users\rayanf\AppData\Local\Programs\Python\Python38\geckodriver.exe')
# driver = webdriver.Firefox (firefox_binary = myExecutable,options=options)

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()