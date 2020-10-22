from .models import Notification



class NotificationRepo:
    def __init__(self,user):
        self.objects=Notification.objects
        self.user=user
    def list(self):
        return self.objects.all()