import os,time

# 进入测试用例目录
cd_testCase = 'cd case'

request_time = time.strftime('%Y%m%d%H',time.localtime(time.time())) #生成一个当前日期的日期字符串
allure_name = 'allure_{}'.format(request_time)
# 运行目录下所有测试用例，自动识别CPU核数，多进程执行用例并生成测试报告
# runAllTestCase = 'pytest -n auto --alluredir=./report/'
allurePath = './report/allure_{}'.format(request_time)
runAllTestCase = 'pytest -n auto --alluredir={}'.format(allurePath)
cd_report = 'cd report'
allureReportPath = './report/allure_result_{}'.format(request_time)
switchHtml = 'allure generate {} -o {}'.format(allurePath,allureReportPath)
open_test_report = 'allure open -h 127.0.0.1 -p 5055 {}'.format(allureReportPath)

os.system(cd_testCase)
os.system(runAllTestCase)
os.system(cd_report)
os.system(switchHtml)
os.system(open_test_report)