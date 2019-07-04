import unittest
from common import HTMLTestRunner_cn




#用例的路径
casePath = "D:\\web_auto\\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule) #
print(discover)
reportPath = "D:\\web_auto\\report"+"report.html"
fp = open(reportPath,"wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                       title="报告的title",
                                        description="描述你的报告做什么用",
                                          retry=1)
runner.run(discover)
fp.close()
