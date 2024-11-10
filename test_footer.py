from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Запускаем браузер
driver = webdriver.Chrome()

# Переходим на страницу
url = "https://ya.ru/ai/gpt-4"
driver.get(url)


try: footer = driver.find_element(By.XPATH,"//footer[@class='sc-222969c7-0 dVHqae']")
except NoSuchElementException: 
        print("Не найден футер")
else: 
        print("Найден футер")

try: footer = driver.find_element(By.XPATH,"//p[@class='sc-222969c7-1 eNylzl']")
except NoSuchElementException: 
        print("Начать проект не найден")
else: 
        print("Начать проект найден")



            
#Закрываем браузер
driver.quit()