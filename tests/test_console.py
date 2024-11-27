#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import pep8
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage, storage_type
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Prepare the test environment."""
        self.console = HBNBCommand()
        self.console.prompt = '(hbnb) '

    def tearDown(self):
        """Clean up after tests."""
        storage.all().clear()

    def test_prompt(self):
        """Test prompt initialization."""
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_quit(self):
        """Test the quit command."""
        self.assertTrue(self.console.do_quit(""))

    def test_do_EOF(self):
        """Test the EOF command."""
        with self.assertRaises(SystemExit):
            self.console.do_EOF("")  # This should raise SystemExit

    @unittest.skipIf(storage_type == 'db', 'BaseModel not used in DBStorage')
    def test_do_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_create("BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(output)  # Expect an ID to be printed

    @unittest.skipIf(storage_type == 'db', 'BaseModel not used in DBStorage')
    def test_do_all(self):
        """Test the all command."""
        bm1 = BaseModel()
        bm1.save()
        bm2 = BaseModel()
        bm2.save()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.do_all("")
            output = fake_out.getvalue().strip()
            self.assertIn(bm1.id, output)
            self.assertIn(bm2.id, output)


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


if __name__ == '__main__':
    unittest.main()
