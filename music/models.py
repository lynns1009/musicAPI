from django.db import models

STYLE=[('J','Jazz'),('P','Pop music'),('F','Folk music'),('B','Blue'),('C','Country music'),('M','Mental')]


class Album(models.Model):
    name = models.CharField(max_length=100,blank=True,default='')
    author = models.CharField(max_length=100, blank=True, default='')
    publish_year = models.DateTimeField()
    style=models.CharField(choices=STYLE,max_length=1)

    def __str__(self):
        return self.name


class Music(models.Model):
    title = models.CharField(max_length=100,blank=True,default='')
    lyrics = models.TextField()
    album = models.CharField(max_length=100,blank=True,default='')
    alb_re=models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title









