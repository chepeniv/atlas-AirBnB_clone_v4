#!/usr/bin/python3

# import unittest
# import os
# from datetime import datetime
from uuid import uuid4
# from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel
# from models.state import State
# from models.city import City
# from models.user import User

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

# def setUpModule():
#     # runs at the start of the module
#     pass

# def tearDownModule():
#     # runs at the end of the module
#     pass


class TestFileStorage(unittest.TestCase):
    # __init__
    # new -- assert on __objects
    # save -- assert on file.json
    # reload -- assert on __objects, case file exist, file not exist
    # delete -- assert on __objects, case object not exist, object exist
    # close -- calls reload
    # construct_key -- assert on return

    def setUp(self):
        self.storage.all().clear()
        self.storage.save()
        self.storage.reload()

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = "file.json"
        # if os.path.exists(cls.json_file):
        #     os.remove(cls.json_file)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.json_file):
            os.remove(cls.json_file)

    def test_fs_count_empty(self):
        items = self.storage.all().items()
        items_count = len(items)
        self.assertEqual(items_count, 0)
        self.assertEqual(self.storage.count(), 0)

    def test_fs_count_class(self):
        self.assertEqual(self.storage.count(State), 0)
        self.assertEqual(self.storage.count(City), 0)
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(City())
        self.storage.new(City())
        self.storage.new(City())
        self.assertEqual(self.storage.count(State), 4)
        self.assertEqual(self.storage.count(City), 3)

    def test_fs_count_all(self):
        self.assertEqual(self.storage.count(), 0)
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(State())
        self.storage.new(City())
        self.storage.new(City())
        self.storage.new(City())
        self.storage.new(User())
        self.storage.new(User())
        self.assertEqual(self.storage.count(), 9)

    def test_fs_get_no_object(self):
        self.assertIsNone(self.storage.get(State, "invalid_id"))
        self.storage.new(State)
        self.assertIsNone(self.storage.get(State, "invalid_id"))

    def test_fs_get_object(self):
        new_state = State()
        self.storage.new(new_state)
        values_state = self.storage.all().values()
        values_state = list(values_state)
        values_state = values_state[0]
        get_state = self.storage.get(State, values_state.id)
        self.assertIsInstance(get_state, State)
        self.assertEqual(get_state, values_state)

        self.storage.all().clear()

        new_city = City()
        self.storage.new(new_city)
        values_city = self.storage.all().values()
        values_city = list(values_city)
        values_city = values_city[0]
        get_city = self.storage.get(City, values_city.id)
        self.assertIsInstance(get_city, City)
        self.assertEqual(get_city, values_city)

    def test_fs_properties(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.storage.all().clear()
        self.assertEqual(self.storage.all(), {})

    def test_fs_all(self):
        self.assertIsNotNone(self.storage.all())

    def test_fs_new(self):
        time = datetime.now().isoformat()
        base_id = str(uuid4())
        kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}

        new = BaseModel(**kwargs)
        key = self.storage.construct_key(new)

        self.assertNotIn(key, self.storage.all().keys())
        self.storage.new(new)
        self.assertIn(key, self.storage.all().keys())

    def test_fs_save(self):
        with open(self.json_file, 'r') as json_file:
            old_json = json_file.read()

        self.storage.new(State())
        self.storage.save()

        with open(self.json_file, 'r') as json_file:
            new_json = json_file.read()

        self.assertNotEqual(old_json, new_json)

    def test_fs_reload(self):
        new = State()
        new.save()

        old_state = self.storage.all().keys()
        old_state = list(old_state)

        self.storage.all().clear()
        clear_state = self.storage.all().keys()
        clear_state = list(clear_state)

        self.assertNotEqual(clear_state, old_state)
        self.storage.reload()
        new_state = self.storage.all().keys()
        new_state = list(new_state)
        self.assertEqual(new_state, old_state)


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    @unittest.skipIf(models.storage_t == 'db', "not testing file storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))


if __name__ == '__main__':
    unittest.main()
