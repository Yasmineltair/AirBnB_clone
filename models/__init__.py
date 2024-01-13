#!/usr/bin/python3
""" new instance add a call to the method new(self) on storage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
