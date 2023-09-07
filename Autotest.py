from importlib.machinery import all_suffixes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Установка драйвера
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')

#Ввод значении в поля
firstname = 'Alex'
lastname = 'Volchkov'
postcode = '7777'
goldname= firstname + " " + lastname

#Нажатие на кнопку Bank Manager Login 
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Bank Manager Login']").click()

time.sleep(1)
#Нажатие на кнопку Add Customer
driver.find_element(By.CSS_SELECTOR, "[ng-class='btnClass1']").click()
#driver.find_element(By.XPATH, "//button[@ng-class='btnClass1']").click()
time.sleep(1)

#Ввод значений в поля 
driver.find_element(By.XPATH, "//input[@ng-model='fName']").send_keys(firstname)
time.sleep(1)
driver.find_element(By.XPATH, "//input[@ng-model='lName']").send_keys(lastname)
time.sleep(1)
driver.find_element(By.XPATH, "//input[@ng-model='postCd']").send_keys(postcode)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "[class='btn btn-default']").click() 
time.sleep(1)

#Подтверждение модального окна
driver.switch_to.alert
driver.switch_to.alert.accept()
time.sleep(1)

#Вторая вкладка Open Account
driver.find_element(By.CSS_SELECTOR, "[ng-click='openAccount()']").click()
time.sleep(5)
#Customer
driver.find_element(By.XPATH, "//select[@ng-model='custId']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[text()='%s']" %goldname).click()
time.sleep(3)
driver.find_element(By.XPATH, "//select[@ng-model='custId']").click()
time.sleep(3)
#Currency
driver.find_element(By.XPATH, "//select[@ng-model='currency']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='Dollar']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//select[@ng-model='currency']").click()
time.sleep(1)

#Нажатие на кнопку процесс 
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
time.sleep(1)
driver.switch_to.alert
driver.switch_to.alert.accept()
time.sleep(1)

#Последняя вкладка Customers
driver.find_element(By.CSS_SELECTOR, "[ng-click='showCust()']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@ng-model='searchCustomer']").send_keys(firstname)
time.sleep(10)
