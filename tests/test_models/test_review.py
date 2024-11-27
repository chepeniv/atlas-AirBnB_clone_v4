#!/usr/bin/python3

import unittest
from models.review import Review
from models.state import State
from models.city import City
from models import storage_type, storage
import inspect
from models import review
from models.base_model import BaseModel
import pep8


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
class TestReviewFile(unittest.TestCase):

    def test_review__init__(self):
        new_rev = Review()
        self.assertEqual(new_rev.place_id, "")
        self.assertEqual(new_rev.user_id, "")
        self.assertEqual(new_rev.text, "")

    def test_review_text(self):
        pass

    def test_review_place_id(self):
        pass

    def test_review_user_id(self):
        pass


@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestReviewDB(unittest.TestCase):

    def setUp(self):
        """Setup a new City instance before each test"""
        self.state = State(name="Test_State")
        storage.new(self.state)
        storage.save()
        self.city = City(name="Test_City", state_id=self.state.id)
        storage.new(self.city)
        storage.save()

    def tearDown(self):
        """Clean up the class instances after each test"""
        storage.delete(self.city)
        storage.delete(self.state)
        storage.save()

    def test_city_instance_in_storage(self):
        """Test that the City instance is stored in the database"""
        key = "City." + self.city.id
        self.assertIn(key, storage.all())

    def test_city_name_in_storage(self):
        """Test that the City instance in storage has the correct name"""
        key = "City." + self.city.id
        self.assertEqual(storage.all()[key].name, "Test_City")

    def test_city_retrieval_by_id(self):
        """Test retrieval of the city from storage by its ID"""
        city = storage.all().get("City." + self.city.id)
        self.assertIsNotNone(city)

    def test_city_retrieved_has_correct_id(self):
        """Test that the retrieved city's ID matches the original ID"""
        city = storage.all().get("City." + self.city.id)
        self.assertEqual(city.id, self.city.id)

    def test_city_retrieved_has_correct_name(self):
        """Test that the retrieved city's name matches the expected value"""
        city_from_storage = storage.all().get("City." + self.city.id)
        self.assertEqual(city_from_storage.name, "Test_City")

    def test_state_id_type(self):
        """Test that state_id is a string"""
        self.assertEqual(type(self.city.state_id), str)

    def test_state_id_matches_state(self):
        """Test that state_id matches the State's ID"""
        self.assertEqual(self.city.state_id, self.state.id)

    def test_city_name_type(self):
        """Test that name is a string"""
        self.assertEqual(type(self.city.name), str)

    def test_city_name_value(self):
        """Test that name matches the expected value"""
        self.assertEqual(self.city.name, "Test_City")


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_place_id_attr(self):
        """Test Review has attr place_id, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if storage_type == 'db':
            self.assertEqual(review.place_id, None)
        else:
            self.assertEqual(review.place_id, "")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if storage_type == 'db':
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if storage_type == 'db':
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.to_dict())
        self.assertEqual(string, str(review))


if __name__ == "__main__":
    unittest.main()
