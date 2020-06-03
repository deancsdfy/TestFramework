from framework.email import sendTestReportEmail
import os,time

# 进入测试用例目录
cd_testCase = 'cd testCase'

request_time = time.strftime('%Y%m%d',time.localtime(time.time())) #生成一个当前日期的日期字符串
allure_name = 'allure_{}'.format(request_time)
# 运行目录下所有测试用例，自动识别CPU核数，多进程执行用例并生成测试报告
# runAllTestCase = 'pytest -n auto --alluredir=./report/'
runAllTestCase = 'pytest -n auto --alluredir=./report/{}'.format(allure_name)
cd_report = 'cd report'
switchHtml = 'allure generate ./{} -o ./allure-result_{}'.format(allure_name,request_time)

os.system(cd_testCase)
os.system(runAllTestCase)
os.system(cd_report)
os.system(switchHtml)
    
# 测试报告发送到指定邮箱
# sendTestReportEmail()