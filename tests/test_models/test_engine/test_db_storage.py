#!/usr/bin/python3
"""This module contains TestDBStorage class"""
from datetime import datetime
from models import storage
import MySQLdb
from models.user import User
from models.amenity import Amenity
import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 'Only run this test when the storage is a database')
class TestDBStorage(unittest.TestCase):
    """This class is for testing DBStorage class attributes and functions"""

    def setUp(self):
        """Setup data before each test method"""

        self.db_connection = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            passwd=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB')
        )

        self.cursor = self.db_connection.cursor()

    def tearDown(self):
        """Excutes data after each test method"""

        self.cursor.close()
        self.db_connection.close()

    def test_new(self):
        """Tests new() function"""

        my_cursor = self.cursor

        user = User(
            email="user@gmail.com",
            password="123456",
            first_name="user",
            last_name="user"
        )
        my_cursor.execute(
            "SELECT * FROM users WHERE id=%s", (user.id,))

        self.assertEqual(my_cursor.rowcount, 0)

        self.assertNotIn(user, storage.all().values())
        user.save()
        self.assertIn(user, storage.all().values())

        self.db_connection.commit()

        my_cursor.execute(
            "SELECT * FROM users WHERE id=%s", (user.id,))

        self.assertEqual(my_cursor.rowcount, 1)
        result = my_cursor.fetchone()
        self.assertTrue(result is not None)
        self.assertIn(user.email, result)
        self.assertIn(user.password, result)

    def test_delete(self):
        """Tests delete method"""

        amenity = Amenity(name="Wifi")

        amenity.save()

        self.assertIn(amenity, storage.all().values())

        amenity.delete()

        self.assertNotIn(amenity, storage.all().values())

    def test_reload(self):
        """ Tests the reloading of the database session """

        my_cursor = self.cursor
        user = User(
            email="user@gmail.com",
            password="123456",
            first_name="user",
            last_name="user"
        )
        my_cursor.execute(
            'INSERT INTO users(id, created_at, updated_at, email, password' +
            ', first_name, last_name) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (user.id, user.created_at, user.updated_at, user.email,
             user.password, user.first_name, user.last_name,
            )
        )
        self.assertNotIn(f'User.{user.id}', storage.all())
        self.db_connection.commit()
        storage.reload()
        self.assertIn(f'User.{user.id}', storage.all())

    def test_save(self):
        """ Tests save method """

        my_cursor = self.cursor

        user = User(
            email='user@gmail.com',
            password='password',
            first_name='user',
            last_name='user'
        )

        my_cursor.execute('SELECT * FROM users WHERE id=%s', (user.id,))
        result = my_cursor.fetchone()
        old_count = my_cursor.rowcount
        self.assertTrue(result is None)
        self.assertFalse(user in storage.all().values())
        user.save()

        self.db_connection.commit()

        my_cursor.execute('SELECT * FROM users WHERE id=%s', (user.id,))
        result = my_cursor.fetchone()

        new_count = my_cursor.rowcount
        self.assertFalse(result is None)
        self.assertEqual(old_count + 1, new_count)
        self.assertIn(f"User.{user.id}", storage.all())

    def test_storage_var_created(self):
        """ DBStorage object storage created """
        from models.engine.db_storage import DBStorage
        self.assertEqual(type(storage), DBStorage)
