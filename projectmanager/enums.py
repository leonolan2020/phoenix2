from django.db.models import TextChoices
from django.utils.translation import gettext as _

class EmployeeEnum(TextChoices):
    CEO='سرپرست',_('سرپرست')  
    GUARD='نگهبان',_('نگهبان')      
    MANAGER='مدیر',_('مدیر')      
    TECHNICAL='فنی',_('فنی')    
    DEFAULT='تایید نشده',_('تایید نشده')
    ACCOUNTANT='حسابدار',_('حسابدار')
    CASHIER='صندوقدار',_('صندوقدار')
    
    


class AssignmentStatusEnum(TextChoices):
    DEFAULT='DEFAULT',_('DEFAULT')
    IN_PROGRESS='در جریان',_('در جریان')
    DONE='انجام شده',_('انجام شده')
    STOPEED='متوقف شده',_('متوقف شده')
    DENIED='رد شده',_('رد شده')

def StatusColor(status):
    if status==AssignmentStatusEnum.DEFAULT:
        return 'rose'
    if status==AssignmentStatusEnum.IN_PROGRESS:
        return 'info'
    if status==AssignmentStatusEnum.DONE:
        return 'success'
    if status==AssignmentStatusEnum.STOPEED:
        return 'secondary'
    if status==AssignmentStatusEnum.DENIED:
        return 'danger'


    