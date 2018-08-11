import unittest
import moduls
import web
import data as d

class TestSuite(unittest.TestCase):
    #@unittest.skip(" test_method_test_check, Reason: to long")
    def test_method_test_check(self):
        self.assertEqual(moduls.test(), "Hi")
    #@unittest.skip(" test_var_test_check, Reason: to long")
    def test_var_test_check(self):
        self.assertEqual(moduls.sayhi, "Hi")
    #@unittest.skip(" test_StatusCode, Reason: to long")
    def test_StatusCode(self):
        self.assertEqual(moduls.getStatus_code(d.url_ok), 200)
    #@unittest.skip(" test_Login_check, Reason: to long")
    def test_Login_check(self):
        self.assertTrue(moduls.getElement(d.url_ok, "h1", "Login"))
    #@unittest.skip(" test_FNT_login to long")
    def test_FNT_login(self):
        self.assertTrue(web.fnt_login())
    @unittest.skip(" test_FNT_loginHARD, Reason: to long")
    def test_FNT_loginHARD(self):
        self.assertTrue(web.fnt_login(2))
if __name__ == '__main__':
    unittest.main()