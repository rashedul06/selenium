import time
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import keys
driver=webdriver.Firefox(executable_path="F:\Selenium\geckodriver")
driver.get("http://192.168.1.105:8060/web/database/selector")
time.sleep(2)
driver.find_element_by_xpath("html/body/div[1]/div/div[2]/a[3]").click()
time.sleep(2)
element=driver.find_element_by_id("login").send_keys("nurnabi@scclbd.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
time.sleep(4)
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
time.sleep(6)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[8]/a/span").click()
time.sleep(6)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[8]/ul[1]/li[3]/a/span").click()
time.sleep(6)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div/button[1]").click()
time.sleep(6)
driver.find_element_by_css_selector("#o_field_input_7").click()
time.sleep(2)
# Customer selection
driver.find_element_by_xpath("/html/body/ul[1]/li[4]/a").click()
time.sleep(2)
driver.find_element_by_css_selector("#o_field_input_8").click()
time.sleep(2)
# Journal account selection
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/table[1]/tbody/tr[2]/td[2]/select/option[5]").click()
time.sleep(2)
driver.find_element_by_css_selector("#o_field_input_9").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ul[2]/li[4]/a").click()
element=driver.find_element_by_css_selector("#o_field_input_10").send_keys("Gulshan")
driver.find_element_by_css_selector("#o_field_input_11").click()
element=driver.find_element_by_css_selector("#o_field_input_11").send_keys(123456)