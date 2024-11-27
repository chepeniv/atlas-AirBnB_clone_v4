#!/usr/bin/python3


import unittest
import os
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage_type, storage
import inspect
from models import user
from models.base_model import BaseModel
import pep8


@unittest.skipIf(storage_type == 'db', 'Tests not designed for DBStorage')
class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.storage = FileStorage()
        cls.test_file = "file.json"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_file):
            os.remove(cls.test_file)

    def test_user__init__(self):
        new_user = User()
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_user_to_dict(self):
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")

    def test_user_save_reload(self):
        new_user = User()
        old_updated_at = new_user.updated_at
        key = f"User.{new_user.id}"

        new_user.save()
        self.storage.reload()
        self.assertNotEqual(old_updated_at, new_user.updated_at)
        self.assertIn(key, self.storage.all())

    def test_user_email(self):
        # Ariel@Chepe I put the following code in comments because it was the
        # first thing I saw before the one I have now
        # Let me know if either are even correct
        # self.user = User(email="") not right?
        self.assertEqual(User.email, "")

    def test_user_password(self):
        # self.user = User(password="")
        self.assertEqual(User.password, "")

    def test_user_first_name(self):
        # self.user = User(first_name="")
        self.assertEqual(User.first_name, "")

    def test_user_last_name(self):
        # self.user = User(last_name="")
        self.assertEqual(User.last_name, "")

    def test_user_places(self):
        pass

    def test_user_reviews(self):
        pass


@unittest.skipUnless(storage_type == 'db', "Tests designed only for DBStorage")
class TestUserDB(unittest.TestCase):

    def setUp(self):
        """Setup a new User instance before each test"""
        self.user = User(email="a@b.com", password="password",
                         first_name="John", last_name="Roe")
        storage.new(self.user)
        storage.save()

    def tearDown(self):
        """Clean up the User instance after each test"""
        storage.delete(self.user)
        storage.save()

    def test_first_name_type(self):
        """Test that first_name is a string"""
        self.assertEqual(type(self.user.first_name), str)

    def test_last_name_type(self):
        """Test that last_name is a string"""
        self.assertEqual(type(self.user.last_name), str)

    def test_email_type(self):
        """Test that email is a string"""
        self.assertEqual(type(self.user.email), str)

    def test_password_type(self):
        """Test that password is a string"""
        self.assertEqual(type(self.user.password), str)

    def test_first_name_value(self):
        """Test that first_name can be set"""
        self.assertEqual(self.user.first_name, "John")

    def test_last_name_value(self):
        """Test that last_name can be set"""
        self.assertEqual(self.user.last_name, "Roe")

    def test_email_value(self):
        """Test that email can be set"""
        self.assertEqual(self.user.email, "a@b.com")

    def test_password_value(self):
        """Test that password can be set"""
        self.assertEqual(self.user.password, "password")

    def test_user_instance_in_storage(self):
        """Test that the User instance is stored in the database"""
        storage.new(self.user)
        storage.save()
        key = "User." + self.user.id
        self.assertIn(key, storage.all())

    def test_user_retrieval_by_id(self):
        """Test retrieval of the user from storage by its ID"""
        storage.new(self.user)
        storage.save()
        user_from_storage = storage.all().get("User." + self.user.id)
        self.assertIsNotNone(user_from_storage)

    def test_user_retrieved_has_correct_id(self):
        """Test that the retrieved user's ID matches the original ID"""
        storage.new(self.user)
        storage.save()
        user_from_storage = storage.all().get("User." + self.user.id)
        self.assertEqual(user_from_storage.id, self.user.id)

    def test_user_retrieved_has_correct_first_name(self):
        """Test that the retrieved user's
        first_name matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.first_name, "John")

    def test_user_retrieved_has_correct_last_name(self):
        """Test that the retrieved user's
        last_name matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.last_name, "Roe")

    def test_user_retrieved_has_correct_email(self):
        """Test that the retrieved user's email matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.email, "a@b.com")

    def test_user_retrieved_has_correct_password(self):
        """Test that the retrieved user's
        password matches the expected value"""
        user = storage.all().get("User." + self.user.id)
        self.assertEqual(user.password, "password")


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        if storage_type == 'db':
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, "")

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        if storage_type == 'db':
            self.assertEqual(user.password, None)
        else:
            self.assertEqual(user.password, "")

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        if storage_type == 'db':
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        if storage_type == 'db':
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user = User()
        string = "[User] ({}) {}".format(user.id, user.to_dict())
        self.assertEqual(string, str(user))


if __name__ == '__main__':
    unittest.main()
