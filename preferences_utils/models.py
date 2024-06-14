from django.db import models


class PreferencesUtilsModel(models.Model):
    __subclasses__ = {}

    @classmethod
    def register(cls, name):
        """ Decorator to register a subclass 
            We can have multiple subclasses, so we keeps track of them
        """
        if cls.__name__ != "PreferencesUtilsModel":
            raise Exception("You can only register subclasses of PreferencesUtilsModel")

        def wrapper(subcls):
            cls.__subclasses__[name] = subcls
            return subcls

        return wrapper

    @classmethod
    def instance(cls, name=""):
        """
        If called from a specific subclass name is not required,
        if called from the base class, the name is required
        """
        if name == "" and not hasattr(cls, "objects"):
            raise Exception(
                "You must specify the subclass name if called from the base class"
            )

        kls = cls if name == "" else cls.__subclasses__[name]
        item = kls.objects.first()
        if not item:
            item = kls(id=1)
            item.save()
        return item

    def save(self, *args, **kwargs):
        """ Assure to save only one instance """
        self.id = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.__class__.__name__

    class Meta:
        abstract = True
