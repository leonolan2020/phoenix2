# Generated by Django 3.1.2 on 2020-11-07 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='app_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='app_name'),
        ),
    ]