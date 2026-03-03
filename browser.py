from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def get_driver():
    config = load_config()
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(config['implicit_wait'])
    return driver
