# Generated by Django 3.1.4 on 2021-01-25 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210125_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tiitle',
            new_name='title',
        ),
    ]
