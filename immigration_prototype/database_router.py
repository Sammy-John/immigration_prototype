class CRMRouter:
    """
    A router to control all database operations on models in the CRM app.
    """
    route_app_labels = {'crm'}

    def db_for_read(self, model, **hints):
        """
        Directs read operations for 'crm' models to 'crm_db'.
        Directs read operations for 'auth_app' models to 'default'.
        """
        if model._meta.app_label == 'crm':
            return 'crm_db'
        elif model._meta.app_label == 'auth_app':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Directs write operations for 'crm' models to 'crm_db'.
        Directs write operations for 'auth_app' models to 'default'.
        """
        if model._meta.app_label == 'crm':
            return 'crm_db'
        elif model._meta.app_label == 'auth_app':
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensures that the CRM app only appears in the 'crm_db' database and 'auth_app' in 'default'.
        """
        if app_label == 'crm':
            return db == 'crm_db'
        elif app_label == 'auth_app':
            return db == 'default'
        return None
