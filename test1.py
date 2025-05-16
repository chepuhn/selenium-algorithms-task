from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    time.sleep(2)  

    assert "Example" in driver.title
    print("Заголовок содержит 'Example' — проверка пройдена.")

    link = driver.find_element(By.CSS_SELECTOR, "a")
    if "More information" in link.text:
        link.click()
        print("Клик по ссылке 'More information...' выполнен.")
    else:

        print("Не найдена нужная ссылка.")

    time.sleep(2)

    # 4. Проверяем, что URL правильный
    assert driver.current_url == "https://www.iana.org/help/example-domains"
    print("Перенаправление успешно — проверка пройдена.")

finally:
    driver.quit()
