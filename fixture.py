import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd
