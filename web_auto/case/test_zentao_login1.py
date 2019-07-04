from selenium import webdriver
import time
import  unittest

class LoginTest(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")

    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def login(self,user,psw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(psw)
        self.driver.find_element_by_id("submit").click()

    def test_01(self):
        '''登录成功的案例'''
        time.sleep(2)
        self.login("admin","Zhanyi88")
        time.sleep(3)
        t = self.get_login_username()
        print("登录成功，获取结果:%s"%t)
        self.assertTrue(t == "admin")

    def test_02(self):
        '''登录失败 的案例'''
        time.sleep(2)
        #错误账号和密码
        self.login("admin1","")
        #判断是否登陆成功
        time.sleep(3)
        t = self.get_login_username()
        print("登录失败，获取结果：%s"%t)
        #self.assertTrue(1 == 2) #断言失败截图

    def tearDown(self):
        self.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

