# Generated by Django 5.1.2 on 2024-11-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cronofy', '0009_cronofyuser_delete_calendlyuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronofyuser',
            name='sub',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
