from .settings import ADMIN_URL,SITE_URL,MEDIA_URL
from .apps import APP_NAME
class AdminUtility():
    def get_link(self,class_name,class_title):
        url=f'{ADMIN_URL}{APP_NAME}/{class_name}/add/'
        return f"""
         <a target="_blank" href="{url}" title="افزودن {class_title}" >
                     <i class="material-icons text-info">add_circle</i>
                 </a>
        """

    def get_add_feature(self):
        return self.get_link(class_name='feature',class_title='سرویس')
    def get_add_ourteam(self):
        return self.get_link(class_name='ourteam',class_title='تیم ما')
    def get_add_blog(self):
        return self.get_link(class_name='blog',class_title='مقاله')
    def get_add_ourwork(self):
        return self.get_link(class_name='ourwork',class_title='پروژه ما')
    def get_add_homeslider(self):
        return self.get_link(class_name='homeslider',class_title='اسلایدر')