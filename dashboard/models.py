from django.db import models
from .settings import ADMIN_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
from tinymce import models as tinymce_models
from .settings import MEDIA_URL
IMAGE_FOLDER=APP_NAME+'/images/'
class Notification(models.Model):
    name=models.CharField(_("نام"),max_length=50)
    country=models.CharField(_("کشور"),max_length=50)
    city=models.CharField(_("شهر"),max_length=50)
    salary=models.IntegerField(_("حقوق"))
    def __str__(self):
        return f'{self.country} - {self.name}'
    def get_color(self):
        if self.salary>10000:
            return 'table-success'
        if self.salary>8000:
            return 'table-info'
        if self.salary>6000:
            return 'table-warning'
        if self.salary>4000:
            return 'table-secondary'
        if self.salary>2000:
            return 'table-danger'
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/notification/{self.pk}/change/'


class Icon(models.Model):
    icon_title=models.CharField(_("عنوان"), max_length=50)    
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'OurService/', height_field=None,null=True,blank=True, width_field=None, max_length=None)
    icon_fa=models.CharField(_("آیکون فونت آسوم"),max_length=50,null=True,blank=True)
    icon_material=models.CharField(_("آیکون متریال"),choices=IconsEnum.choices,null=True,blank=True, max_length=100)
    icon_svg=models.TextField(_("آیکون svg"),null=True,blank=True)
    color=models.CharField(_("رنگ"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    width=models.IntegerField(_("عرض"),default=128)
    height=models.IntegerField(_("ارتفاع"),default=128)
    def get_icon_tag(self):
        if self.image_origin is not None and self.image_origin:
            return f'<img src="{MEDIA_URL}{str(self.image_origin)}" alt="{self.title}" height="{self.height}" width="{self.width}">'
        if self.icon_material is not None and len(self.icon_material)>0:
            return f'<i class="text-{self.color} material-icons">{self.icon_material}</i>'
        if self.icon_fa is not None and len(self.icon_fa)>0:
            return f'<i   style="position:inherit !important;" class="text-{self.color} {self.icon_fa}"></i>'
        if self.icon_svg is not None and len(self.icon_svg)>0:
            return f'<span class="text-{self.color}">{self.icon_svg}</span>'
    
      
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





class Color(models.Model):
    color_name=models.CharField(_("color name"),max_length=50)
    color_code=models.CharField(_("color code"),blank=True,null=True,max_length=50)
    color_class=models.CharField(_("color class"),blank=True,null=True,choices=ColorEnum.choices,default=ColorEnum.DEFAULT,max_length=50)
    def __str__(self):
        return f'color({self.color_name})'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
class Jumbotron(models.Model):
    title=models.CharField(_("عنوان"), max_length=500,blank=True,null=True)
    pretitle=models.CharField(_("پیش عنوان"), max_length=500,blank=True,null=True)
    posttitle=models.CharField(_("پس عنوان"), max_length=500,blank=True,null=True)
    short_description=tinymce_models.HTMLField(_("شرح کوتاه"),max_length=1000,blank=True,null=True)
    description=tinymce_models.HTMLField(_("شرح کامل"),max_length=2000,null=True,blank=True)

    def __str__(self):
        return f'Jumbotron({self.pk}) - {self.title}'

    class Meta:
        verbose_name = 'Jumbotron'
        verbose_name_plural = 'Jumbotrons'

class Card(models.Model):
    color=models.ForeignKey("Color",null=True,blank=True,on_delete=models.SET_NULL)
    icon=models.ForeignKey("icon",null=True,blank=True,on_delete=models.SET_NULL)
    jumbotron=models.ForeignKey("Jumbotron",null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return f'card({self.pk})'

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

