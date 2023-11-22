# we can pass multiple values through parameters. consider login test,there are four scenarios,
# But every time we cants change code for each scenario, so we use parameters for that.
# we're defining parameters in conftest file.and crete new file test_login_parameters.py for test that scenario.
# when we only use parameters.There are 3 scenarios for to fail the test case, that 3 case report shows
# assert fail, but in real that fail result means your test case is pass, to give status pass we use nested if in our
# test case.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        driver = webdriver.Firefox()

    elif browser == 'edge':
        driver = webdriver.Edge()

    else:
        chrome_options = Options()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)


    driver.implicitly_wait(3)
    driver.maximize_window()
    return driver


# below code for changes in html report metadata


def pytest_metadata(metadata):
    # To Add metadata
    metadata["Environment"] = "Test"
    metadata["Project Name"] = "OrangeHrm"
    metadata["Module Name"] = "Employee"
    metadata["Tester"] = "Ruturaj"

    # to remove existing metadata
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


# below code for parameterized test case

@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1234", "Fail"),
    ("Admin1", "admin1234", "Fail")
])
def getDataforlogin(request):
    return request.param
