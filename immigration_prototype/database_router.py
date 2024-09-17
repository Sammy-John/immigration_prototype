class MultiDBRouter:
    """
    A router to control all database operations for multiple apps.
    """
    route_app_labels = {'crm', 'auth_app', 'cms'}

    def db_for_read(self, model, **hints):
        """
        Directs read operations for models to the appropriate database.
        """
        if model._meta.app_label == 'crm':
            return 'crm_db'
        elif model._meta.app_label == 'auth_app':
            return 'default'
        elif model._meta.app_label == 'cms':
            return 'cms_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Directs write operations for models to the appropriate database.
        """
        if model._meta.app_label == 'crm':
            return 'crm_db'
        elif model._meta.app_label == 'auth_app':
            return 'default'
        elif model._meta.app_label == 'cms':
            return 'cms_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensures that apps only appear in their designated databases.
        """
        if app_label == 'crm':
            return db == 'crm_db'
        elif app_label == 'auth_app':
            return db == 'default'
        elif app_label == 'cms':
            return db == 'cms_db'
        return None
