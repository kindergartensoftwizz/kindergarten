# Generated by Django 2.0 on 2020-04-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidsapp', '0002_auto_20200410_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]
