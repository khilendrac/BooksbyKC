# Generated by Django 3.1.1 on 2020-09-24 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0004_auto_20200924_1051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
    ]
