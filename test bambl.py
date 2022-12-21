import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

s =Service('C:/Test/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Запуск сайта
driver.get("https://qa.neapro.site/login/")

#Логин
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(1) input").click()
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(1) input").send_keys("photo-deti@mail.ru")
driver.find_element(By.CSS_SELECTOR,".fieldset:nth-child(2) input").send_keys("qqqqqqqq")
driver.find_element(By.CSS_SELECTOR,".btn").click()
time.sleep(3)

#выбор паспорта
driver.find_element(By.CSS_SELECTOR, ".form:nth-child(2) .document-tile:nth-child(1) > .document-name").click()

#заполнение простых текстовых форм
driver.find_element(By.ID, "surname").clear()
driver.find_element(By.ID, "surname").send_keys("Мустафьев")
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Мустафа")
driver.find_element(By.ID, "patronymic").clear()
driver.find_element(By.ID, "patronymic").send_keys("Джабраилович")
driver.find_element(By.ID, "issued").clear()
driver.find_element(By.ID, "issued").send_keys("ТП ОУФМС РФ")

#заполнение числовых масок
driver.find_element(By.ID, "passportNumber").clear()
driver.find_element(By.ID, "passportNumber").click()
driver.find_element(By.ID, "passportNumber").send_keys("222222")
driver.find_element(By.ID, "passportSeries").clear()
driver.find_element(By.ID, "passportSeries").click()
driver.find_element(By.ID, "passportSeries").send_keys("1111")
driver.find_element(By.ID, "code").clear()
driver.find_element(By.ID, "code").click()
driver.find_element(By.ID, "code").send_keys("333333")
driver.find_element(By.ID, "cardId").clear()
driver.find_element(By.ID, "cardId").click()
driver.find_element(By.ID, "cardId").send_keys("44444444444")

#заполнение адреса
driver.find_element(By.CSS_SELECTOR, " .vue-dadata__input").click()
driver.find_element(By.CSS_SELECTOR, " .vue-dadata__input").send_keys(Keys.CONTROL+"a")
driver.find_element(By.CSS_SELECTOR, " .vue-dadata__input").send_keys(Keys.DELETE)
driver.find_element(By.CSS_SELECTOR, " .vue-dadata__input").send_keys("г Москва")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, " .vue-dadata__suddestions").click()
