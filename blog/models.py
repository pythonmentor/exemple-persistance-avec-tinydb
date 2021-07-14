"""Module responsable de définir les modèles de l'application."""

from . import managers


class ModelType(type):
    """Metaclasse permettant de déduire automatiquement le nom du manager et de
    l'instancier sous le nom de l'attribut objects."""

    def __init__(cls, name, bases, attributes):
        """Initialise une nouvelle classe de modèle."""
        cls.objets = None
        if name != "Model":
            manager_name = getattr(cls, "manager_name", name + "Manager")
            manager = getattr(managers, manager_name, None)
            # On instancie le manager s'il existe
            cls.objects = manager(cls) if manager else None


class Model(metaclass=ModelType):
    """Classe de base pour tous les modèles."""

    def __eq__(self, other):
        """Implémentation par défaut de la notion d'égalité."""
        if hasattr(self, "id"):
            return self.id == other
        return self is other

    def to_dict(self):
        """Transforme l'instance courante en dictionnaire."""
        return vars(self)

    def save(self):
        cls = type(self)
        if hasattr(cls, "objects") and cls.objects is not None:
            cls.objects.save(self)


class User(Model):
    """Représente un utilisateur du blog."""

    def __init__(self, id=None, first_name=None, name=None, email=None):
        """Initialise un nouvel utilisateur."""
        self.id = id
        self.first_name = first_name
        self.name = name
        self.email = email
        self.articles = []

    def to_dict(self):
        data = super().to_dict()
        data["articles"] = [article.id for article in self.articles]

    def from_dict(cls, dictionary):
        articles = dictionary.get("articles")


class Article(Model):
    """Représente un article publié dans le blog."""

    def __init__(self, id=None, title=None, content=None, authors=None, tags=None):
        """Initialise un nouvel article en vue de sa publication."""
        self.id = id
        self.title = title
        self.content = content
        self.authors = authors or []
        self.tags = tags or []


class Tag(Model):
    """Représente une étiquette utilisée pour taguer un article."""

    def __init__(self, id=None, name=None, *args, **kwargs):
        """Initialise une nouvelle étiquette."""
        self.id = id
        self.name = name
        self.articles = []


class Comment(Model):
    """Représente un commentaire ajouté à un article du blog."""

    def __init__(self, id=None, author=None, content=None):
        self.id = id
        self.author = author
        self.content = content
