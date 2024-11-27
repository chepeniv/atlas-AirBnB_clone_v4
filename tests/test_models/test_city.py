#!/usr/bin/python3

import unittest
from models.city import City
from models.state import State
from models import storage_type, storage
import pep8
from models import city
import inspect
from datetime import datetime
from models.base_model import BaseModel


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
class TestCityFile(unittest.TestCase):

    def test_city__init__(self):
        new_city = City()
        self.assertEqual(new_city.name, "")
        self.assertEqual(new_city.state_id, "")


@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestCityDB(unittest.TestCase):

    def test_city__init__success(self):
        name = "John"
        state_id = "5-5-5-5"
        new_city = City(name=name, state_id=state_id)
        self.assertEqual(new_city.name, name)
        self.assertEqual(new_city.state_id, state_id)

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


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        if storage_type == 'db':
            self.assertEqual(city.name, None)
        else:
            self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        if storage_type == 'db':
            self.assertEqual(city.state_id, None)
        else:
            self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_d = c.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_d = c.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        city = City()
        string = "[City] ({}) {}".format(city.id, city.to_dict())
        self.assertEqual(string, str(city))


if __name__ == "__main__":
    unittest.main()
