from django.db import models

# Create your models here.
class FeaturedPost(models.Model):
    
    img = models.ImageField(upload_to='pics/')
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now = True)
    desc = models.TextField()
    #price = models.IntegerField()
    condition = models.BooleanField(default=True)

