# Generated by Django 4.2.9 on 2025-04-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_porfile_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(blank=True, default='base_image.png', upload_to=''),
        ),
    ]
