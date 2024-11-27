#!/usr/bin/python3

import unittest
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage_type
import pep8 as pycodestyle
import time
from unittest import mock
import models
import inspect
module_doc = models.base_model.__doc__


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
class TestBaseModelFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.json_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        cls.storage.all().clear()

    def test_base__init__(self):
        base_obj = BaseModel()
        base_obj.save()
        self.assertIsInstance(base_obj.id, str)
        self.assertIsInstance(base_obj.created_at, datetime)
        self.assertIsInstance(base_obj.updated_at, datetime)
        self.assertIn(base_obj, self.storage.all().values())

    def test_base__init__kwargs(self):
        time = datetime.now().isoformat()
        base_id = str(uuid4())
        kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}

        base_obj = BaseModel(**kwargs)
        self.assertEqual(base_obj.id, base_id)
        self.assertEqual(base_obj.created_at.isoformat(), time)
        self.assertEqual(base_obj.updated_at.isoformat(), time)

    def test_base_to_dict(self):
        base_obj = BaseModel()
        base_dict = base_obj.to_dict()
        self.assertEqual(base_dict['__class__'], 'BaseModel')

    def test_base__str__(self):
        base_obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
            base_obj.id, base_obj.to_dict())
        self.assertEqual(str(base_obj), expected_str)

    def test_base_save(self):
        base_obj = BaseModel()
        last_update = base_obj.updated_at
        base_obj.save()
        new_update = base_obj.updated_at
        self.assertNotEqual(last_update, new_update)

    def test_base_storage_save(self):
        with open(self.json_file, 'r') as json_file:
            old_json = json_file.read()

        base_obj = BaseModel()
        base_obj.save()

        with open(self.json_file, 'r') as json_file:
            new_json = json_file.read()

        self.assertNotEqual(old_json, new_json)

    def test_base_delete(self):
        pass

    def test_base_id(self):
        pass

    def test_base_created_at(self):
        pass

    def test_base_updated_at(self):
        pass

# @unittest.skipIf(storage_type != 'db', 'Tests not designed for DBStorage')
# class TestBaseModelDB(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         pass

#     @classmethod
#     def tearDownClass(cls):
#         pass

#     def test_base__init__success(self):
#         pass

#     def test_base__init__filure(self):
#         pass

#     def test_base__init__kwargs(self):
#         time = datetime.now().isoformat()
#         base_id = str(uuid4())
#         kwargs = {'id': base_id, 'created_at': time, 'updated_at': time}

#         base_obj = BaseModel(**kwargs)
#         self.assertEqual(base_obj.id, base_id)
#         self.assertEqual(base_obj.created_at.isoformat(), time)
#         self.assertEqual(base_obj.updated_at.isoformat(), time)

#     def test_base_to_dict(self):
#         base_obj = BaseModel()
#         base_dict = base_obj.to_dict()
#         self.assertEqual(base_dict['__class__'], 'BaseModel')

#     def test_base__str__(self):
#         base_obj = BaseModel()
#         expected_str = "[BaseModel] ({}) {}".format(
#           base_obj.id, base_obj.__dict__)
#         self.assertEqual(str(base_obj), expected_str)

#     def test_base_save(self):
#         base_obj = BaseModel()
#         last_update = base_obj.updated_at
#         base_obj.save()
#         new_update = base_obj.updated_at
#         self.assertNotEqual(last_update, new_update)

#     def test_base_storage_save(self):
#         with open(self.json_file, 'r') as json_file:
#             old_json = json_file.read()

#         base_obj = BaseModel()
#         base_obj.save()

#         with open(self.json_file, 'r') as json_file:
#             new_json = json_file.read()

#         self.assertNotEqual(old_json, new_json)

#     def test_base_delete(self):
#         pass

#     def test_base_id(self):
#         pass

#     def test_base_created_at(self):
#         pass

#     def test_base_updated_at(self):
#         pass


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_instantiation(self):
        """Test that object is correctly created"""
        inst = BaseModel()
        self.assertIs(type(inst), BaseModel)
        inst.name = "Holberton"
        inst.number = 89
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
        self.assertEqual(inst.name, "Holberton")
        self.assertEqual(inst.number, 89)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""
        tic = datetime.utcnow()
        inst1 = BaseModel()
        toc = datetime.utcnow()
        # print(f'\ntic: {tic}')
        # print(f'inst1: {inst1.created_at}')
        # print(f'toc: {toc}')
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.utcnow()
        inst2 = BaseModel()
        toc = datetime.utcnow()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.to_dict())
        self.assertEqual(string, str(inst))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main()
