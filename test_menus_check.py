from fixture import driver
from test_login import test_login_admin


def test_menus_check(driver):

    list = ["Appearence", "Logotype", "Catalog", "Product Groups", "Option Groups", "Manufacturers", "Suppliers", "Delivery Statuses",
            "Sold Out Statuses", "Quantity Units", "CSV Import/Export", "Countries", "Currencies", "Customers", "CSV Import/Export", "Newsletter",
            "Geo Zones", "Languages", "Storage Encoding", "Modules", "Customer", "Shipping", "Payment", "Order Total",
            "Order Success", "Order Action", "Orders", "Order Statuses", "Pages", "Reports", "Most Sold Products", "Most Shopping Customers",
            "Settings", "Defaults", "General", "Listings", "Images", "Checkout", "Advanced", "Security",
            "Slides", "Tax", "Tax Rates", "Translations", "Scan Files", "CSV Import/Export", "Users", "vQmods"]

    for i in range(len(list)):
        driver.find_element_by_xpath("//li[@id='app-']//span[.='" + list[i] + "']").click()
        driver.find_element_by_tag_name("h1")
        i += 1
