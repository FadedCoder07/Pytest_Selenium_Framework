from selenium.webdriver.common.by import By
class Anasayfaa:
    def __init__(self,driver):
        self.driver=driver
    def first_item_click(self):
        self.driver.find_element(By.XPATH, "//div[@class='item-box']//h2/a[not(contains(text(),'Gift Card'))]").click()