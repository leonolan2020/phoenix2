from django.db import models
from .settings import ADMIN_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
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