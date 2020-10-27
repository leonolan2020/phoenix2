from dashboard.settings import ADMIN_URL,SITE_URL,MEDIA_URL
from .apps import APP_NAME
class AdminUtility():
    def get_link(self,class_name,class_title):
        url=f'{ADMIN_URL}{APP_NAME}/{class_name}/add/'
        return f"""
         <a target="_blank" href="{url}" title="افزودن {class_title}" >
                     <i class="material-icons text-info">add_circle</i>
                 </a>
        """

    def get_add_contractor(self):
        return self.get_link(class_name='contractor',class_title='پیمانکار')
    
    def get_add_organizationunit(self):
        return self.get_link(class_name='organizationunit',class_title='واحد سازمانی')
    
    def get_add_blog(self):
        return self.get_link(class_name='blog',class_title='مقاله')
    
    def get_add_project(self):
        return self.get_link(class_name='project',class_title='پروژه')
    
    def get_add_homeslider(self):
        return self.get_link(class_name='homeslider',class_title='اسلایدر')