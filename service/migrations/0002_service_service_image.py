# Generated by Django 4.2.7 on 2023-12-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='news/'),
        ),
    ]