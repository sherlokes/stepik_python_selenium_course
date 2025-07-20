from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math 
import time

def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
        
browser = webdriver.Chrome()

browser.get("https://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 9).until(
EC.text_to_be_present_in_element((By.ID, "price"), "$100"))   
button = browser.find_element(By.ID, "book")
button.click()
        
x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
x = x_element.text
y = calc(x)
answer_element = browser.find_element(By.CSS_SELECTOR, '#answer')
answer_element.clear()       
answer_element.send_keys(y)  

button = browser.find_element(By.ID, "solve")
button.click()
    
time.sleep(30)
browser.quit()