# Generated by Django 5.0 on 2024-10-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singerqueue', '0002_contactinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='social_types',
            field=models.CharField(choices=[('', 'Please pick social contact type'), ('tiktok', 'TikTok'), ('X', 'X'), ('facebook', 'Facebook'), ('instagram', 'Instagram'), ('phone_number', 'Phone Number'), ('email', 'Email'), ('n/a', 'N/A')], default='', max_length=12),
        ),
    ]
