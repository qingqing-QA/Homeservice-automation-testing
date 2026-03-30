import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # CI 必须加

    driver = webdriver.Chrome(options=options)
    driver.get("https://example.com")

    yield driver

    driver.quit()
