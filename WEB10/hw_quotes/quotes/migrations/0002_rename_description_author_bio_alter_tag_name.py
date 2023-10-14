# Generated by Django 4.2.6 on 2023-10-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='description',
            new_name='bio',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True),
        ),
    ]