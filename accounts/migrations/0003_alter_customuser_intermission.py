# Generated by Django 5.0 on 2024-10-22 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_intermission_customuser_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='intermission',
            field=models.URLField(blank=True),
        ),
    ]