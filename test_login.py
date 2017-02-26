from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture import driver


def test_login_admin(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("username").click()
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
