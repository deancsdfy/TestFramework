import unittest
from testCase import douban
from testCase import email_163
from framework.HTMLTestRunner import HTMLTestRunner
from framework.email import sendTestReportEmail

suites = unittest.TestSuite()
suites.addTests(unittest.TestLoader().loadTestsFromModule(douban))
suites.addTests(unittest.TestLoader().loadTestsFromModule(email_163))


if __name__ == "__main__":
    with open('report/HTMLREport.html', 'wb+') as f:
        runner = HTMLTestRunner(stream=f,
                                description='Report Details',
                                verbosity=2,)
        runner.run(suites)
    # 测试报告发送到指定邮箱
    sendTestReportEmail()