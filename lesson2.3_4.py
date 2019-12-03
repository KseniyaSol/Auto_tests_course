from selenium import webdriver
import time
import math

try: 
    link ="http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")    
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = math.log(abs(12*math.sin(int(x))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(y))

    button = browser.find_element_by_css_selector("button.btn")    
    button.click()

finally:
    time.sleep(5)
    browser.quit()
