# Generated by Django 4.0.6 on 2022-07-17 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0004_alter_posts_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]