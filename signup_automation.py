from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://authorized-partner.vercel.app/register")

time.sleep(2)

checkbox = driver.find_element(By.CSS_SELECTOR, "#remember")

checkbox.click()

continue_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]")

continue_button.click()

time.sleep(4)