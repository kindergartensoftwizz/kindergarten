# Generated by Django 2.0 on 2020-04-10 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kidsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='kinder',
            new_name='contact',
        ),
        migrations.AlterModelTable(
            name='contact',
            table='contact',
        ),
    ]
