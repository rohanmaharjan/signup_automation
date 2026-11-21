from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import os
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria
import random
from fpdf import FPDF

# driver = webdriver.Chrome()

run_id = int(time.time())
email_front = os.getenv("GMAIL_USER").split("@")[0]

def new_phone():
    prefix = random.choice(["984", "985", "986", "980", "981", "982", "974", "975"])
    Phone = prefix + str(random.randint(1000000, 9999999))
    return Phone


GMAIL_USER = os.getenv("GMAIL_USER")
API_KEY = "Your Mailosaur API Key"
SERVER_ID = "Your Mailosaur Server ID"

def new_email():
    Email = f"{email_front}{run_id}@{SERVER_ID}.mailosaur.net"
    return Email

client = MailosaurClient(API_KEY)

# url to terms and condition page
WEBSITE_URL="Website URL"

# stores test results
results = []

# set up you account page
'''
first_name = driver.find_element(By.NAME, "firstName").send_keys("Ram")

last_name = driver.find_element(By.NAME, "lastName").send_keys("Shrestha")

driver.find_element(By.NAME, "email").send_keys(Email)

phone_no = driver.find_element(By.NAME, "phoneNumber").send_keys(Phone)

password = driver.find_element(By.NAME, "password").send_keys("Asdfghjk!23")

conform_password = driver.find_element(By.NAME, "confirmPassword").send_keys("Asdfghjk!23")
'''

# function defination for set up page in order to avoid repetition of code for different test cases
def set_up_page_review(test_id, description, data, expected):
    # URL = os.getenv("WEBSITE_URL")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(WEBSITE_URL)
    time.sleep(2)

    # terms and condition page
    checkbox = driver.find_element(By.CSS_SELECTOR, "#remember").click()

    continue_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Continue'])[1]").click()
    time.sleep(4)

    for field, value in data.items():
        driver.find_element(By.NAME, field).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    fields = driver.find_elements(By.NAME, "firstName")

    def get_code():
        criteria = SearchCriteria()
        criteria.sent_to = new_email()

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
    
    # fields = driver.find_elements(By.NAME, "firstName")

    if len(fields) == 0:
        actual = "pass"
    else:
        actual = "fail"

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    results.append(f"{test_id} | {description} | expected: {expected} | actual: {actual} | {status}")   
    driver.quit()
time.sleep(2)

# test cases
# positive test cases
valid_all = {
    "firstName": "Rohan",
    "lastName": "Maharjan",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvbn!23",
}

valid_hyphen_name = {
    "firstName": "Rohan-Kumar",
    "lastName": "Maharjan",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword":"Zxcvbn!23",
}
valid_small_firstname_lastname = {
    "firstName": "R",
    "lastName": "M",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword":"Zxcvbn!23",
}

valid_space_lastname = {
    "firstName": "Rohan",
    "lastName": "Govinda Maharjan",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvbn!23",
}

valid_min_password = {
    "firstName": "Rohan",
    "lastName": "Maharjan",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!2",
    "confirmPassword": "Zxcvbn!2",
}

# negative test cases
empty_firstname = {
    "firstName": "",
    "lastName": "Shrestha",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvbn!23",
}

empty_lastname = {
    "firstName": "Rohan",
    "lastName": "",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvbn!23",
}

empty_fields = {
    "firstName": "",
    "lastName": "",
    "email": "",
    "phoneNumber": "",
    "password": "",
    "confirmPassword": "",
}

invalid_email = {
    "firstName": "Rohan",
    "lastName": "Maharjan",
    "email": "abc@",
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvbn!23",
}

invalid_phone = {
    "firstName": "Rohan",
    "lastName": "Maharjan",
    "email": new_email(),
    "phoneNumber": "98123",
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvbn!23",
}

weak_password = {
    "firstName": "Rohan",
    "lastName": "Maharjan",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "abc12345",
    "confirmPassword": "abc12345",
}

different_password = {
    "firstName": "Rohan",
    "lastName": "Maharjan",
    "email": new_email(),
    "phoneNumber": new_phone(),
    "password": "Zxcvbn!23",
    "confirmPassword": "Zxcvb!23",
}


set_up_page_review("P1", "All valid data", valid_all, "moves to next page")
set_up_page_review("P2", "First name with hyphen", valid_hyphen_name, "moves to next page")
set_up_page_review("P3", "Small first and last name", valid_small_firstname_lastname, "moves to next page")
set_up_page_review("P4", "Last name with space", valid_space_lastname, "moves to next page")
set_up_page_review("P5", "Minimum password length", valid_min_password, "moves to next page")
set_up_page_review("P6", "Empty first name", empty_firstname, "shows error message")
set_up_page_review("P7", "Empty last name", empty_lastname, "shows error message")
set_up_page_review("P8", "All empty fields", empty_fields, "shows error messages")
set_up_page_review("P9", "Invalid email format", invalid_email, "shows error message")
set_up_page_review("P10", "Invalid phone number", invalid_phone, "shows error message")
set_up_page_review("P11", "Weak password", weak_password, "shows error message")
set_up_page_review("P12", "Different passwords", different_password, "shows error message")


pdf = FPDF()
pdf.add_page()
pdf.set_font("Times New Roman", "B", 14)
pdf.cell(0, 10, "Test report for SignUp Page", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Times New Roman", size=10)
for line in results:
    pdf.multi_cell(0, 7, line)
pdf.output("test_report.pdf")
