# Generated by Django 4.1.1 on 2022-09-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newapp", "0006_product_sub_category_details_porduct_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product_sub_category_details",
            name="porduct_image",
            field=models.ImageField(default="/default.png", upload_to="product_images"),
        ),
    ]