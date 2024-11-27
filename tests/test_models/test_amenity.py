#!/usr/bin/python3

import unittest
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models import storage, storage_type
import pep8
import inspect
from datetime import datetime

################################
# chepe@Ariel: besides BaseModel lets use this one to test out the
# workflow and approach we're gonna use to implement testing for both
# bd and file storage modes
################################


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
class TestAmenityFile(unittest.TestCase):

    def test_amenity__init__(self):
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.name, "")

    # Ariel@chepe this file is where I wrote tests for
    # Ariel@self come back to once it clicks
    def test_property_name(self):
        self.assertEqual(Amenity.name, "")

    # setup amenity before testing
    def setUp(self):
        self.amenity = Amenity("")

    # cleans up after setup
    def tearDown(self):
        storage.delete(self.amenity)

    # test to see if amenity inherits from base and basemodel
    def test_amenity_inherit(self):
        self.assertIsInstance(self.amenity, BaseModel)
        self.assertIsInstance(self.amenity, Base)

    # Ariel@Chepe don't know if it's truly necessary but its another test idea
    def test_amenity_many_to_many(self):
        # write test here
        pass


@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestAmenityDB(unittest.TestCase):
    """Amenity DB tests"""
    def setUp(self):
        """Setup a new User instance before each test"""
        self.amenity = Amenity(name="Chair")
        storage.new(self.amenity)
        storage.save()

    def tearDown(self):
        """Teardown of all User instances after each test"""
        storage.delete(self.amenity)
        storage.save()

    def test_amenity_instance_in_storage(self):
        """Test that the Amenity instance is stored in the database"""
        key = "Amenity." + self.amenity.id
        self.assertIn(key, storage.all())

    def test_amenity_name_in_storage(self):
        """Test that the Amenity instance in storage has the correct name"""
        key = "Amenity." + self.amenity.id
        self.assertEqual(storage.all()[key].name, "Chair")

    def test_amenity_retrieval_by_id(self):
        """Test retrieval of the Amenity from storage by its ID"""
        amenity_from_storage = storage.all().get("Amenity." + self.amenity.id)
        self.assertIsNotNone(amenity_from_storage)

    def test_amenity_name_type(self):
        """Test that the name attribute is a string"""
        self.assertEqual(type(self.amenity.name), str)

    def test_amenity_name_value(self):
        """Test that the name matches the expected value"""
        self.assertEqual(self.amenity.name, "Chair")


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            # print(f'func in self.amenity_F: {func}')
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's as an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        if storage_type == 'db':
            self.assertEqual(amenity.name, None)
        else:
            self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        print(am.__dict__)
        new_d = am.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in am.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_d = am.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], am.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], am.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.to_dict())
        self.assertEqual(string, str(amenity))


if __name__ == "__main__":
    unittest.main()
