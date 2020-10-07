import random

class ContenidoRouter:
    def db_for_read(self, model, **hints):
        """
        Lee de la base de datos contenido
        """
        return 'contenido'

    def db_for_write(self, model, **hints):
        """
        Escribe la base de datos contenido
        """
        return 'contenido'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite todo tipo de relaciones
        """
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Permite migraciones de contenido
        """
        return db == 'contenido'