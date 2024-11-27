import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class ChromeDriverManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ChromeDriverManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, driver_path='chromedriver.exe', headless=True):
        if self._initialized:
            return
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self._initialized = True

    def fetch_tos_content(self, url, wait_time=3):
        self.driver.get(url)
        time.sleep(wait_time)  # Waiting for JavaScript to execute and load
        page_source = self.driver.page_source
        return page_source

    def close(self):
        self.driver.quit()
        self._initialized = False
