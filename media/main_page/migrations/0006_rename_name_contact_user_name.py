# Generated by Django 3.2 on 2021-08-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='user_name',
        ),
    ]
