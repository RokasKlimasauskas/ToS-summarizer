import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def fetch_tos_content(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_driver_path = 'chromedriver.exe'  # Replace with the actual path to your ChromeDriver
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Initializing new Chrome browser session
    
    driver.get(url)
    time.sleep(3)   # Waiting for JavaScript to execute and load
 
    page_source = driver.page_source
    driver.quit()
    return page_source

def parse_tos_content(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    return soup.get_text()

def content(web_url):
    tos_content_fetched = fetch_tos_content(web_url)
    tos_content_parsed = parse_tos_content(tos_content_fetched)
    return tos_content_parsed

