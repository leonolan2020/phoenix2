from .models import Notification,Card



class NotificationRepo:
    def __init__(self,user):
        self.objects=Notification.objects
        self.user=user
    def list(self):
        return self.objects.all()

class CardRepo:
    def __init__(self,user):
        self.objects=Card.objects
        self.user=user
    def list(self):
        return self.objects.all()