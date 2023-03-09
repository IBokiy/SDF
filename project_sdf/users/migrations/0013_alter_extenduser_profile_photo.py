# Generated by Django 4.1.7 on 2023-03-09 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_extenduser_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='profile_photo',
            field=models.ImageField(blank=True, default='default_profile_photo.jpg', null=True, upload_to='profile_photos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
    ]
