# Generated by Django 3.1.1 on 2020-09-24 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0002_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
