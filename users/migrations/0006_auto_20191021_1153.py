# Generated by Django 2.2.6 on 2019-10-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191021_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersprofile',
            name='modified_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
