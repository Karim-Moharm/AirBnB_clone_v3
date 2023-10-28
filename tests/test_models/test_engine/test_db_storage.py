#!/usr/bin/python3
"""Module for file_storage test Cases
"""
from models.engine import db_storage
import unittest
from models.all_models import our_models


class TestFileStorage(unittest.TestCase):
    """test cases for FileStorage class
    """

    def test_module_documetation(self):
        """test the documentation of a module
        """
        self.assertTrue(len(db_storage.__doc__) > 0)

    def test_class_documetation(self):
        """test the documentation of class
        """
        self.assertTrue(len(db_storage.DBStorage.__doc__) > 0)

    def test_method_documetation(self):
        """test documentation of methods inside and outside class
        """
        for method in dir(db_storage):
            self.assertTrue(len(method.__doc__) > 0)

    def test_private_attrs_1(self):
        file_attr = db_storage.DBStorage.__file_path
        self.assertRaises(AttributeError, file_attr)

    def test_private_attrs(self):
        storage = db_storage.DBStorage()

        with self.assertRaises(AttributeError):
            _ = storage.__engine

        with self.assertRaises(AttributeError):
            _ = storage.__session

    def test_all_method(self):
        """test the return type of all method
        """
        f = db_storage.DBStorage()
        self.assertEqual(type(f.all()), dict)

    # def test_new(self):
    #     user = our_models["User"]()
    #     self.storage.new(user)
    #     self.assertIn(f'{user.__class__.__name__}.{user.id}',
    #                   self.storage.all())
