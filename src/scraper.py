from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = self._init_driver()

    def _init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-logging")
        chrome_options.add_argument('--log-level=3')
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        os.system('cls' if os.name == 'nt' else 'clear')

        return driver
    
    def get_pdf_links(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        pdf_links = []
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute('href')
            if href and (('Anexo_I' in href or 'Anexo_II' in href) and href.endswith('.pdf')):
                pdf_links.append(href)
                
        return pdf_links
    
    def close_driver(self):
        self.driver.quit()