from django.db import models

# Create your models here.

class iletisim(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=300)
    message = models.TextField(max_length=5000)
    

class yazilar(models.Model):
    on_baslik = models.CharField(max_length=200)
    baslik = models.CharField(max_length=200)
    tarih = models.CharField(max_length=50)
    
    img1 = models.ImageField(null=True, blank=True, upload_to="images/")
    yazi1 = models.TextField(max_length=5000)
    
    img2 = models.ImageField(null=True, blank=True, upload_to="images/")
    yazı2 = models.TextField(max_length=5000)
    
    img3 = models.ImageField(null=True, blank=True, upload_to="images/")
    
    yaziBenzersizId = models.CharField(max_length=10)
    yazi_path = models.CharField(max_length=100, default="")