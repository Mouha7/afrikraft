# Generated by Django 4.2.13 on 2024-06-04 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user_id',
        ),
    ]
