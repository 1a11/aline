import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
driver = webdriver.Chrome()

while True:
    driver.get("http://vpelle.ru/votes/523753")
    assert "Маргарита" in driver.title
    elem = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div[1]/div[4]/a')
    elem.click()
    elem = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div/div/input[1]')

    elem.send_keys('+'+str(random.getrandbits(9)))

    elem = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div/div/input[2]')

    elem.send_keys(str(random.getrandbits(random.randint(50,55))))

    elem = driver.find_element_by_xpath('//*[@id="install_allow"]')
    elem.click()
