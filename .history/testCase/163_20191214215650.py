import sys,unittest
sys.path.append('.')
from framework.logger import Logger
from PageObject.pageMethon import Login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

logger = Logger('163').getlogger()

class Test_email163(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.indexUrl = 'https://email.163.com/'
        self.driver.get(self.indexUrl)

    def tearDown(self):
        self.driver.quit()

    # 登录
    def test_login(self):
        Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
        self.uid = self.driver.find_element_by_id('spnUid')
        self.assertEqual(self.uid.text,'deancsdfy@163.com')

if __name__ == "__main__":
    unittest.main()