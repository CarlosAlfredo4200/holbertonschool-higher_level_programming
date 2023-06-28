# import unittest
# from models.rectangle import Rectangle

# class TestRectangle(unittest.TestCase):
#     def test_valid_width_height(self):
#         rect = Rectangle(1, 2)
#         self.assertEqual(rect.width, 1)
#         self.assertEqual(rect.height, 2)

#     def test_valid_width_height_x(self):
#         rect = Rectangle(1, 2, 3)
#         self.assertEqual(rect.width, 1)
#         self.assertEqual(rect.height, 2)
#         self.assertEqual(rect.x, 3)

#     def test_valid_width_height_x_y(self):
#         rect = Rectangle(1, 2, 3, 4)
#         self.assertEqual(rect.width, 1)
#         self.assertEqual(rect.height, 2)
#         self.assertEqual(rect.x, 3)
#         self.assertEqual(rect.y, 4)

#     def test_invalid_width_type(self):
#         with self.assertRaises(TypeError):
#             Rectangle("1", 2)

#     def test_invalid_height_type(self):
#         with self.assertRaises(TypeError):
#             Rectangle(1, "2")

#     def test_invalid_x_type(self):
#         with self.assertRaises(TypeError):
#             Rectangle(1, 2, "3")

#     def test_invalid_y_type(self):
#         with self.assertRaises(TypeError):
#             Rectangle(1, 2, 3, "4")

#     def test_invalid_extra_argument(self):
#         with self.assertRaises(TypeError):
#             Rectangle(1, 2, 3, 4, 5)

#     def test_invalid_width_value(self):
#         with self.assertRaises(ValueError):
#             Rectangle(-1, 2)

#     def test_invalid_height_value(self):
#         with self.assertRaises(ValueError):
#             Rectangle(1, -2)

#     def test_invalid_x_value(self):
#         with self.assertRaises(ValueError):
#             Rectangle(0, 2)

#     def test_invalid_y_value(self):
#         with self.assertRaises(ValueError):
#             Rectangle(1, 0)

#     def test_invalid_x_negative_value(self):
#         with self.assertRaises(ValueError):
#             Rectangle(1, 2, -3)

#     def test_invalid_y_negative_value(self):
#         with self.assertRaises(ValueError):
#             Rectangle(1, 2, 3, -4)

#     def test_area(self):
#         rect = Rectangle(3, 4)
#         self.assertEqual(rect.area(), 12)

# if __name__ == '__main__':
#     unittest.main()

