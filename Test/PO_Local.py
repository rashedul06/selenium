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
element=driver.find_element_by_id("login").send_keys("imran@scclbd.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[3]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr[1]/td[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[12]/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/table[1]/tbody/tr[1]/td[2]/div/div/input[1]").click()
driver.find_element_by_xpath("/html/body/ul[1]/li[7]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[9]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div[1]/div[6]/span/span[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[5]/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/div/footer/button[1]/span").click()