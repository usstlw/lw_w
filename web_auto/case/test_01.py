import  unittest
class IntegerrithmeticTestCase(unittest.TestCase):
    def test_1(self): #test method names begin with 'test'
        '''用例说明：111'''
        print("11111")
        a = "admin"
        b = "admin1"
        self.assertNotIn(a,b)

    def setUp(self):
        print("先打开浏览器")

    @classmethod
    def setUpClass(cls):
        print("用例前，只执行一次")

    def test_a(self):
        '''用例说明：aaaaa'''
        print("22222")
        self.assertEqual((0*10),0)

    def test_A(self):
        '''用例说明：AAAAA'''
        print("33333")
        self.assertEqual((0*10),0)
        self.assertEqual((5 * 8), 40)

if __name__ == '__main__':
    unittest.main()

