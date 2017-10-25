import unittest


class TestPy(unittest.TestCase):
    def test_float_to_int(self):
        self.assertEqual(1, int(1.0))

    def test_int_to_bool(self):
        self.assertTrue(bool(10))

