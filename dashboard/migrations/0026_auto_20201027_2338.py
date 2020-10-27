# Generated by Django 3.1.2 on 2020-10-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_profilecustomization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilecustomization',
            name='menu_active_color',
        ),
        migrations.RemoveField(
            model_name='profilecustomization',
            name='menu_bg_color',
        ),
        migrations.RemoveField(
            model_name='profilecustomization',
            name='menu_bg_image',
        ),
        migrations.AddField(
            model_name='profilecustomization',
            name='sidebar_active_color',
            field=models.CharField(default='black', max_length=50, verbose_name='sidebar_active_color'),
        ),
        migrations.AddField(
            model_name='profilecustomization',
            name='sidebar_bg_color',
            field=models.CharField(default='rose', max_length=50, verbose_name='sidebar_bg_color'),
        ),
        migrations.AddField(
            model_name='profilecustomization',
            name='sidebar_bg_image',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='sidebar_bg_image'),
        ),
    ]
