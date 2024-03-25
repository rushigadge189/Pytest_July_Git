import time

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser") ;
@pytest.fixture()
def browser(request) :
    return request.config.getoption("--browser") ;

@pytest.fixture()
def setup(browser) :
    if(browser=='chrome') :
        driver=webdriver.Chrome() ;
        print("OPENING IN CHROME BROWSER") ;

    elif (browser=='edge'):
        driver=webdriver.Edge() ;
        print("OPENING IN EDGE BROWSER") ;
    else:
        print("OPENING IN HEADLESS MODE") ;
        chrome_options=webdriver.ChromeOptions();
        chrome_options.add_argument("headless");
        driver=webdriver.Chrome(options=chrome_options) ;

    driver.implicitly_wait(5);
    driver.maximize_window();

    return driver
def pytest_metadata(metadata) :
    metadata["Class"] = "Credence" ;
    metadata["Batch"] = "CT#15" ;
    metadata.pop("Platform","None");

