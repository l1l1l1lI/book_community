# Generated by Django 3.1.3 on 2023-11-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_auto_20231111_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_name',
            field=models.TextField(null=True),
        ),
    ]
