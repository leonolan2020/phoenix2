from django.db.models import TextChoices
from django.utils.translation import gettext as _
class SignatureStatusEnum(TextChoices):
    DEFAULT='DEFAULT',_('DEFAULT')
    DELIVERED='تحویل شده',_('تحویل شده')
    IN_PROGRESS='در حال بررسی',_('درحال بررسی')
    DENIED='رد شده',_('ردشده')
    ACCEPTED='پذیرفته شده',_('پذیرفته شده')
    PURCHASING='درحال خرید',_('درحال خرید')

    
class EmployeeEnum(TextChoices):
    CEO='سرپرست',_('سرپرست')  
    GUARD='نگهبان',_('نگهبان')      
    MANAGER='مدیر',_('مدیر')      
    TECHNICAL='فنی',_('فنی')    
    DEFAULT='تایید نشده',_('تایید نشده')
    ACCOUNTANT='حسابدار',_('حسابدار')
    CASHIER='صندوقدار',_('صندوقدار')
    
    
class MaterialRequestStatusEnum(TextChoices):
    DEFAULT='DEFAULT',_('DEFAULT')
    DELIVERED='تحویل شده',_('تحویل شده')
    IN_PROGRESS='در حال بررسی',_('درحال بررسی')
    DENIED='رد شده',_('ردشده')
    ACCEPTED='پذیرفته شده',_('پذیرفته شده')
    PURCHASING='درحال خرید',_('درحال خرید')


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
    if status==MaterialRequestStatusEnum.DEFAULT:
        return 'rose'
    if status==MaterialRequestStatusEnum.IN_PROGRESS:
        return 'info'
    if status==MaterialRequestStatusEnum.ACCEPTED:
        return 'success'
    if status==MaterialRequestStatusEnum.DELIVERED:
        return 'success'
    if status==MaterialRequestStatusEnum.DENIED:
        return 'danger'
    if status==MaterialRequestStatusEnum.PURCHASING:
        return 'primary'


    