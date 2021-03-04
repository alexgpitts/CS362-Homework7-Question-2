import unittest
import leap_year


#unittest class tests
class TestCase(unittest.TestCase):

    # A test that checks 2004 which is a leap year evenly 
    # divisible by 4, but not 100 and not 400
    def test_leap_year_1(self): 
        self.assertEqual(leap_year.is_leap_year(2004), True) 

    def test_leap_year_2(self): 
        self.assertEqual(leap_year.is_leap_year(2001), False) 




if __name__ == '__main__':
    unittest.main(verbosity=2)