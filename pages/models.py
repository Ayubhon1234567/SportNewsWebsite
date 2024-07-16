from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


# class ContactModel(models.Model):


class ConfirmationModel(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4, unique=True)
    status = models.BooleanField(default=True)
    expire_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'


class ContactModel(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class PlayerModel(models.Model):
    name=models.CharField(max_length=500)
    position=models.TextField()
    number=models.IntegerField()
    image=models.ImageField(upload_to='team')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Team'
        verbose_name_plural='Teams'

class DefendersModel(models.Model):
    name=models.CharField(max_length=500)
    position=models.TextField()
    number=models.IntegerField()
    image=models.ImageField(upload_to='defend')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='defend'
        verbose_name_plural='defenders'


class ManagerModel(models.Model):
    name=models.CharField(max_length=500)
    position=models.TextField()
    number=models.IntegerField()
    image=models.ImageField(upload_to='manage')

    def __str__(self):
        return self.name

    class Meta:
      verbose_name='manage'
      verbose_name_plural='manager'




class NewsModel(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='news')
    author = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'


class MatchModel(models.Model):
    team1=models.TextField()
    team2=models.TextField()
    city1=models.TextField()
    city2=models.TextField()
    balance1=models.IntegerField()
    balance2=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    time=models.IntegerField()
    image1=models.ImageField(upload_to='matches')
    image2=models.ImageField(upload_to='matches')
    turnir=models.TextField()


    def __str__(self):
        return self.team1

    class Meta:
        verbose_name='match'
        verbose_name_plural='matches'


class GoalModel(models.Model):
    name=models.TextField()
    score=models.IntegerField()
    number=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='bombardir'
        verbose_name_plural='bombardirs'


class AssistModel(models.Model):
    name=models.TextField()
    score=models.IntegerField()
    number=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='assist'
        verbose_name_plural='assisters'


