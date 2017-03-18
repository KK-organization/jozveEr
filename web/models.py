from django.db import models
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_delete

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 50, default="")
    last_name = models.CharField(max_length=50, default="")
    useremail = models.CharField(max_length=50, default="")
    username = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    token = models.CharField(max_length=50, default="")
    signedin = models.CharField(max_length=10, default="")

    def signin(self):
        self.signedin = 'True'

    def signout(self):
        self.signedin='False'

    def __str__(self):
        return self.username


class Note(models.Model):
    link = models.FileField(upload_to='res/')
    name = models.CharField(max_length=100, default="")
    username = models.ForeignKey(User)
    describtion = models.CharField(max_length=200, default="")
    prof = models.CharField(max_length=100)

@receiver(post_delete, sender = Note)
def fileDelete(sender, instance, **kwargs):
    if instance.link :
        instance.link.delete(False)

#class University(models.Model):
#    name = models.CharField(max_length=100)
#    notes = models.ForeignKey(*Note)
