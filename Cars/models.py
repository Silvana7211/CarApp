from django.db import models

class Seller(models.Model):
    Name=models.CharField(max_length=30)
    vat=models.CharField(max_length=30)
    Country=models.CharField(max_length=10)
    City=models.CharField(max_length=10)
    Founded_date=models.DateField()
    Postcode=models.IntegerField()
    Address=models.TextField(max_length=40)
    Phone_number=models.IntegerField()
    Website=models.TextField()
    Email=models.EmailField()


class Car(models.Model):
    manufacturer=models.CharField(max_length=30)
    year=models.IntegerField()
    Model=models.TextField()
    Body_color=models.CharField(max_length=10)
    Body_color_original=models.CharField(max_length=10)
    Upholstery=models.CharField(max_length=10)
    Body_type=models.CharField(max_length=10)
    Number_of_doors=models.IntegerField()
    Type=models.IntegerField(choices=(('1','new'), ('2','used')))
    Country_version=models.CharField(max_length=10)
    Gearing_type=models.IntegerField(choices=(('1','manual'), ('2','automatic')))
    Gears=models.IntegerField()
    Disp=models.IntegerField()
    Horsepower=models.IntegerField()
    Tork=models.IntegerField()
    Km_driven=models.IntegerField()
    Fuel=models.CharField(max_length=10)
    Price=models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='Cars', on_delete=models.CASCADE)
    Seller=models.ForeignKey(Seller, on_delete=models.CASCADE)


