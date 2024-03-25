from selenium import webdriver
from ExcelDataProvider import ExcelDataProvider

# Initialize WebDriver without specifying the ChromeDriver path
driver = webdriver.Chrome()  

def login_with_credentials(username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element("id", "user-name").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    driver.find_element("id", "login-button").click()

    # Example verification step
    if "inventory" in driver.current_url:
        print(f"Login successful with username: {username}")
    else:
        print(f"Login failed for username: {username}")

def login_with_excel_data(file_path, sheet_name):
    test_data = ExcelDataProvider.get_test_data(file_path, sheet_name)
    for data in test_data:
        username = data[0]
        password = data[1]
        login_with_credentials(username, password)

if __name__ == "__main__":
    # Provide path to your Excel file and sheet name
    excel_file_path = "C:\\Users\\sanja\\OneDrive\\Documents\\Worldline Assessment\\assignment no 4\\credentials.xlsx"
    excel_sheet_name = "Sheet1"

    login_with_excel_data(excel_file_path, excel_sheet_name)

# Quit the driver after all tests are done
driver.quit()
