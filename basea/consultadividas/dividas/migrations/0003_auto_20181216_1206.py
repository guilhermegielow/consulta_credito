# Generated by Django 2.1.4 on 2018-12-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividas', '0002_auto_20181216_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divida',
            name='documento',
            field=models.CharField(max_length=20),
        ),
    ]
