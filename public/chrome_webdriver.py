from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

class ChromeWebDriver:
    def __new__(cls) -> WebDriver:
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument("window-size=1920x1080")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver