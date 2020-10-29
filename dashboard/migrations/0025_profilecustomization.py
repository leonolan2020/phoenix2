# Generated by Django 3.1.2 on 2020-10-27 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('dashboard', '0024_auto_20201027_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileCustomization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_bg_color', models.CharField(max_length=50, verbose_name='menu_bg_color')),
                ('menu_bg_image', models.CharField(max_length=50, verbose_name='menu_bg_image')),
                ('menu_active_color', models.CharField(max_length=50, verbose_name='menu_active_color')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'ProfileCustomization',
                'verbose_name_plural': 'سفارشی سازی پروفایل ها',
            },
        ),
    ]