# Generated by Django 3.1.2 on 2020-10-25 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20201025_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(default='link_1', max_length=200, verbose_name='عنوان'),
            preserve_default=False,
        ),
    ]