# Generated by Django 3.1.2 on 2020-10-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_link_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.GalleryPhoto', verbose_name='تصویر ها'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='color',
            field=models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='secondary', max_length=50, verbose_name='رنگ آیکون'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='height',
            field=models.IntegerField(blank=True, null=True, verbose_name='ارتفاع آیکون'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='icon_title',
            field=models.CharField(max_length=50, verbose_name='عنوان آیکون'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='image_origin',
            field=models.ImageField(blank=True, null=True, upload_to='dashboard/images/OurService/', verbose_name='تصویر آیکون'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name='عرض آیکون'),
        ),
    ]