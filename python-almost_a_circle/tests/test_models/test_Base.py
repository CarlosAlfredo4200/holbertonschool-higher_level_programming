import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_id_generation(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)


if __name__ == '__main__':
    unittest.main()
