import time
from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import keys
driver=webdriver.Firefox(executable_path="F:\Selenium\geckodriver")
driver.get("http://192.168.1.105:8060/web/database/selector")
time.sleep(2)
driver.find_element_by_xpath("html/body/div[1]/div/div[2]/a[3]").click()
element=driver.find_element_by_id("login").send_keys("abdulhye.niloy@gmail.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[3]/a/span").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div/button[1]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/input").click()
time.sleep(2)
element=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/input")
#drp.select_by_visible_text('[10.01.013] Carbolic Acid (Admin)')
time.sleep(2)
driver.find_element_by_xpath("/html/body/ul[10]/li[1]/a").click()
element=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[4]/div/div[1]/div[1]/div[2]/div[1]/input[2]").send_keys(100)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[2]/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[5]/span").click()
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[3]/a").click()
time.sleep(2)
element=driver.find_element_by_id("login").send_keys("utpal_chem@scclbd.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[3]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/ul[1]/li[2]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr[1]/td[2]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[6]/span").click()
time.sleep(2)
element=driver.find_element_by_id("o_field_input_34").click()
element=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/table[1]/tbody/tr/td[2]/select/option[3]").click()
#drp=select(element)
time.sleep(2)
#drp.select_by_index('1')
element=driver.find_element_by_id("o_field_input_35").click()
element=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/table[3]/tbody/tr/td[2]/select/option[3]").click()
time.sleep(2)
element=driver.find_element_by_id("o_field_input_36").click()
element=driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/table[4]/tbody/tr/td[2]/select/option[4]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/footer/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span[1]").click()
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[3]/a").click()
time.sleep(2)
element=driver.find_element_by_id("login").send_keys("das.bk.sccl@gmail.com")
element=driver.find_element_by_id("password").send_keys("@dminsccl")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/main/div/form/div[4]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[1]/li[4]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/ul[1]/li[2]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div/table/tbody/tr[1]/td[2]").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/header/button[13]/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[3]/div/footer/button[1]/span").click()
# PR approved by B.k Das
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/a/span[1]").click()
driver.find_element_by_xpath("/html/body/nav/div[2]/ul[2]/li/ul/li[3]/a").click()
time.sleep(2)
