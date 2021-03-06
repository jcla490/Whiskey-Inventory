# Generated by Django 2.2.5 on 2019-11-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiskey_list', '0002_spirit_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spirit',
            name='brand',
            field=models.CharField(blank=True, max_length=255, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='spirit',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='spirit',
            name='release',
            field=models.CharField(blank=True, max_length=255, verbose_name='Release Name'),
        ),
        migrations.AlterField(
            model_name='spirit',
            name='whiskey_type',
            field=models.CharField(choices=[('AMW', 'American Whiskey'), ('AMR', 'American Rye'), ('BOU', 'Bourbon Whiskey'), ('CAN', 'Canadian Whisky/Rye'), ('RUM', 'Rum')], default='BOU', max_length=3),
        ),
    ]
