# Generated by Django 3.1.5 on 2021-02-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0003_auto_20210202_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='Seller_id',
            field=models.IntegerField(default=1),
        ),
    ]