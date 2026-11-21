from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import os
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
import random

driver = webdriver.Chrome()

run_id = int(time.time())
email_front = os.getenv("GMAIL_USER").split("@")[0]


prefix = random.choice(["984", "985", "986", "980", "981", "982", "974", "975"])
Phone = prefix + str(random.randint(1000000, 9999999))


GMAIL_USER = os.getenv("GMAIL_USER")
API_KEY = "Keep your amilosaur api key here"

SERVER_ID = "keep your mailosaur server id here"
Email = f"{email_front}{run_id}@{SERVER_ID}.mailosaur.net"

client = MailosaurClient(API_KEY)

# url to terms and condition page
URL = os.getenv("URL")
driver.get(URL)

time.sleep(2)

# terms and condition page
checkbox = driver.find_element(By.CSS_SELECTOR, "#remember").click()

continue_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]").click()

time.sleep(4)

# set up you account page
first_name = driver.find_element(By.NAME, "firstName").send_keys("Ram")

last_name = driver.find_element(By.NAME, "lastName").send_keys("Shrestha")

driver.find_element(By.NAME, "email").send_keys(Email)

phone_no = driver.find_element(By.NAME, "phoneNumber").send_keys(Phone)

password = driver.find_element(By.NAME, "password").send_keys("Asdfghjk!23")

conform_password = driver.find_element(By.NAME, "confirmPassword").send_keys("Asdfghjk!23")


next = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)


def get_code():
    criteria = SearchCriteria()
    criteria.sent_to = Email

    # waits up to 30 seconds for the email to arrive
    message = client.messages.get(SERVER_ID, criteria, timeout=30000)

    # mailosaur finds the code in the email for us
    return message.text.codes[0].value

code = get_code()

code_boxes = driver.find_elements(By.CSS_SELECTOR, "form input")


if len(code_boxes) == 1:
    code_boxes[0].click()
    code_boxes[0].send_keys(code)
else:
    for i in range(len(code)):
        code_boxes[i].send_keys(code[i])

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(4)


# Agency Detail
Agency_name = driver.find_element(By.NAME, "agency_name").send_keys("ABC Limited")

Role_agency = driver.find_element(By.NAME, "role_in_agency").send_keys("CEO")

Agency_email = driver.find_element(By.NAME, "agency_email").send_keys("abc@gmail.com")

agency_website = driver.find_element(By.NAME, "agency_website").send_keys("www.abc.om")

agency_address = driver.find_element(By.NAME, "agency_address").send_keys("Kathmandu")

driver.find_element(By.CSS_SELECTOR, ".font-satoshi-regular.text-translucent").click()
driver.find_element(By.XPATH, "//*[text()='Nepal']").click()


next_button1 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(4)

# Professional Experience
driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/button[1]").click()
span = driver.find_element(By.XPATH, "//span[normalize-space()='5 years']")
parent = span.find_element(By.XPATH, "./..")
driver.execute_script("arguments[0].click();", parent)

# time.sleep(4)
number_of_students = driver.find_element(By.NAME, "number_of_students_recruited_annually").send_keys("100")
# time.sleep(4)
focus_area = driver.find_element(By.NAME, "focus_area").send_keys("Undergraduate admisiion to USA")

success = driver.find_element(By.NAME, "success_metrics").send_keys("99%")

#services provided
driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[2]/div[1]/button[1]").click()

next_button2 = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(4)

# verificationa and preferences
business_reg_no = driver.find_element(By.NAME, "business_registration_number").send_keys("123456")

#preffered countries
driver.find_element(By.CSS_SELECTOR, ".font-satoshi-regular.text-translucent").click()
driver.find_element(By.XPATH, "//*[text()='Pakistan']").click()


driver.find_element(By.XPATH, "/html[1]/body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/button[1]").click()


# image_path = r"C:\Users\Lenovo\Desktop\signup_automation\Screenshot 2026-11-20 125231.png"
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img.png")

upload = driver.find_element(By.XPATH, "//input[@type='file']")
upload.send_keys(image_path)

submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(4)