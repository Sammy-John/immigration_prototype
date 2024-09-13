from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_app'

    def ready(self):
        from django.contrib.auth.models import Group, Permission
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver

        @receiver(post_migrate)
        def create_user_groups(sender, **kwargs):
            if sender.name == 'auth_app':
                groups_permissions = {
                    'Super Admin': Permission.objects.all(),
                    'Manager': Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user']),
                    'Agents': Permission.objects.filter(codename__in=['view_client', 'edit_client', 'create_content']),
                    'Office': Permission.objects.filter(codename__in=['view_client', 'create_content'])
                }
                for group_name, permissions in groups_permissions.items():
                    group, created = Group.objects.get_or_create(name=group_name)
                    group.permissions.set(permissions)

class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_app'

