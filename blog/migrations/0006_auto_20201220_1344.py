# Generated by Django 2.2 on 2020-12-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201220_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, storage='press_release_storage', upload_to='profile_pics'),
        ),
    ]
