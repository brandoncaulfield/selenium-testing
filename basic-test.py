import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class list_app_test(unittest.TestCase):

    def setup(self):
        self.firefox_options = Options()
        self.firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.firefox_options)

    def test_title_text(self):
        self.driver.get("http://localhost:3000")
        assert "List App" in self.driver.title

# h1_elem = driver.find_element("link text")
# print(h1_elem)
    def teardown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()