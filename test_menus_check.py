from fixture import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_menus_check(driver):

    list = ["Appearence", "Logotype", "Catalog", "Product Groups", "Option Groups", "Manufacturers", "Suppliers", "Delivery Statuses",
            "Sold Out Statuses", "Quantity Units", "CSV Import/Export", "Countries", "Currencies", "Customers", "CSV Import/Export", "Newsletter",
            "Geo Zones", "Languages", "Storage Encoding", "Modules", "Customer", "Shipping", "Payment", "Order Total",
            "Order Success", "Order Action", "Orders", "Order Statuses", "Pages", "Reports", "Most Sold Products", "Most Shopping Customers",
            "Settings", "Defaults", "General", "Listings", "Images", "Checkout", "Advanced", "Security",
            "Slides", "Tax", "Tax Rates", "Translations", "Scan Files", "CSV Import/Export", "Users", "vQmods"]

    def login_admin(driver):
        driver.get("http://localhost/litecart/admin/login.php")
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()
        WebDriverWait(driver, 10).until(EC.title_is("My Store"))

    login_admin(driver)
    for i in range(len(list)):
        driver.find_element_by_xpath("//li[@id='app-']//span[.='" + list[i] + "']").click()
        driver.find_element_by_tag_name("h1")
        i += 1
