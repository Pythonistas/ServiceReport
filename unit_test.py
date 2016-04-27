import unittest
from ServiceReport import business_unit_for_user


class TestDataMethods(unittest.TestCase):

    def test_business_unit_for_user(self):
        self.assertIsNone(business_unit_for_user('blah blah blah'))
        self.assertEqual(business_unit_for_user('Mal'), 'Serenity')
        self.assertEqual(business_unit_for_user('Barney'), 'Flintstones')


if __name__ == '__main__':
    unittest.main()
