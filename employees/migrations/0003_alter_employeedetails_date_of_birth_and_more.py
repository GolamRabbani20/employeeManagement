# Generated by Django 5.1.1 on 2024-09-14 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_rename_enployeedetails_employeedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2019, 1, 19, 6, 15, 29, 361583, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile_photos/'),
        ),
    ]
