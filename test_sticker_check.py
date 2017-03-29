from fixture import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sticker_check(driver):

    list = ["box-most-popular", "box-campaigns", "box-latest-products"]

    driver.get("http://localhost/litecart/index.php")
    WebDriverWait(driver, 10).until(EC.title_is("Online Store | My Store"))
    for section in list:
        section_item = driver.find_element_by_xpath("//div[@id='" + section + "']//ul")
        list_items = section_item.find_elements_by_tag_name("li")
        for list_item in list_items:
            len(list_item.find_elements_by_xpath(".//div[contains(@class, 'sticker')]")) == 1
