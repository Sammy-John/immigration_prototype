# Generated by Django 5.1.1 on 2024-09-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='lead',
            name='created_by_id',
            field=models.IntegerField(blank=True, help_text='ID of the user who created the lead.', null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='updated_by_id',
            field=models.IntegerField(blank=True, editable=False, help_text='ID of the user who last updated the lead.', null=True),
        ),
    ]
