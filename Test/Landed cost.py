import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.keys import keys
driver=webdriver.Firefox(executable_path="F:\Selenium\geckodriver")
driver.get("http://192.168.1.105:8060/web/database/selector")
time.sleep(2)
driver.find_element_by_xpath("html/body/div[1]/div/div[2]/a[3]").click()
element=driver.find_element_by_id("login").send_keys("shohrab@scclbd.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[5]/a/span").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[5]/ul[4]/li[1]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[1]/span").click()
time.sleep(2)
# driver.find_element_by_css_selector("#o_field_input_72/25/25").click()
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]/div/div/input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ul[2]/li[6]/a").click()
#driver.find_element_by_css_selector("/html/body/ul[2]/li[6]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]/div/div/div/input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ul[5]/li/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div/footer/button[1]/span").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[2]/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]/button/span").click()
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/table[1]/tbody/tr[1]/td[2]/div/div/input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ul[1]/li[7]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/table[1]/tbody/tr[2]/td[2]/div/div/input[1]").click()
driver.find_element_by_xpath("/html/body/ul[2]/li[1]/a").click()
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/table[1]/tbody/tr[3]/td[2]/div/div/input[1]").click()
driver.find_element_by_xpath("/html/body/ul[3]/li[1]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/table[2]/tbody/tr/td[2]/div/div/input[1]").click()
driver.find_element_by_xpath("/html/body/ul[4]/li[1]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/footer/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[2]/span").click()
#Update cost
#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[4]/span").click()
time.sleep(2)
#driver.close()