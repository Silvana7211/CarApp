# Generated by Django 3.1.5 on 2021-02-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0006_auto_20210205_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='Seller_id',
            field=models.IntegerField(),
        ),
    ]
