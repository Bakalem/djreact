# Generated by Django 2.1.3 on 2018-12-04 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='titre',
            new_name='title',
        ),
    ]