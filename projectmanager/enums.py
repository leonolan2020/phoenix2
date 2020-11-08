from django.db.models import TextChoices
from django.utils.translation import gettext as _

class AssignmentStatusEnum(TextChoices):
    DEFAULT='DEFAULT',_('DEFAULT')
    IN_PROGRESS='در جریان',_('در جریان')
    DONE='انجام شده',_('انجام شده')
    STOPEED='متوقف شده',_('متوقف شده')
    DENIED='رد شده',_('رد شده')




    