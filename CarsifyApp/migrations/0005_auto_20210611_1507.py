# Generated by Django 3.2.2 on 2021-06-11 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarsifyApp', '0004_auto_20210611_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='Address_Typee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CarsifyApp.address_type'),
        ),
    ]
