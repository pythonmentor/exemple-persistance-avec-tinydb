"""Module responsable de créer la connexion à la base de données."""

from tinydb import TinyDB

db = TinyDB('db.json')