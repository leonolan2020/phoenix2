# Generated by Django 3.1.2 on 2020-11-06 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Blog', serialize=False, to='dashboard.blog')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'default_related_name': 'app_Blog',
            },
            bases=('dashboard.blog',),
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('contactmessage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Technology', serialize=False, to='dashboard.contactmessage')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
                'default_related_name': 'app_Technology',
            },
            bases=('dashboard.contactmessage',),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('feature_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Feature', serialize=False, to='dashboard.feature')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
                'default_related_name': 'app_Feature',
            },
            bases=('dashboard.feature',),
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('homeslider_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_HomeSlider', serialize=False, to='dashboard.homeslider')),
            ],
            options={
                'verbose_name': 'HomeSlider',
                'verbose_name_plural': 'HomeSliders',
                'default_related_name': 'app_HomeSlider',
            },
            bases=('dashboard.homeslider',),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('link_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Link', serialize=False, to='dashboard.link')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
                'default_related_name': 'app_Link',
            },
            bases=('dashboard.link',),
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('mainpic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_MainPic', serialize=False, to='dashboard.mainpic')),
            ],
            options={
                'verbose_name': 'MainPic',
                'verbose_name_plural': 'MainPics',
                'default_related_name': 'app_MainPic',
            },
            bases=('dashboard.mainpic',),
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('metadata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_MetaData', serialize=False, to='dashboard.metadata')),
            ],
            options={
                'verbose_name': 'MetaData',
                'verbose_name_plural': 'MetaDatas',
                'default_related_name': 'app_MetaData',
            },
            bases=('dashboard.metadata',),
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('ourteam_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_OurTeam', serialize=False, to='dashboard.ourteam')),
            ],
            options={
                'verbose_name': 'OurTeam',
                'verbose_name_plural': 'OurTeams',
                'default_related_name': 'app_OurTeam',
            },
            bases=('dashboard.ourteam',),
        ),
        migrations.CreateModel(
            name='OurWork',
            fields=[
                ('ourwork_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_OurWork', serialize=False, to='dashboard.ourwork')),
            ],
            options={
                'verbose_name': 'OurWork',
                'verbose_name_plural': 'OurWorks',
                'default_related_name': 'app_OurWork',
            },
            bases=('dashboard.ourwork',),
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('parameter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Parameter', serialize=False, to='dashboard.parameter')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'Parameters',
                'default_related_name': 'app_Parameter',
            },
            bases=('dashboard.parameter',),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('resume_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Resume', serialize=False, to='dashboard.resume')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
                'default_related_name': 'app_Resume',
            },
            bases=('dashboard.resume',),
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('technology_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='app_Technology', serialize=False, to='dashboard.technology')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
                'default_related_name': 'app_Technology',
            },
            bases=('dashboard.technology',),
        ),
    ]
