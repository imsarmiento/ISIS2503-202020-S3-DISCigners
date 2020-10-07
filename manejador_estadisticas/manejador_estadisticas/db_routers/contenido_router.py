class ContenidoRouter:
    def db_for_read(self, model, **hints):
        """
        Lee de la base de datos contenido
        """
        if model._meta.app_label is 'manejador_contenido':
            return 'contenido_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Escribe la base de datos contenido
        """
        if model._meta.app_label is 'manejador_contenido':
            return 'contenido_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite todo tipo de relaciones
        """
        if (
            obj1._meta.app_label is 'manejador_contenido' or
            obj2._meta.app_label is 'manejador_contenido'
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Permite migraciones de contenido
        """
        if model._meta.app_label is 'manejador_contenido':
            return db is 'contenido_db'
        return None