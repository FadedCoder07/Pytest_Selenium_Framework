from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest

@pytest.fixture(scope="class")
def setup(request):
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
