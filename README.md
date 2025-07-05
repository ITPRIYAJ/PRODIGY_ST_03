# PRODIGY_ST_03
Task 3: Automate Positive and Negative Login Functionality using Selenium with XPath Locators. Includes:
✅ Valid login test 
✅ Invalid username test
✅ Invalid password test 
✅ Empty fields validation
🔐 Demo Web Shop - Login Functionality Automation
Task 3 - @Prodigy

This project automates Login Functionality testing for Demo Web Shop using Selenium WebDriver, Pytest, and XPath locators in Python.

✅ Test Scenarios Covered:
Positive Login Test

Valid username and password

Verify successful login

Negative Login - Invalid Username

Invalid username, valid password

Validate error message display

Negative Login - Invalid Password

Valid username, invalid password

Validate error message display

Negative Login - Empty Fields

Both fields empty

Validate error message display

🛠️ Technology Used:
Python

Selenium WebDriver

Pytest

XPath Locators

⚙️ Prerequisites:
Python installed

Chrome browser and ChromeDriver installed

Selenium and Pytest libraries

Install requirements using:

bash
Copy
Edit
pip install selenium pytest  
🚀 How to Run Tests:
Execute the following command in your project directory:

bash
Copy
Edit
pytest test_login.py  
All test cases use explicit waits and XPath locators for stable automation.

📂 Project Structure:
bash
Copy
Edit
├── test_login.py     # Contains all Login test cases
├── README.md         # Project documentation
└── requirements.txt  # Dependencies (Optional)
📝 Notes:
Tests are written for https://demowebshop.tricentis.com/

Ensure correct credentials are updated for valid login tests

Uses XPath for all element selections


