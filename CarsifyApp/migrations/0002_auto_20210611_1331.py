# Generated by Django 3.2.2 on 2021-06-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarsifyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Topic',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Yourmessage',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Email',
        ),
        migrations.AddField(
            model_name='contact',
            name='Query',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='Remark',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='State',
            field=models.TextField(null=True),
        ),
    ]