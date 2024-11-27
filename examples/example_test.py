#!/usr/bin/python3
'''
python test script for Base class
execute test :
    python3 -m unittest test.test_models.test_base
or
    python3 -m unittest test/test_models/test_base.py

reference list of assert methods:

    assertEqual(a, b)           a == b
    assertNotEqual(a, b)        a != b
    assertTrue(x)               bool(x) is True
    assertFalse(x)              bool(x) is False
    assertIs(a, b)              a is b
    assertIsNot(a, b)           a is not b
    assertIsNone(x)             a is None
    assertIsNotNone(x)          a is not None
    assertIn(a, b)              a in b
    assertNotIn(a, b)           a not in b
    assertIsInstance(a, b)      isinstance(a, b)
    assertNotIsInstance(a, b)   not isinstance(a, b)

    assertAlmostEqual(a, b)     round(a-b, 7) == 0
    assertNotAlmostEqual(a, b)  round(a-b, 7) != 0
    assertGreater(a, b)         a > b
    assertGreaterEqual(a, b)    a >= b
    assertLess(a, b)            a < b
    assertLessEqual(a, b)       a <= b
    assertRegex(s, r)           r.search(s)
    assertNotRegex(s, r)        not r.search(s)
    assertCountEqual(a, b)      a and b have the same number of each
                                element (regardless of order)

    assertRaises(exc, fun, *args, **kwds)
    assertRaisesRegex(exc, r, fun, *args, **kwds)
    assertWarns(warn, fun, *args, **kwds)
    assertWarnsRegex(warn, r, fun, *args, **kwds)
    assertLogs(logger, level)
'''


import io, os, contextlib, unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_base_id(self):
        base = Base()
        self.assertIsNotNone(base.id)

    def test_base_id_increment(self):
        base_A = Base()
        base_B = Base()
        self.assertEqual(base_A.id + 1, base_B.id)

    def test_base_id_assignment(self):
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

class TestRectangleClass(unittest.TestCase):

    def tearDown(self):
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rect__init__(self):
        rectA = Rectangle(1, 2)
        self.assertEqual(rectA.width, 1)
        self.assertEqual(rectA.height, 2)

        rectB = Rectangle(1, 2, 3)
        self.assertEqual(rectB.x, 3)

    def test_rect_wrong_param(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("W", 2)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, "H")

    def test_rect_neg_params(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 2)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -2)

    def test_rect_zero_params(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)

    def test_rect_area(self):
        rect = Rectangle(3, 3)
        self.assertEqual(rect.area(), 9)

    def test_rect__str__(self):
        rect = Rectangle(3, 3)
        self.assertEqual(str(rect), "[Rectangle] ({}) 0/0 - 3/3".format(rect.id))

    def test_rect_display(self):
        rect = Rectangle(3, 3)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue().strip()
        self.assertEqual(output, "###\n###\n###")

    def test_rect_display_with_x(self):
        rect = Rectangle(3, 3, 4)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue()
        self.assertEqual(output, "    ###\n    ###\n    ###\n")

    def test_rect_display_with_x_y(self):
        rect = Rectangle(3, 3, 4, 4)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue()
        self.assertEqual(output, "\n\n\n\n    ###\n    ###\n    ###\n")

    def test_rect_to_dict(self):
        rect = Rectangle(4, 4)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': rect.id, 'width': 4, 'height': 4, 'x': 0, 'y': 0})

    def test_rect_update(self):
        rect = Rectangle(4, 4)
        self.assertIsNone(rect.update())

        rect.update(89)
        self.assertEqual(rect.id, 89)

        rect.update(89, 1)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': 89, 'width': 1, 'height': 4, 'x': 0, 'y': 0})

    def test_rect_create(self):
        self.assertIsInstance(Rectangle.create(**{ 'id': 89}), Rectangle)

        self.assertIsInstance(Rectangle.create(
            **{ 'id': 89,
                'width': 1
               }), Rectangle)

        self.assertIsInstance(Rectangle.create(
            **{ 'id': 89,
                'width': 1,
                'height': 2
               }), Rectangle)

    def test_rect_save_to_file_none(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertIsNone(Rectangle.save_to_file(None))
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_rect_save_to_file_empty(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertIsNone(Rectangle.save_to_file([]))
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_rect_save_to_file_one_object(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_rect_load_from_file_doesnt_exist(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rect_load_from_file_exist(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        self.assertNotEqual(Rectangle.load_from_file(), [])

if __name__== '__main__':
    unittest.main()
