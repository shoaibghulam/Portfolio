# Generated by Django 3.0.5 on 2020-04-22 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20200423_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='Serviceid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.ServiceModel'),
        ),
    ]
