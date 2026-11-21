## SIGNUP PAGE AUTOMATION PROJECT
---
**About the project**
The project is fully automated signup page testing. Here total 12 test cases are done 5 positive and 7 negative test cases.
---

## Environment Setup
**Technology and Languages**
- Python, Selenium, SelectorHub, Mailosaur API, FPDF, VS code

**To run the code**
- install all required packages and dependencies from requirements.txt
  ```python
  pip install -r requirements.txt
  ```

- set up .env file and include WEBSITE_URL, PERSONAL_GMAIL, MAILOSAUR_API_KEY, MAILOSAUR_SERVER_ID

- to run the script do python file_name.py

---

## Test Cases
---
**Positive Test Cases**
- All valid data
- First name with hyphen
- Small first and last name (short first name and short last name e.g R M)
- Last name with space
- Minimum password length

**Negative Test Cases**
- Empty first name
- Empty last name
- All empty fields
- Invalid email format
- Invalid phone number
- Weak password
- Different passwords

