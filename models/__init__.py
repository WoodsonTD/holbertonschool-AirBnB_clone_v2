#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
<<<<<<< HEAD


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

=======


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
>>>>>>> 37029cd23383498458d955c4ff36c3c6b16528f0
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
