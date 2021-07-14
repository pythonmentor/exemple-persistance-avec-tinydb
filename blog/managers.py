"""Module responsable de définir les managers permettant de gérer les tables de
la base de données."""
import re

import requests

from .database import db


class Manager:
    """Classe de base représentant un manager."""

    def __init__(self, model, db=db):
        """Initialise un nouveau manager."""
        cls = type(self)
        self._db = db
        self.model = model
        cls.table_name = getattr(cls, "table_name", self._build_table_name())
        self._table = db.table(self.table_name)

    def save(self, obj):
        """Crée l'objet en base de données s'il n'existe pas ou le mets à jour
        sinon."""

    def _build_table_name(self):
        """Construit le nom de la table à partir du nom du modèle si l'attribut
        de classe table_name n'existe pas."""
        REGEX = r"([A-Z]+(?![^A-Z])|[A-Z]+$|[A-Z][^A-Z]+)"
        cleaned_model_name = self.model.__name__.replace("_", "")
        parts = [part for part in re.split(REGEX, cleaned_model_name) if part]
        return "_".join(parts).lower()


class UserManager(Manager):
    """Représente un gestionnaire permettant la recherche et la sauvegarde
    d'utilisateurs en base de données."""


class ArticleManager(Manager):
    """Représente un gestionnaire permettant la recherche et la sauvegarde
    d'articles en base de données."""


class TagManager(Manager):
    """Représente un gestionnaire permettant la recherche et la sauvegarde
    d'étiquettes en base de données."""


class CommentManager(Manager):
    """Représente un gestionnaire permettant la recherche et la sauvegarde
    d'commentaires en base de données."""
