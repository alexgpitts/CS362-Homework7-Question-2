import unittest
import leap_year


#unittest class tests
class TestCase(unittest.TestCase):

    # A test that checks 2004 which is a leap year evenly 
    # divisible by 4, but not 100 and not 400
    def test_leap_year_1(self): 
        self.assertEqual(leap_year.is_leap_year(2004), True) 

    # A test that checks 2001 which is not a leap year evenly 
    # divisible by 4
    def test_leap_year_2(self): 
        self.assertEqual(leap_year.is_leap_year(2001), False) 

    # A test that checks 2300 which is not a leap year because it is
    # divisible by 100 but not 400
    def test_leap_year_3(self): 
        self.assertEqual(leap_year.is_leap_year(2300), False) 

    # A test that checks 2400 which is a leap year because it is
    # divisible by 4, 100 and 400
    def test_leap_year_4(self): 
        self.assertEqual(leap_year.is_leap_year(2400), True) 




if __name__ == '__main__':
    unittest.main(verbosity=2)