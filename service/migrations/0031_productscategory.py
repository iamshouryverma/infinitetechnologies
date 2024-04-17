# Generated by Django 4.2.7 on 2023-12-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0030_alter_indexproducts_index_external_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category_title', models.TextField()),
                ('product_category_desc', models.TextField()),
                ('external_category_link', models.TextField(blank=True, null=True)),
                ('product_category_img', models.FileField(default=None, max_length=5000, null=True, upload_to='productimg/')),
            ],
        ),
    ]
