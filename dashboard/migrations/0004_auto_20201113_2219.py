# Generated by Django 3.1.2 on 2020-11-13 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20201108_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ourwork',
            name='category',
        ),
        migrations.AddField(
            model_name='page',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.ourworkcategory', verbose_name='دسته بندی'),
        ),
    ]