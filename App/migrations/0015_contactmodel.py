# Generated by Django 3.0.5 on 2020-04-23 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_usersmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('ContactId', models.AutoField(primary_key=True, serialize=False)),
                ('ContactName', models.CharField(default='Name', max_length=100)),
                ('ContactMsg', models.TextField(default='Message', max_length=3000)),
                ('MarkTime', models.IntegerField(default=0, max_length=2)),
            ],
        ),
    ]
