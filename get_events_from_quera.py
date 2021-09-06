from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# myExecutable = FirefoxBinary(r'C:\Users\rayanf\AppData\Local\Programs\Python\Python38\geckodriver.exe')
# driver = webdriver.Firefox (firefox_binary = myExecutable,options=options)

def set_driver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.quera.ir/accounts/login")
    return driver

def login(driver):
    username_input = '//*[@id="auth-form"]/div/div[1]/form/div[1]/div/input'
    password_input = '//*[@id="auth-form"]/div/div[1]/form/div[2]/div/input'
    login_submit = '//*[@id="auth-form"]/div/div[1]/form/button'

    driver.find_element_by_xpath(username_input).send_keys('rayanforsat@gmail.com')
    driver.find_element_by_xpath(password_input).send_keys('projecttest1379')
    driver.find_element_by_xpath(login_submit).click()


if __name__ == '__main__':
    driver = set_driver()
    login(driver)
    time.sleep(2000)
    driver.close()