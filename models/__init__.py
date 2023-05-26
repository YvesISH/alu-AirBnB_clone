#!/usr/bin/python3
"""
    Initialize and reload the FileStorage engine
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
