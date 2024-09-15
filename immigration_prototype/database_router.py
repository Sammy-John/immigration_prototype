class CRMRouter:
    """
    A router to control all database operations on models in the CRM app.
    """
    route_app_labels = {'crm'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read CRM models go to crm_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'crm_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write CRM models go to crm_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'crm_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that CRM app only appears in the 'crm_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'crm_db'
        return None
