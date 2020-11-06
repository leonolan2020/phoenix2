# Generated by Django 3.1.2 on 2020-11-06 18:50

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام رنگ')),
                ('color', models.CharField(max_length=50, verbose_name='کد رنگ')),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='نام کامل')),
                ('mobile', models.CharField(max_length=50, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('subject', models.CharField(max_length=50, verbose_name='عنوان پیام')),
                ('message', models.CharField(max_length=50, verbose_name='متن پیام')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='افزوده شده در')),
                ('app_name', models.CharField(max_length=50, verbose_name='اپلیکیشن')),
            ],
            options={
                'verbose_name': 'ContactMessage',
                'verbose_name_plural': 'پیام های ارتباط با ما',
            },
        ),
        migrations.CreateModel(
            name='CountDownItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title')),
                ('pretitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='Pre Title')),
                ('for_home', models.BooleanField(default=False, verbose_name='نمایش در صفحه اصلی')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/CountDownItem/', verbose_name='تصویر')),
                ('counter', models.IntegerField(default=100, verbose_name='شمارنده')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'CountDownItem',
                'verbose_name_plural': 'شمارنده ها',
            },
        ),
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='عنوان تصویر')),
                ('image_description', models.CharField(blank=True, max_length=500, null=True, verbose_name='شرح تصویر')),
                ('thumbnail_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Gallery/Photo/Thumbnail/', verbose_name='Thumbnail Image')),
                ('image_origin', models.ImageField(upload_to='dashboard/images/Gallery/Photo/', verbose_name='Big Image 345*970 ')),
                ('archive', models.BooleanField(default=False, verbose_name='Archive?')),
                ('priority', models.IntegerField(default=100, verbose_name='Priority')),
                ('location', models.CharField(blank=True, max_length=50, null=True, verbose_name='موقعیت مکانی تصویر')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='افزوده شده در')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'GalleryPhoto',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner', models.ImageField(upload_to='dashboard/images/Banner/', verbose_name='تصویر اسلایدر  1333*2000 ')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='عنوان')),
                ('body', models.TextField(blank=True, max_length=2000, null=True, verbose_name='بدنه')),
                ('text_color', models.CharField(default='#fff', max_length=20, verbose_name='رنگ متن')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('archive', models.BooleanField(default=False, verbose_name='بایگانی شود؟')),
                ('tag_number', models.IntegerField(default=100, verbose_name='عدد برچسب')),
                ('tag_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن برچسب')),
            ],
            options={
                'verbose_name': 'HomeSlider',
                'verbose_name_plural': 'اسلایدر های صفحه اصلی',
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon_title', models.CharField(max_length=50, verbose_name='عنوان آیکون')),
                ('icon_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='کلاس آیکون')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/OurService/', verbose_name='تصویر آیکون')),
                ('icon_fa', models.CharField(blank=True, max_length=50, null=True, verbose_name='آیکون فونت آسوم')),
                ('icon_material', models.CharField(blank=True, choices=[('engineering', 'engineering'), ('account_circle', 'account_circle'), ('add_shopping_cart', 'add_shopping_cart'), ('apartment', 'apartment'), ('alarm', 'alarm'), ('attach_file', 'attach_file'), ('attach_money', 'attach_money'), ('backup', 'backup'), ('build', 'build'), ('card_travel', 'card_travel'), ('chat', 'chat'), ('construction', 'construction'), ('dashboard', 'dashboard'), ('delete', 'delete'), ('description', 'description'), ('extension', 'extension'), ('face', 'face'), ('favorite', 'favorite'), ('fingerprint', 'fingerprint'), ('get_app', 'get_app'), ('help_outline', 'help_outline'), ('home', 'home'), ('important_devices', 'important_devices'), ('link', 'link'), ('local_shipping', 'local_shipping'), ('lock', 'lock'), ('mail', 'mail'), ('notification_important', 'notification_important'), ('place', 'place'), ('psychology', 'psychology'), ('publish', 'publish'), ('reply', 'reply'), ('schedule', 'schedule'), ('send', 'send'), ('settings', 'settings'), ('share', 'share'), ('sync', 'sync'), ('verified_user', 'verified_user'), ('vpn_key', 'vpn_key'), ('weekend', 'weekend')], max_length=100, null=True, verbose_name='آیکون متریال')),
                ('icon_svg', models.TextField(blank=True, null=True, verbose_name='آیکون svg')),
                ('color', models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='secondary', max_length=50, verbose_name='رنگ آیکون')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='عرض آیکون')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='ارتفاع آیکون')),
            ],
            options={
                'verbose_name': 'Icon',
                'verbose_name_plural': 'آیکون ها',
            },
        ),
        migrations.CreateModel(
            name='Jumbotron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='عنوان')),
                ('pretitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='پیش عنوان')),
                ('posttitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='پس عنوان')),
                ('short_description', tinymce.models.HTMLField(blank=True, max_length=1000, null=True, verbose_name='شرح کوتاه')),
                ('description', tinymce.models.HTMLField(blank=True, max_length=2000, null=True, verbose_name='شرح کامل')),
            ],
            options={
                'verbose_name': 'Jumbotron',
                'verbose_name_plural': 'Jumbotrons',
            },
        ),
        migrations.CreateModel(
            name='MainPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('آیکون سایت', 'آیکون سایت'), ('سایت', 'سایت'), ('سوالات', 'سوالات'), ('جستجو', 'جستجو'), ('ویدیو', 'ویدیو'), ('درباره ما', 'درباره ما'), ('سربرگ ارتباط با ما', 'سربرگ ارتباط با ما'), ('لودینگ', 'لودینگ'), ('لوگو', 'لوگو'), ('لوگوی بزرگ', 'لوگوی بزرگ'), ('لوگوی تیره', 'لوگوی تیره'), ('لوگوی روشن', 'لوگوی روشن'), ('سربرگ مقاله', 'سربرگ مقاله'), ('سربرگ پروژه', 'سربرگ پروژه'), ('سربرگ پیش فرض برای صفحات', 'سربرگ پیش فرض برای صفحات'), ('سربرگ درباره ما', 'سربرگ درباره ما'), ('سربرگ برچسب', 'سربرگ برچسب')], max_length=50, verbose_name='جای تصویر')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/MainPic/', verbose_name='تصویر')),
            ],
            options={
                'verbose_name': 'MainPic',
                'verbose_name_plural': 'تصویر های اصلی سایت',
            },
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_home', models.BooleanField(default=False, verbose_name='نمایش در صفحه اصلی')),
                ('key', models.CharField(default='name', max_length=50, verbose_name='key name')),
                ('value', models.CharField(default='description', max_length=50, verbose_name='key value')),
                ('content', models.CharField(max_length=2000, verbose_name='content')),
            ],
            options={
                'verbose_name': 'MetaData',
                'verbose_name_plural': 'متا دیتا - کلمات کلیدی سئو',
            },
        ),
        migrations.CreateModel(
            name='OurWorkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('image_header', models.ImageField(blank=True, null=True, upload_to='dashboard/images/OurWorkCategory/', verbose_name='تصویر سربرگ')),
            ],
            options={
                'verbose_name': 'دسته بندی  پروژه',
                'verbose_name_plural': 'دسته بندی  پروژه ها',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Page/Main/', verbose_name='تصویر')),
                ('header_image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Page/Header/', verbose_name='تصویر سربرگ')),
                ('thumbnail_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Page/Thumbnail/', verbose_name='تصویر کوچک')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('color', models.CharField(blank=True, choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='DEFAULT', max_length=50, null=True, verbose_name='color class')),
                ('short_description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='شرح کوتاه')),
                ('description', tinymce.models.HTMLField(blank=True, max_length=10000, null=True, verbose_name='شرح کامل')),
                ('child_class', models.CharField(blank=True, max_length=50, null=True, verbose_name='child_class')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date_added')),
                ('archive', models.BooleanField(default=False, verbose_name='بایگانی شود؟')),
                ('for_home', models.BooleanField(default=False, verbose_name='در صفحه اصلی نمایش داده شود؟')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon')),
                ('images', models.ManyToManyField(blank=True, related_name='pages', to='dashboard.GalleryPhoto', verbose_name='تصویر ها')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.profile', verbose_name='profile')),
                ('related_pages', models.ManyToManyField(blank=True, to='dashboard.Page', verbose_name='صفحه های مرتبط')),
            ],
            options={
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('درباره ما کامل', 'درباره ما کامل'), ('درباره ما کوتاه', 'درباره ما کوتاه'), ('عنوان درباره ما', 'عنوان درباره ما'), ('آدرس', 'آدرس'), ('واحد پول', 'واحد پول'), ('ارتباط با ما', 'ارتباط با ما'), ('پیام درخواست نامعتبر', 'پیام درخواست نامعتبر'), ('ایمیل', 'ایمیل'), ('فکس', 'فکس'), ('تگ سرچ گوگل', 'تگ سرچ گوگل'), ('موقعیت در گوگل مپ', 'موقعیت در گوگل مپ'), ('موبایل', 'موبایل'), ('رنگ زمینه منوی بالای سایت', 'رنگ زمینه منوی بالای سایت'), ('رنگ متن منوی بالای سایت', 'رنگ متن منوی بالای سایت'), ('لینک تیم ما', 'لینک تیم ما'), ('عنوان تیم ما', 'عنوان تیم ما'), ('کد پستی', 'کد پستی'), ('پیش عنوان', 'پیش عنوان'), ('شرح کوتاه', 'شرح کوتاه'), ('تلفن', 'تلفن'), ('قوانین', 'قوانین'), ('رنگ سربرگ کروم در موبایل', 'رنگ سربرگ کروم در موبایل'), ('عنوان', 'عنوان'), ('لینک', 'لینک'), ('لینک ویدیو', 'لینک ویدیو'), ('عنوان ویدیو', 'عنوان ویدیو')], max_length=50, verbose_name='نام')),
                ('value', models.CharField(max_length=10000, verbose_name='مقدار')),
            ],
            options={
                'verbose_name': 'Parameter',
                'verbose_name_plural': 'پارامتر ها',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('خواف', 'خواف'), ('نشتیفان', 'نشتیفان'), ('سنگان', 'سنگان'), ('قاسم آباد', 'قاسم آباد'), ('تایباد', 'تایباد'), ('تربت جام', 'تربت جام'), ('فریمان', 'فریمان'), ('مشهد', 'مشهد'), ('تهران', 'تهران'), ('تربت حیدریه', 'تربت حیدریه')], default='خواف', max_length=50, verbose_name='name')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'منطقه ها',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.page')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'مقالات',
            },
            bases=('dashboard.page',),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('icon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.icon')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('file', models.FileField(blank=True, null=True, upload_to='dashboard/Document', verbose_name='فایل ضمیمه')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'اسناد',
            },
            bases=('dashboard.icon',),
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.page')),
            ],
            options={
                'verbose_name': 'OurService',
                'verbose_name_plural': 'خدمات و سرویس ها',
            },
            bases=('dashboard.page',),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('icon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.icon')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('for_home', models.BooleanField(default=False, verbose_name='نمایش در پایین صفحه سایت')),
                ('for_nav', models.BooleanField(default=False, verbose_name='نمایش در منوی بالای سایت')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('url', models.CharField(default='#', max_length=2000, verbose_name='لینک')),
                ('profile_adder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'لینک ها',
            },
            bases=('dashboard.icon',),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.page')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='start_date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='end_date')),
                ('duration', models.CharField(blank=True, max_length=50, null=True, verbose_name='مدت زمان')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'رزومه',
            },
            bases=('dashboard.page',),
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.page')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'تکنولوژی',
            },
            bases=('dashboard.page',),
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_home', models.BooleanField(default=False, verbose_name='نمایش در صفحه خانه')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Testimonial/', verbose_name='تصویر')),
                ('title', models.CharField(max_length=2000, verbose_name='عنوان')),
                ('body', models.CharField(blank=True, max_length=2000, null=True, verbose_name='متن')),
                ('footer', models.CharField(max_length=200, verbose_name='پانوشت')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='authentication.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'گفته های مشتریان',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('image_header', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Tag/', verbose_name='تصویر سربرگ')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon', verbose_name='آیکون')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
        migrations.CreateModel(
            name='ResumeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('تجربه ها', 'تجربه ها'), ('آموزش ها', 'آموزش ها'), ('مهارت ها', 'مهارت ها'), ('علاقه ها', 'علاقه ها'), ('گواهینامه ها', 'گواهینامه ها'), ('جایزه ها', 'جایزه ها'), ('کار های انجام شده', 'کار های انجام شده')], default='آموزش ها', max_length=50, verbose_name='title')),
                ('priority', models.IntegerField(default=100, verbose_name='priority')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon', verbose_name='icon')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='profile')),
                ('resumes', models.ManyToManyField(to='dashboard.Resume', verbose_name='resume')),
            ],
            options={
                'verbose_name': 'ResumeCategory',
                'verbose_name_plural': 'دسته بندی رزومه',
            },
        ),
        migrations.CreateModel(
            name='ProfileCustomization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sidebar_bg_color', models.CharField(default='rose', max_length=50, verbose_name='sidebar_bg_color')),
                ('sidebar_bg_image', models.CharField(blank=True, max_length=50, null=True, verbose_name='sidebar_bg_image')),
                ('sidebar_active_color', models.CharField(default='black', max_length=50, verbose_name='sidebar_active_color')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'ProfileCustomization',
                'verbose_name_plural': 'سفارشی سازی پروفایل ها',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.Tag', verbose_name='برچسب ها'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('body', models.CharField(blank=True, max_length=500, null=True, verbose_name='توضیحات')),
                ('url', models.CharField(blank=True, max_length=1100, null=True, verbose_name='url')),
                ('seen', models.BooleanField(default=False, verbose_name='دیده شد')),
                ('priority', models.IntegerField(default=1000, verbose_name='اولویت')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('date_seen', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ دیده شده')),
                ('color', models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='UNSET', max_length=50, verbose_name='رنگ')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'اعلان ها',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='توسط')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'لایک های کاربران',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_home', models.BooleanField(default=False, verbose_name='نمایش در صفحه خانه')),
                ('color', models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='UNSET', max_length=50, verbose_name='رنگ')),
                ('priority', models.IntegerField(verbose_name='ترتیب')),
                ('question', models.CharField(max_length=200, verbose_name='سوال')),
                ('answer', models.CharField(max_length=5000, verbose_name='پاسخ')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'پرسش های متداول',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='نظر')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='توسط')),
                ('replys', models.ManyToManyField(blank=True, to='dashboard.Comment', verbose_name='پاسخ ها')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'نظرات کاربران',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('success', 'success'), ('danger', 'danger'), ('warning', 'warning'), ('primary', 'primary'), ('secondary', 'secondary'), ('info', 'info'), ('light', 'light'), ('dark', 'dark'), ('rose', 'rose'), ('DEFAULT', 'DEFAULT'), ('UNSET', 'UNSET')], default='UNSET', max_length=50, verbose_name='رنگ')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.icon')),
                ('jumbotron', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.jumbotron')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.Document', verbose_name='دانلود ها'),
        ),
        migrations.AddField(
            model_name='page',
            name='links',
            field=models.ManyToManyField(blank=True, related_name='pages', to='dashboard.Link', verbose_name='لینک ها'),
        ),
        migrations.CreateModel(
            name='OurWork',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.page')),
                ('location', models.CharField(blank=True, max_length=500, null=True, verbose_name='موقعیت در نقشه گوگل 400*400')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.ourworkcategory', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'OurWork',
                'verbose_name_plural': 'پروژه ها',
            },
            bases=('dashboard.page',),
        ),
        migrations.CreateModel(
            name='GalleryAlbum',
            fields=[
                ('jumbotron_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.jumbotron')),
                ('image_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Gallery/Album/', verbose_name='Big Image 345*970 ')),
                ('for_home', models.BooleanField(default=False, verbose_name='Show on homepage')),
                ('archive', models.BooleanField(default=False, verbose_name='Archive?')),
                ('priority', models.IntegerField(default=100, verbose_name='Priority')),
                ('thumbnail_origin', models.ImageField(blank=True, null=True, upload_to='dashboard/images/Gallery/Album/Thumbnail/', verbose_name='Thumbnail Image')),
                ('photos', models.ManyToManyField(blank=True, to='dashboard.GalleryPhoto', verbose_name='Photos')),
            ],
            options={
                'verbose_name': 'GalleryAlbum',
                'verbose_name_plural': 'آلبوم های تصاویر',
            },
            bases=('dashboard.jumbotron',),
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('link_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.link')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='authentication.profile', verbose_name='profile')),
            ],
            options={
                'verbose_name': 'SocialLink',
                'verbose_name_plural': 'شبکه اجتماعی',
            },
            bases=('dashboard.link',),
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=100, verbose_name='سمت')),
                ('description', models.CharField(max_length=500, verbose_name='توضیحات')),
                ('priority', models.IntegerField(default=1000, verbose_name='ترتیب')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.profile', verbose_name='پروفایل')),
                ('resume_categories', models.ManyToManyField(blank=True, to='dashboard.ResumeCategory', verbose_name='ResumeCategories')),
                ('social_links', models.ManyToManyField(blank=True, to='dashboard.SocialLink', verbose_name='social_links')),
            ],
            options={
                'verbose_name': 'OurTeam',
                'verbose_name_plural': 'تیم ما',
                'db_table': 'OurTeam',
                'managed': True,
            },
        ),
    ]
