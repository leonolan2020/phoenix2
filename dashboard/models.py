import os
from .apps import APP_NAME
from .enums import *
from .settings import ADMIN_URL, MEDIA_URL, STATIC_URL
from utility.persian import PersianCalendar
from django.db import models
from django.http import Http404, HttpResponse
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from tinymce import models as tinymce_models
IMAGE_FOLDER = APP_NAME+'/images/'


class Icon(models.Model):
    icon_title = models.CharField(_("عنوان آیکون"), max_length=50)
    icon_class = models.CharField(
        _("کلاس آیکون"), max_length=50, null=True, blank=True)
    image_origin = models.ImageField(_("تصویر آیکون"), upload_to=IMAGE_FOLDER+'OurService/',
                                     height_field=None, null=True, blank=True, width_field=None, max_length=None)
    icon_fa = models.CharField(
        _("آیکون فونت آسوم"), max_length=50, null=True, blank=True)
    icon_material = models.CharField(
        _("آیکون متریال"), choices=IconsEnum.choices, null=True, blank=True, max_length=100)
    icon_svg = models.TextField(_("آیکون svg"), null=True, blank=True)
    color = models.CharField(_("رنگ آیکون"), choices=ColorEnum.choices,
                             default=ColorEnum.SECONDARY, max_length=50)
    width = models.IntegerField(_("عرض آیکون"), null=True, blank=True)
    height = models.IntegerField(_("ارتفاع آیکون"), null=True, blank=True)
    
    def get_icon_tag(self, icon_style='', color=None):
        if color is None:
            self.color = self.color
        else:
            self.color = color
        if self.image_origin is not None and self.image_origin:
            return f'<img src="{MEDIA_URL}{str(self.image_origin)}" alt="{self.title}" height="{self.height}" width="{self.width}">'
        if self.icon_material is not None and len(self.icon_material) > 0:
            return f'<i style="{icon_style}" class="text-{self.color} material-icons">{self.icon_material}</i>'
        if self.icon_fa is not None and len(self.icon_fa) > 0:
            return f'<i   style="{icon_style}" style="position:inherit !important;" class="text-{self.color} {self.icon_fa}"></i>'
        if self.icon_svg is not None and len(self.icon_svg) > 0:
            return f'<span  style="{icon_style}" class="text-{self.color}">{self.icon_svg}</span>'




    def get_icon_tag_pure(self,icon_style=''):
        
        if self.image_origin is not None and self.image_origin:
            return f'<img src="{MEDIA_URL}{str(self.image_origin)}" alt="{self.title}" height="{self.height}" width="{self.width}">'
        if self.icon_material is not None and len(self.icon_material) > 0:
            return f'<i style="{icon_style}" class=" material-icons">{self.icon_material}</i>'
        if self.icon_fa is not None and len(self.icon_fa) > 0:
            return f'<i   style="{icon_style}" class="{self.icon_fa}"></i>'
        if self.icon_svg is not None and len(self.icon_svg) > 0:
            return f'<span  style="{icon_style}" class="">{self.icon_svg}</span>'


    class Meta:
        verbose_name = _("Icon")
        verbose_name_plural = _("آیکون ها")

    def __str__(self):
        return self.icon_title

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/icon/{self.pk}/change/'

    def image(self):
        if self.image_origin is None:
            return None
        return MEDIA_URL+str(self.image_origin)

    def __unicode__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse("OurService_detail", kwargs={"pk": self.pk})


class Jumbotron(models.Model):
    title = models.CharField(_("عنوان"), max_length=500, blank=True, null=True)
    pretitle = models.CharField(
        _("پیش عنوان"), max_length=500, blank=True, null=True)
    posttitle = models.CharField(
        _("پس عنوان"), max_length=500, blank=True, null=True)
    short_description = tinymce_models.HTMLField(
        _("شرح کوتاه"), max_length=1000, blank=True, null=True)
    description = tinymce_models.HTMLField(
        _("شرح کامل"), max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'Jumbotron({self.pk}) - {self.title}'

    class Meta:
        verbose_name = 'Jumbotron'
        verbose_name_plural = 'Jumbotrons'


class Card(models.Model):
    color = models.CharField(
        _("رنگ"), choices=ColorEnum.choices, default=ColorEnum.PRIMARY, max_length=50)
    icon = models.ForeignKey(
        "icon", null=True, blank=True, on_delete=models.SET_NULL)
    jumbotron = models.ForeignKey(
        "Jumbotron", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'card({self.pk})'

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class CountDownItem(models.Model):
    title = models.CharField(_("Title"), max_length=500, blank=True, null=True)
    pretitle = models.CharField(
        _("Pre Title"), max_length=500, blank=True, null=True)
    for_home = models.BooleanField(_("نمایش در صفحه اصلی"), default=False)
    image_origin = models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'CountDownItem/',
                                     null=True, blank=True, height_field=None, width_field=None, max_length=None)
    counter = models.IntegerField(_("شمارنده"), default=100)
    priority = models.IntegerField(_("ترتیب"), default=100)

    class Meta:
        verbose_name = _("CountDownItem")
        verbose_name_plural = _("شمارنده ها")

    def image(self):
        if self.image_origin:
            return MEDIA_URL+str(self.image_origin)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.title

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/coundownitem/{self.pk}/change/'


class Page(models.Model):
    image_origin = models.ImageField(_("تصویر"), null=True, blank=True, upload_to=IMAGE_FOLDER +
                                     'Page/Main/', height_field=None, width_field=None, max_length=None)
    header_image_origin = models.ImageField(_("تصویر سربرگ"), null=True, blank=True,
                                            upload_to=IMAGE_FOLDER+'Page/Header/', height_field=None, width_field=None, max_length=None)
    thumbnail_origin = models.ImageField(_("تصویر کوچک"), null=True, blank=True, upload_to=IMAGE_FOLDER +
                                         'Page/Thumbnail/', height_field=None, width_field=None, max_length=None)

    title = models.CharField(_('title'), max_length=200)
    icon = models.ForeignKey("icon", null=True, blank=True, on_delete=models.SET_NULL)
    color = models.CharField(_("color class"), blank=True, null=True,
                             choices=ColorEnum.choices, default=ColorEnum.PRIMARY, max_length=50)

    # category=models.CharField(_("دسته بندی"),null=True,blank=True,max_length=100)

    short_description = models.CharField(
        _("شرح کوتاه"), max_length=1000, blank=True, null=True)
    description = tinymce_models.HTMLField(
        _("شرح کامل"), max_length=100000, null=True, blank=True)
    child_class = models.CharField(
        _('child_class'), null=True, blank=True, max_length=50)
    app_name=models.CharField(_('app_name'),null=True,blank=True,max_length=50)
    date_added = models.DateTimeField(
        _('date_added'), null=True, blank=True, auto_now=False, auto_now_add=True)
    archive = models.BooleanField(_("بایگانی شود؟"), default=False)
    for_home = models.BooleanField(
        _("در صفحه اصلی نمایش داده شود؟"), default=False)
    priority = models.IntegerField(_('ترتیب'), default=100)

    profile = models.ForeignKey("authentication.profile", verbose_name=_(
        "profile"), null=True, blank=True, on_delete=models.SET_NULL)

    links = models.ManyToManyField(
        "Link", related_name="pages", verbose_name=_("لینک ها"), blank=True)
    tags = models.ManyToManyField(
        "Tag", related_name="pages", verbose_name=_("برچسب ها"), blank=True)
    documents = models.ManyToManyField(
        "Document", related_name="pages", verbose_name=_("دانلود ها"), blank=True)
    comments = models.ManyToManyField(
        "Comment", related_name="page_for_comment", verbose_name=_("نطر ها"), blank=True)

    images = models.ManyToManyField(
        "GalleryPhoto", related_name="pages", verbose_name=_("تصویر ها"), blank=True)
    related_pages = models.ManyToManyField(
        "Page", verbose_name=_("صفحه های مرتبط"), blank=True)

    def image(self):
        if self.image_origin:
            return MEDIA_URL+str(self.image_origin)
        
        else:
            return STATIC_URL+f'/dashboard/img/pages/{self.child_class}.jpg'

    def thumbnail(self):
        if self.thumbnail_origin:
            return MEDIA_URL+str(self.thumbnail_origin)
        else:
            return STATIC_URL+f'/dashboard/img/pages/{self.child_class}.jpg'

    def header_image(self):
        if self.header_image_origin:
            return MEDIA_URL+str(self.header_image_origin)
        else:
            return STATIC_URL+f'/dashboard/img/pages/{self.child_class}.jpg'

    def __str__(self):
        return f'page({self.pk}) - {self.title}'

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def get_app_url(self):
        return reverse('app:'+self.child_class, kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse(self.app_name+':'+self.child_class, kwargs={'pk': self.pk})

    def persian_date_added_tag(self):
        value = self.date_added
        a = PersianCalendar().from_gregorian(value)
        return f"""
        <span  title="{value.strftime("%Y/%m/%d %H:%M:%S") }" class="text-secondary">
            <small>
                {str(a)}
            </small>   
        </span>
        """


class Document(Icon):
    title = models.CharField(_('عنوان'), max_length=200)
    priority = models.IntegerField(_('ترتیب'), default=100)
    profile = models.ForeignKey("authentication.Profile", verbose_name=_(
        "پروفایل"), on_delete=models.CASCADE)
    file = models.FileField(_("فایل ضمیمه"), null=True, blank=True,
                            upload_to=APP_NAME+'/Document', max_length=100)

    def get_link(self):
        return f"""

            <a href="{self.get_download_url()}">
            {self.get_icon_tag()}
            {self.title}</a>
        """

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("اسناد")

    def get_download_url(self):
        if self.file:
            return reverse('dashboard:download', kwargs={'document_id': self.pk})
        else:
            return ''

    def download(self):
        #STATIC_ROOT2 = os.path.join(BASE_DIR, STATIC_ROOT)
        file_path = str(self.file.path)
        # print(file_path)
        # return JsonResponse({'download:':str(file_path)})
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(
                    fh.read(), content_type="application/force-download")
                response['Content-Disposition'] = 'inline; filename=' + \
                    os.path.basename(file_path)
                return response
        raise Http404

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("dashboard:document", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/document/{self.pk}/change/'


class Region(models.Model):
    name = models.CharField(_("name"), max_length=50,
                            choices=RegionEnum.choices, default=RegionEnum.KHAF)
    priority = models.IntegerField(_("ترتیب"), default=100)

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("منطقه ها")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Region_detail", kwargs={"pk": self.pk})


class Notification(models.Model):
    profile = models.ForeignKey("authentication.Profile", verbose_name=_(
        "پروفایل"), on_delete=models.CASCADE)
    title = models.CharField(_("عنوان"), max_length=50)
    body = models.CharField(
        _("توضیحات"), max_length=500, null=True, blank=True)
    url = models.CharField(_("url"), max_length=1100, blank=True, null=True)
    seen = models.BooleanField(_('دیده شد'), default=False)
    priority = models.IntegerField(_("اولویت"), default=1000)
    date_added = models.DateTimeField(
        _('تاریخ ایجاد'), auto_now_add=True, auto_now=False)
    date_seen = models.DateTimeField(
        _('تاریخ دیده شده'), auto_now_add=False, auto_now=False, null=True, blank=True)

    color = models.CharField(
        _("رنگ"), choices=ColorEnum.choices, default=ColorEnum.PRIMARY, max_length=50)

    icon = models.ForeignKey(
        "icon", null=True, blank=True, on_delete=models.SET_NULL)

    # def send(self,user,channel_name,event_name):
    #     try:
    #           PusherChannelEventRepo(user=user).get(channel_name,event_name).send_message(

    #         {
    #             'body':self.body,
    #             'title':self.title,
    #             'color':self.color,
    #             'icon':self.icon,
    #             'link':self.link,
    #             'get_absolute_url':self.get_absolute_url(),
    #         }

    #         )
    #     except expression as identifier:
    #         pass

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("اعلان ها")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(APP_NAME+":notification", kwargs={"pk": self.pk})


class ProfileCustomization(models.Model):
    profile = models.ForeignKey(
        "authentication.profile", verbose_name="پروفایل", on_delete=models.CASCADE)
    sidebar_bg_color = models.CharField(
        _('sidebar_bg_color'), default='rose', max_length=50)
    sidebar_bg_image = models.CharField(
        _('sidebar_bg_image'), null=True, blank=True, max_length=50)
    sidebar_active_color = models.CharField(
        _('sidebar_active_color'), default='black', max_length=50)

    class Meta:
        verbose_name = _("ProfileCustomization")
        verbose_name_plural = _("سفارشی سازی پروفایل ها")

    def set_value(self, line_key, line_value):
        if line_key == 'sidebar_bg_color':
            self.sidebar_bg_color = line_value
        if line_key == 'sidebar_bg_image':
            self.sidebar_bg_image = line_value
        if line_key == 'sidebar_active_color':
            self.sidebar_active_color = line_value
        self.save()

    def __str__(self):
        return self.profile.name()


class Comment(models.Model):
    profile = models.ForeignKey("authentication.Profile", null=True,
                                blank=True, verbose_name=_("توسط"), on_delete=models.CASCADE)
    text = models.TextField(_("نظر"))
    date_added = models.DateTimeField(
        _("تاریخ"), auto_now=False, auto_now_add=True)
    replys = models.ManyToManyField(
        "Comment", verbose_name=_("پاسخ ها"), blank=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("نظرات کاربران")

    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)

    def __str__(self):
        name = '' if self.profile is None else self.profile.name()
        return f'{name} @ {self.text}'

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/blog/{self.pk}/change/'

    def get_absolute_url(self):
        return reverse("app:blog", kwargs={"blog_id": self.pk})

    def profile_name(self):
        return self.profile.name()

    def profile_get_absolute_url(self):
        return self.profile.get_absolute_url()

    def profile_image(self):
        return self.profile.image()

    def profile_id(self):
        return self.profile.pk

    def persian_date_added_tag(self):
        value = self.date_added
        a = PersianCalendar().from_gregorian(value)
        return f'<a href="#" title="{value.strftime("%Y/%m/%d %H:%M:%S") }">{str(a)}</a>'


class Like(models.Model):
    profile = models.ForeignKey("authentication.Profile", null=True,
                                blank=True, verbose_name=_("توسط"), on_delete=models.CASCADE)
    date_added = models.DateTimeField(
        _("تاریخ"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("لایک های کاربران")

    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)

    def __str__(self):
        name = '' if self.profile is None else self.profile.name()
        return f'{name} @ {self.persian_date_added()}'


class OurWorkCategory(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    priority = models.IntegerField(_("ترتیب"), default=100)
    image_header = models.ImageField(_("تصویر سربرگ"), null=True, blank=True, upload_to=IMAGE_FOLDER +
                                     'OurWorkCategory/', height_field=None, width_field=None, max_length=None)

    def image(self):
        if self.image_header is None:
            return None
        return MEDIA_URL+str(self.image_header)

    def to_link_tag(self):
        return """
        <a href="{get_absolute_url}" class="leo-farsi tag-cloud-link">
             
                {get_icon_tag}
            
              {title}</a>
          """.format(get_absolute_url=tag.get_absolute_url(), get_icon_tag=tag.icon.get_icon_tag(), title=tag.title)

    class Meta:
        verbose_name = _("دسته بندی  پروژه")
        verbose_name_plural = _("دسته بندی  پروژه ها")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:our_works_by_category', kwargs={'category_id': self.pk})

    def get_edit_url(self):
        return f'{ADMIN_URL}app/ourworkcategory/{self.pk}/change/'


class Color(models.Model):
    name = models.CharField(_('نام رنگ'), max_length=50)
    color = models.CharField(_('کد رنگ'), max_length=50)

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("رنگ ها")

    def __str__(self):
        return self.name


class ResumeCategory(models.Model):
    profile = models.ForeignKey("authentication.profile", verbose_name=_(
        "profile"), on_delete=models.CASCADE)
    title = models.CharField(_("title"), choices=ResumeCategoryEnum.choices,
                             default=ResumeCategoryEnum.EDUCATION, max_length=50)
    resumes = models.ManyToManyField("Resume", verbose_name=_("resume"))
    priority = models.IntegerField(_("priority"), default=100)
    icon = models.ForeignKey("Icon", verbose_name='icon',
                             on_delete=models.SET_NULL, null=True, blank=True)

    def get_icon_tag(self):
        if self.icon is not None:
            return self.icon.get_icon_tag(color='--')
        return f"""
               <i class="material-icons">palette</i>
            """

    class Meta:
        verbose_name = _("ResumeCategory")
        verbose_name_plural = _("دسته بندی رزومه")

    def __str__(self):
        return f'{self.profile.name()} -> {self.title}'

    def get_absolute_url(self):
        return reverse("ResumeCategory_detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return (f'{ADMIN_URL}{APP_NAME}/resumecategory/{self.pk}/change')


class GalleryAlbum(Jumbotron):
    image_origin = models.ImageField(_("Big Image 345*970 "), upload_to=IMAGE_FOLDER+'Gallery/Album/',
                                     null=True, blank=True, height_field=None, width_field=None, max_length=None)
    for_home = models.BooleanField(_("Show on homepage"), default=False)
    archive = models.BooleanField(_("Archive?"), default=False)
    priority = models.IntegerField(_("Priority"), default=100)
    thumbnail_origin = models.ImageField(_("Thumbnail Image"), upload_to=IMAGE_FOLDER+'Gallery/Album/Thumbnail/',
                                         null=True, blank=True, height_field=None, width_field=None, max_length=None)

    photos = models.ManyToManyField(
        "GalleryPhoto", verbose_name=_("Photos"), blank=True)

    def get_tag(self):
        s = """<div class="row rtl mb-3">"""
        for pic in self.photos.all():
            s += f"""<div class="col-lg-3">
            <a target="_blank" href="{pic.image()}"><img src="{pic.image()}" width="100%"></a>
            </div>"""
        s += "</div>"
        return s

    def image(self):
        return MEDIA_URL+str(self.image_origin)

    def thumbnail(self):
        return MEDIA_URL+str(self.thumbnail_origin)

    class Meta:
        verbose_name = _("GalleryAlbum")
        verbose_name_plural = _("آلبوم های تصاویر")

    def __str__(self):
        return self.title

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/galleryalbum/{self.pk}/change/'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("OurService_detail", kwargs={"pk": self.pk})


class GalleryPhoto(models.Model):
    image_title = models.CharField(
        _("عنوان تصویر"), max_length=100, null=True, blank=True)
    image_description = models.CharField(
        _("شرح تصویر"), max_length=500, null=True, blank=True)
    thumbnail_origin = models.ImageField(_("Thumbnail Image"), upload_to=IMAGE_FOLDER+'Gallery/Photo/Thumbnail/',
                                         null=True, blank=True, height_field=None, width_field=None, max_length=None)
    image_origin = models.ImageField(_("Big Image 345*970 "), upload_to=IMAGE_FOLDER +
                                     'Gallery/Photo/', height_field=None, width_field=None, max_length=None)
    archive = models.BooleanField(_("Archive?"), default=False)
    priority = models.IntegerField(_("Priority"), default=100)
    location = models.CharField(
        _("موقعیت مکانی تصویر"), max_length=50, null=True, blank=True)
    profile = models.ForeignKey("authentication.profile", null=True,
                                blank=True, verbose_name=_("پروفایل"), on_delete=models.SET_NULL)
    date_added = models.DateTimeField(
        _("افزوده شده در"), auto_now=False, auto_now_add=True)

    def image(self):
        return MEDIA_URL+str(self.image_origin)

    def thumbnail(self):
        if self.thumbnail_origin:
            return MEDIA_URL+str(self.thumbnail_origin)
        else:
            return self.image()#STATIC_URL+'material/img/Pattern-Randomized.svg'

    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)

    class Meta:
        verbose_name = _("GalleryPhoto")
        verbose_name_plural = _("تصاویر")

    def __str__(self):
        return 'image ('+str(self.pk)+')'

    def get_absolute_url(self):
        return MEDIA_URL+str(self.image_origin)

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/galleryphoto/{self.pk}/change/'

# the classes above will be derived in another modules


class MetaData(models.Model):
    for_home = models.BooleanField(_("نمایش در صفحه اصلی"), default=False)
    key = models.CharField(_("key name"), max_length=50, default='name')
    value = models.CharField(
        _("key value"), max_length=50, default='description')
    content = models.CharField(_("content"), max_length=2000)

    class Meta:
        verbose_name = _("MetaData")
        verbose_name_plural = _("متا دیتا - کلمات کلیدی سئو")

    def __str__(self):
        return ('*** ' if self.for_home else '')+f'{self.key} : {self.value}: {self.content[:20]}'


class MainPic(models.Model):
    name = models.CharField(_("جای تصویر"), max_length=50,
                            choices=MainPicEnum.choices)
    image_origin = models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'MainPic/',
                                     height_field=None, width_field=None, max_length=None, null=True, blank=True)

    def get_edit_btn(self):
        return f"""
            <a class="" href="{self.get_edit_url()}">
            <i class="material-icons">settings</i>
            ویرایش تصویر
            </a>
        """

    class Meta:
        verbose_name = _("MainPic")
        verbose_name_plural = _("تصویر های اصلی سایت")

    def image(self):
        if self.image_origin and self.image_origin is not None:
            return f'{MEDIA_URL}{str(self.image_origin)}'
        return None

    def __str__(self):
        return self.name


class Parameter(models.Model):

    name = models.CharField(_("نام"), max_length=50,
                            choices=ParametersEnum.choices)
    value = models.CharField(_("مقدار"), max_length=10000)

    def get_edit_btn(self):
        return f"""
         <a target="_blank" title="ویرایش {self.name}" class="btn btn-info btn-link" href="{self.get_edit_url()}">
                            <i class="material-icons">settings</i>
                        </a>
        """

    class Meta:
        verbose_name = _("Parameter")
        verbose_name_plural = _("پارامتر ها")

    def __str__(self):
        return f'{self.name} : {self.value}'

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/parameter/{self.pk}/change/'

class ContactMessage(models.Model):
    full_name = models.CharField(_("نام کامل"), max_length=50)
    mobile = models.CharField(_("شماره تماس"), max_length=50)
    email = models.EmailField(_("ایمیل"), max_length=254)
    subject = models.CharField(_("عنوان پیام"), max_length=50)
    message = models.CharField(_("متن پیام"), max_length=50)
    date_added = models.DateTimeField(
        _("افزوده شده در"), auto_now=False, auto_now_add=True)
    app_name = models.CharField(_("اپلیکیشن"), max_length=50)

    class Meta:
        verbose_name = _("ContactMessage")
        verbose_name_plural = _("پیام های ارتباط با ما")

    def __str__(self):
        return self.email+"   @  "+PersianCalendar().from_gregorian(self.date_added)


class FAQ(models.Model):
    for_home = models.BooleanField(_("نمایش در صفحه خانه"), default=False)
    color = models.CharField(
        _("رنگ"), choices=ColorEnum.choices, default=ColorEnum.PRIMARY, max_length=50)

    icon = models.ForeignKey(
        "icon", null=True, blank=True, on_delete=models.SET_NULL)
    priority = models.IntegerField(_("ترتیب"))
    question = models.CharField(_("سوال"), max_length=200)
    answer = models.CharField(_("پاسخ"), max_length=5000)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("پرسش های متداول")

    def __str__(self):
        return self.question

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/faq/{self.pk}/change/'

    def get_absolute_url(self):
        return reverse("app:faq")


class Blog(Page):

    def save(self):
        self.child_class = 'blog'
        super(Blog, self).save()

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("مقالات")

    def __str__(self):
        return self.title


class Technology(Page):

    def save(self):
        self.child_class = 'technology'
        super(Technology, self).save()

    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("تکنولوژی")

    def __str__(self):
        if self.title:
            return self.title
        return str(self.priority)


class Link(Icon):
    title = models.CharField(_("عنوان"), max_length=200)
    for_home = models.BooleanField(
        _("نمایش در پایین صفحه سایت"), default=False)
    for_nav = models.BooleanField(_("نمایش در منوی بالای سایت"), default=False)
    priority = models.IntegerField(_("ترتیب"), default=100)
    url = models.CharField(_("لینک"), max_length=2000, default="#")
    profile_adder = models.ForeignKey(
        "authentication.Profile", verbose_name=_("پروفایل"), on_delete=models.CASCADE)

    def get_link(self):
        return f"""

            <a target="_blank" href="{self.url}">
            {self.get_icon_tag()}
            {self.title}</a>
        """

    def get_link_icon_tag(self):
        if self.url:
            icon = self.get_icon_tag()
            return f'<a title="{self.title}" href="{self.url}">{icon}</a>'
        else:
            return self.get_icon_tag()

    def to_link_tag(self):
        return """
          <a class="btn  btn-round btn-block btn-{color}" href="{url}">
          <i class="material-icons">{icon}</i>
          {title}</a>
        """.format(color=self.color, icon=self.icon, url=self.url, title=self.title)

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("لینک ها")

    def __str__(self):
        return self.title+('*' if self.for_home else '')


class OurTeam(models.Model):
    profile = models.ForeignKey("authentication.Profile", verbose_name=_(
        "پروفایل"), on_delete=models.CASCADE)
    job = models.CharField(_("سمت"), max_length=100)
    description = models.CharField(_("توضیحات"), max_length=500)
    priority = models.IntegerField(_("ترتیب"), default=1000)
    social_links = models.ManyToManyField(
        "SocialLink", verbose_name=_("social_links"), blank=True)
    resume_categories = models.ManyToManyField(
        "ResumeCategory", verbose_name=_("ResumeCategories"), blank=True)

    def __str__(self):
        return self.profile.name()

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'OurTeam'
        managed = True
        verbose_name = 'OurTeam'
        verbose_name_plural = 'تیم ما'


class HomeSlider(models.Model):
    image_banner = models.ImageField(_("تصویر اسلایدر  1333*2000 "), upload_to=IMAGE_FOLDER +
                                     'Banner/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(_("عنوان"), null=True, blank=True, max_length=500)
    body = models.TextField(_("بدنه"), null=True, blank=True, max_length=2000)
    text_color = models.CharField(_("رنگ متن"), default="#fff", max_length=20)

    priority = models.IntegerField(_("ترتیب"), default=100)
    archive = models.BooleanField(_("بایگانی شود؟"), default=False)
    tag_number = models.IntegerField(_("عدد برچسب"), default=100)
    tag_text = models.CharField(
        _("متن برچسب"), max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = _("HomeSlider")
        verbose_name_plural = _("اسلایدر های صفحه اصلی")

    def image(self):
        return MEDIA_URL+str(self.image_banner)

    def __str__(self):
        return str(self.priority)


class OurWork(Page):
    category = models.ForeignKey("OurWorkCategory", null=True, blank=True, verbose_name=_(
        "دسته بندی"), on_delete=models.SET_NULL)
    location = models.CharField(
        _('موقعیت در نقشه گوگل 400*400'), max_length=500, null=True, blank=True)

    def save(self):
        self.child_class = 'ourwork'
        super(OurWork, self).save()

    class Meta:
        verbose_name = _("OurWork")
        verbose_name_plural = _("پروژه ها")

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    for_home = models.BooleanField(_("نمایش در صفحه خانه"), default=False)
    image_origin = models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'Testimonial/',
                                     null=True, blank=True, height_field=None, width_field=None, max_length=None)
    title = models.CharField(_("عنوان"), max_length=2000)
    body = models.CharField(_("متن"), max_length=2000, null=True, blank=True)
    footer = models.CharField(_("پانوشت"), max_length=200)
    priority = models.IntegerField(_("ترتیب"), default=100)
    profile = models.ForeignKey("authentication.Profile", null=True,
                                blank=True, verbose_name=_("profile"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("گفته های مشتریان")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/testimonial/{self.pk}/change/'


class Feature(Page):

    def save(self):
        self.child_class = 'feature'
        super(Feature, self).save()

    def get_icon_tag(self):
        if self.thumbnail_origin is not None and self.thumbnail_origin:
            return f'<img src="{MEDIA_URL}{str(self.thumbnail_origin)}" alt="{self.title}" height="{self.height}" width="{self.width}">'
        if self.icon_material is not None and len(self.icon_material) > 0:
            return f'<i class="text-{self.color} material-icons">{self.icon_material}</i>'
        if self.icon_fa is not None and len(self.icon_fa) > 0:
            return f'<span class="text-{self.color} {self.icon_fa}"></span>'
        if self.icon_svg is not None and len(self.icon_svg) > 0:
            return f'<span class="text-{self.color}">{self.icon_svg}</span>'
        return None

    def get_tag(self):
        icon = self.get_icon_tag()
        if icon and icon is not None:
            return f'<a title="{self.title}" href="{self.get_absolute_url()}">{icon}</a>'
        return None

    class Meta:
        verbose_name = _("OurService")
        verbose_name_plural = _("خدمات و سرویس ها")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Resume(Page):
    start_date = models.DateTimeField(
        _("start_date"), null=True, blank=True, auto_now=False, auto_now_add=False)
    end_date = models.DateTimeField(
        _("end_date"), null=True, blank=True, auto_now=False, auto_now_add=False)
    duration = models.CharField(
        _("مدت زمان"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("رزومه")

    def save(self):
        self.child_class = 'resume'
        super(Resume, self).save()

    def get_icon_tag(self):
        if self.icon is not None:
            return self.icon.get_icon_tag()
        return f"""
               <i class="material-icons">palette</i>
            """
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/resume/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(f'{self.app_name}:resume',kwargs={'pk':self.pk})
      
class Tag(models.Model):
    priority = models.IntegerField(_("ترتیب"), default=100)
    image_header = models.ImageField(_("تصویر سربرگ"), null=True, blank=True,
                                     upload_to=IMAGE_FOLDER+'Tag/', height_field=None, width_field=None, max_length=None)
    title = models.CharField(_("عنوان"), max_length=50)
    icon = models.ForeignKey("Icon", verbose_name=_(
        "آیکون"), null=True, blank=True, on_delete=models.SET_NULL)

    def get_link(self):
        return f"""

            <a class="btn btn-link btn-info"  href="{self.get_absolute_url()}">
            {self.icon.get_icon_tag() if self.icon else ''}
            {self.title}</a>
        """

    def header_image(self):
        if self.image_header is None or not self.image_header:
            return STATIC_URL+'dashboard/img/tag.jpg'
        return MEDIA_URL+str(self.image_header)

    def get_inner_link(self):
        return f"""

            {self.icon.get_icon_tag()}
            {self.title}
        """

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("برچسب ها")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:tag', kwargs={'pk': self.pk})

    def get_projectmanager_url(self):
        return reverse('projectmanager:tag', kwargs={'pk': self.pk})

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/tag/{self.pk}/change/'

    def get_edit_btn(self):
        return f"""
            <a href="{self.get_edit_url()}" title="ویرایش">
            <i class="material-icons">settings</i>
            </a>
        """


class SocialLink(Link):
    app_name=models.CharField(_('اپلیکیشن'),max_length=50,null=True,blank=True)
    profile = models.ForeignKey("authentication.Profile", null=True,
                                blank=True, verbose_name=_("profile"), on_delete=models.PROTECT)

    def get_link(self):
        return f"""
                <a href="{self.url}" class="btn btn-just-icon btn-link {self.icon_class}">
                {self.get_icon_tag()}
                </a>
        """

    class Meta:
        verbose_name = _("SocialLink")
        verbose_name_plural = _("شبکه اجتماعی")

    def __str__(self):
        return self.icon_title
