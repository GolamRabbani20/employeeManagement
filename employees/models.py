from django.db import models


class enployeeDetails(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=False)
    date_of_birth = models.DateField(blank=False)
    photo = models.ImageField(upload_to='profile_photos/')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
