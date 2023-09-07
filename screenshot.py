from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1366,768")

driver = webdriver.Chrome(options=chrome_options)

def screenshot(url):
  driver.get(url)
  driver.save_screenshot('static/images/map/'+url.split('/')[-1])