import unittest
from main import get_records, post_records

def true_or_false(x, y):
    return x > y


class TestAirTablesGet(unittest.TestCase):


    def test_status_code_get_is_200(self):
        self.assertEqual(get_records().status_code, 200)


    def test_get_records(self):
        self.assertTrue(true_or_false(len(get_records().json()), 0))



class TestCasePostAritable(unittest.TestCase):
    

    def test_create_records(self):
        self.assertEqual(post_records('danilo', 'danilo@gmail.com').status_code, 200)




if __name__ == '__main__':
    unittest.main()