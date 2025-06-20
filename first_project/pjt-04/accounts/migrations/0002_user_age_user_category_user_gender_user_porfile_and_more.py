# Generated by Django 4.2.9 on 2025-04-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(blank=True, max_length=500, verbose_name='카테고리'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', '남성'), ('F', '여성')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='porfile',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='weekly_avg_reading_time',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='yearly_read_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
