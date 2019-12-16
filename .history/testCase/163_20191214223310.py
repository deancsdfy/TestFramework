import sys,unittest,time
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

    # # 登录
    # def test_login(self):
    #     Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
    #     self.uid =  WebDriverWait(self.driver, 20, 0.2).until(
    #         lambda x: x.find_element_by_id('spnUid')).text
    #     self.assertEqual(self.uid,'deancsdfy@163.com')

    def test_sendEmail(self):
        Login(self.driver,'deancsdfy@163.com','163688987').login_email163()
        self.writeEmailBtn =  WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_xpath('/html/body/div[1]/nav/div[1]/ul/li[2]'))
        self.writeEmailBtn.click()
        self.toMailAddresInput = WebDriverWait(self.driver, 20, 0.2).until(
            lambda x: x.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/section/header/div[1]/div[1]/div/div[2]'))
        js = 'document.getElementsByClassName("js-component-emailcontainer nui-multiLineIpt C-multiLineIpt nui-ipt").innerHTML="<p>2524165845@qq.com;</p>"; '
        self.driver.execute(js)
        self.subjectInput = self.driver.find_element_by_class_name('nui-ipt-input')
        self.subjectInput.send_keys('test-eamail')
        self.sendBtn = self.driver.find_element_by_link_text('发送')
        time.sleep(10)

if __name__ == "__main__":
    unittest.main()