# 🔐 Demo Web Shop - Login Functionality Automation

**Task 3 - Prodigy**

This project automates Login Functionality testing for [Demo Web Shop](https://demowebshop.tricentis.com/) using **Selenium WebDriver**, **Pytest**, and XPath locators in Python.

* * *

## ✅ Test Scenarios Covered:

1.  **Positive Login Test**
    
    *   Valid username and password
        
    *   Verify successful login
        
2.  **Negative Login - Invalid Username**
    
    *   Invalid username, valid password
        
    *   Validate error message display
        
3.  **Negative Login - Invalid Password**
    
    *   Valid username, invalid password
        
    *   Validate error message display
        
4.  **Negative Login - Empty Fields**
    
    *   Both fields empty
        
    *   Validate error message display
        

* * *

## 🛠️ Technology Used:

*   **Python**
    
*   **Selenium WebDriver**
    
*   **Pytest**
    
*   **XPath Locators**
    

* * *

## ⚙️ Prerequisites:

*   Python installed
    
*   Chrome browser and ChromeDriver installed
    
*   Selenium and Pytest libraries
    

Install requirements using:

bash

CopyEdit

`pip install selenium pytest`  

* * *

## 🚀 How to Run Tests:

Execute the following command in your project directory:

bash

CopyEdit

`pytest demo_login1.py`  

All test cases use **explicit waits** and **XPath locators** for stable automation.

* * *

## 📂 Project Structure:

bash

CopyEdit

`├── test_login.py     # Contains all Login test cases ├── README.md         # Project documentation └── requirements.txt  # Dependencies (Optional)`

* * *

## 📝 Notes:

*   Tests are written for [https://demowebshop.tricentis.com/](https://demowebshop.tricentis.com/)
    
*   Ensure correct credentials are updated for valid login tests
    
*   Uses XPath for all element selections


