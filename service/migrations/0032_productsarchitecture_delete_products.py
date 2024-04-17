# Generated by Django 4.2.7 on 2023-12-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0031_productscategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsArchitecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('architecture_product_title', models.TextField()),
                ('architecture_product_desc', models.TextField()),
                ('architecture_external_link', models.TextField(blank=True, null=True)),
                ('architecture_product_img', models.FileField(default=None, max_length=5000, null=True, upload_to='productimg/')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
