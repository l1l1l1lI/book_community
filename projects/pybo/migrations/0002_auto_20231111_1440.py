# Generated by Django 3.1.3 on 2023-11-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Number_of_volumes',
            new_name='Number_of_pages',
        ),
        migrations.AlterField(
            model_name='book',
            name='subject',
            field=models.TextField(),
        ),
    ]
