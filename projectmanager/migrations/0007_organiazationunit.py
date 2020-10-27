# Generated by Django 3.1.2 on 2020-10-25 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0006_project_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganiazationUnit',
            fields=[
                ('managerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projectmanager.managerpage')),
            ],
            options={
                'verbose_name': 'OrganiazationUnit',
                'verbose_name_plural': 'OrganiazationUnits',
            },
            bases=('projectmanager.managerpage',),
        ),
    ]