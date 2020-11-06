# Generated by Django 3.1.2 on 2020-11-06 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='نام')),
                ('last_name', models.CharField(max_length=200, verbose_name='نام خانوادگی')),
                ('status', models.CharField(choices=[('فعال', 'فعال'), ('غیر فعال', 'غیر فعال')], default='فعال', max_length=50, verbose_name='وضعیت')),
                ('mobile', models.CharField(blank=True, max_length=50, null=True, verbose_name='موبایل')),
                ('slogan', models.CharField(blank=True, max_length=200, null=True, verbose_name='جمله کوتاه')),
                ('bio', models.CharField(blank=True, max_length=500, null=True, verbose_name='درباره')),
                ('image_origin', models.ImageField(blank=True, max_length=1200, null=True, upload_to='authentication/images/Profile/', verbose_name='تصویر')),
                ('image_header_origin', models.ImageField(blank=True, max_length=1200, null=True, upload_to='authentication/images/Profile/header/', verbose_name='تصویر سربرگ')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='آدرس')),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='کد پستی')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'پروفایل ها',
            },
        ),
    ]
