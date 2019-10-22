# Generated by Django 2.2.6 on 2019-10-21 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_auto_20191021_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField(max_length=500)),
                ('ratings', models.IntegerField(max_length=5)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='users.UsersProfile')),
            ],
        ),
    ]
