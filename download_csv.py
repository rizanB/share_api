from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def download_csv(url, dir):
    options = webdriver.FirefoxOptions()
    options.set_preference('browser.download.folderList', 2)
    options.set_preference('browser.download.dir', dir)
    options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/csv')
    options.add_argument("--headless")

    driver = webdriver.Firefox(options = options)

    try:
        driver.get(url)

        print('ready to wait')
        wait = WebDriverWait(driver, 20)
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download as CSV')]")))
        download_button.click()

        time.sleep(3)

    finally:
        driver.quit()