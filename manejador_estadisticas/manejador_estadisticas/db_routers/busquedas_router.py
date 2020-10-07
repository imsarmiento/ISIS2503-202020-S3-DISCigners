class ContenidoRouter:
    def db_for_read(self, model, **hints):
        """
        Lee de la base de datos busquedas
        """
        if model._meta.app_label is 'manejador_contenido':
            return 'busquedas_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Escribe la base de datos busquedas
        """
        if model._meta.app_label is 'manejador_contenido':
            return 'busquedas_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite todo tipo de relaciones
        """
        if (
            obj1._meta.app_label is 'manejador_busquedas' or
            obj2._meta.app_label is 'manejador_busquedas'
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Permite migraciones de busquedas
        """
        if model._meta.app_label is 'manejador_busquedas':
            return db is 'busquedas_db'
        return None