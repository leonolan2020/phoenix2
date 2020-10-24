from django.db import models
from django.conf import settings
from .enums import ProfileStatusEnum
from dashboard.constants import FORCE_RESIZE_IMAGE
from .apps import APP_NAME
from dashboard.settings import ADMIN_URL
from django.utils.translation import gettext as _
from django.shortcuts import reverse
from dashboard.settings import MEDIA_URL,STATIC_URL
IMAGE_FOLDER=APP_NAME+'/images/'
class Profile(models.Model):
    # region = models.ForeignKey("Region", verbose_name=_("region"), on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,null=True,blank=True
    )
    first_name = models.CharField(_("نام"), max_length=200)
    last_name = models.CharField(_("نام خانوادگی"), max_length=200)
    status = models.CharField(_("وضعیت"), max_length=50,choices=ProfileStatusEnum.choices,default=ProfileStatusEnum.ENABLED)
    mobile = models.CharField(_("موبایل"), max_length=50,null=True,blank=True)
    slogan=models.CharField(_('جمله کوتاه'),max_length=200,null=True,blank=True)
    bio = models.CharField(_("درباره"), max_length=500,null=True,blank=True)
    image_origin = models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'Profile/', height_field=None, width_field=None, max_length=1200,blank=True,null=True)
    image_header_origin= models.ImageField(_("تصویر سربرگ"), upload_to=IMAGE_FOLDER+'Profile/header/', height_field=None, width_field=None, max_length=1200,blank=True,null=True)
    address=models.CharField(_('آدرس'),max_length=100,null=True,blank=True)
    postal_code=models.CharField(_('کد پستی'),max_length=50,null=True,blank=True)
    # def social_links(self):
        # return SocialLink
    # =models.ManyToManyField("dashboard.sociallink",blank=True, verbose_name=_("شبکه های اجتماعی"))
    
    def name(self):
        return self.first_name+' '+self.last_name
    # def get_my_qrcode(self):
    #     self.save_qrcode()
    #     return f'{APP_NAME}/images/Profile/{self.pk}.svg'

    # def save_qrcode(self):
    #     try:
    #         data={
    #             'profile_id':self.pk,
    #             'name':self.name,
    #             'image':SITE_DOMAIN+self.image(),
    #         }
    #         img=get_qrcode(data=data)
    #         file_name=os.path.join(os.path.join(os.path.join(os.path.join(MEDIA_ROOT,APP_NAME),'images'),'Profile'),str(self.pk)+".svg")
    #         img.save(file_name)
    #     except :
    #         pass
        
    def header_image(self):
        if self.image_header_origin:
            return MEDIA_URL+str(self.image_header_origin)
        else:
            return STATIC_URL+'authentication/img/city-profile.jpg'

    def image(self):
        if self.image_origin:
            return MEDIA_URL+str(self.image_origin)
        else:
            return STATIC_URL+'authentication/img/avatar.jpg'
    # def save(self):  
        
    #     old_image=None      
    #     try:
    #         old_image=Profile.objects.get(pk=self.pk).image_origin
    #     except:
    #         pass
    #     if not self.image_origin :
    #          super(Profile,self).save()
    #     elif old_image is not None and str(self.image_origin)==str(Profile.objects.get(pk=self.pk).image_origin):
    #         super(Profile,self).save()
    #     elif self.image_origin and FORCE_RESIZE_IMAGE:
    #         #Opening the uploaded image
    #         image = Image.open(self.image_origin)       
    #         output = BytesIO()     
    #         #Resize/modify the image
    #         image = image.resize( (PROFILE_IMAGE_WIDTH, PROFILE_IMAGE_HEIGHT), Image.ANTIALIAS )
            
    #         #after modifications, save it to the output
    #         image.save(output, format='JPEG', quality=95)
           
    #         output.seek(0)  
    #         #change the imagefield value to be the newley modifed image value
    #         self.image_origin = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image_origin.name.split('.')[0], IMAGE_FOLDER+'Profile/image/jpeg', sys.getsizeof(output), None)
            
    #     super(Profile,self).save()
        
    def get_link(self):
        return f"""
        <a href="{self.get_absolute_url()}">
        <i class="fa fa-user"></i>
        {self.name()}
        </a>
        """

    def get_image_link(self):
        return f"""
        <a title="{self.name()}" href="{self.get_absolute_url()}">
        <img src="{self.image()}" width="34px" height="34px" class="rounded-circle">
        </a>
        """
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("پروفایل ها")

    def __str__(self):
        return f'{self.name()} : {self.user.username if self.user else None}'

    def get_absolute_url(self):
        return reverse("app:selected_profile", kwargs={"profile_id": self.pk})
    def get_edit_url(self):
        return reverse("authentication:profile", kwargs={"profile_id": self.pk})
    def get_edit_url_admin(self):
        return f'{ADMIN_URL}{APP_NAME}/profile/{self.pk}/change/'

