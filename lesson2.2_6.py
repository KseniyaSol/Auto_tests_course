from selenium import webdriver
import math
import time

try: 
    link ="http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = int(x_element.text)
    y = math.log(abs(12*math.sin(x)))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))
    check_b = browser.find_element_by_id("robotCheckbox")
    check_b.click()
    radio = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
