# Generated by Django 3.1.2 on 2020-11-06 00:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.page')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectmanager.managerpage', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
            bases=('dashboard.page',),
        ),
        migrations.CreateModel(
            name='ArchiveDocument',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'ArchiveDocument',
                'verbose_name_plural': 'اسناد آرشیوی',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'Contractor',
                'verbose_name_plural': 'Contractors',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('event_date', models.DateTimeField(verbose_name='event_date')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='OrganizationUnit',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'OrganizationUnit',
                'verbose_name_plural': 'OrganizationUnits',
            },
            bases=('projectmanager.managerpage',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
                ('percent', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد پیشرفت')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='شروع')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='پایان')),
                ('location', models.TextField(blank=True, null=True, verbose_name='موقعیت در نقشه گوگل مپ')),
                ('contractors', models.ManyToManyField(blank=True, to='projectmanager.Contractor', verbose_name='پیمانکار ها')),
                ('events', models.ManyToManyField(blank=True, to='projectmanager.Event', verbose_name='رویداد ها')),
                ('organization_units', models.ManyToManyField(blank=True, to='projectmanager.OrganizationUnit', verbose_name='واحد های سازمانی')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
            bases=('projectmanager.managerpage',),
        ),
    ]
