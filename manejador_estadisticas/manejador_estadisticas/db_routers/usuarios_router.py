class UsuariosRouter:
    """
    A router to control all database operations on models in the
    usuarios applications.
    """
    route_app_labels = {'manejador_usuarios'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read usuarios and contenttypes models go to usuarios_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'usuarios'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write usuarios and contenttypes models go to usuarios.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'usuarios'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the manejador usuarios apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None
        # return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the manejador usuarios only appear in the
        'usuarios' database.
        """
        if app_label in self.route_app_labels:
            return db == 'usuarios'
        return None
