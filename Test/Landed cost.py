import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.keys import keys
driver=webdriver.Firefox(executable_path="F:\Selenium\geckodriver")
driver.get("http://192.168.1.105:8060/web/database/selector")
time.sleep(5)
driver.find_element_by_xpath("html/body/div[1]/div/div[2]/a[3]").click()
element=driver.find_element_by_id("login").send_keys("shohrab@scclbd.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[5]/a/span").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/ul[4]/li[1]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[1]/span").click()
time.sleep(2)
element=driver.find_element_by_id("o_field_input_25")
time.sleep(2)
drp=select(element)
drp.select_by_index('5')
element=driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]/div/div/div/input").click()
time.sleep(2)
driver.close()