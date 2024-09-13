from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from PIL import Image

class employeeDetails(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=False)
    date_of_birth = models.DateField(blank=False)
    photo = models.ImageField(upload_to='profile_photos/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.photo.path)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
    

