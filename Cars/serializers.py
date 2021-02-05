from rest_framework import serializers
from Cars.models import Car, Seller
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'owner']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=['manufacturer', 'Model', 'year', 'Body_color', 'Body_color_original', 'Upholstery',
                    'Body_type', 'Number_of_doors', 'Country_version', 'Type', 'Gearing_type',
                    'Gears', 'Disp', 'Horsepower', 'Tork', 'Km_driven', 'Fuel', 'Price', 'Seller', 'owner']

        def create(self, validated_data):
            """
            Create and return a new `Car` instance, given the validated data.
            """
            return Car.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """
            Update and return an existing `Car` instance, given the validated data.
            """
            instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
            instance.Model = validated_data.get('Model', instance.Model)
            instance.year = validated_data.get('year', instance.year)
            instance.Body_color = validated_data.get('Body_color', instance.Body_color)
            instance.Body_color_original = validated_data.get('Body color original', instance.Body_color_original)
            instance.Upholstery=validated_data.get('Upholstery', instance.Upholstery)
            instance.Body_type=validated_data.get('Body type', instance.Body_type)
            instance.Number_of_doors=validated_data.get('Number of doors', instance.Number_of_doors)
            instance.Country_version=validated_data.get('Country version', instance.Country_version)
            instance.Type=validated_data.get('Type', instance.Type)
            instance.Gearing_type=validated_data.get('Gearing type', instance.Gearing_type)
            instance.Gears=validated_data.get('Gears', instance.Gears)
            instance.Disp=validated_data.get('Displacement', instance.Disp)
            instance.Horsepower=validated_data.get('Horesepower', instance.Horsepower)
            instance.Tork=validated_data.get('Tork', instance.Tork)
            instance.Km_Driven=validated_data.get('Km driven', instance.Km_Driven)
            instance.Fuel=validated_data.get('Fuel', instance.Fuel)
            instance.Price=validated_data.get('Price', instance.Price)
            instance.Seller=validated_data.get('Seller', instance.Seller)
            instance.owner = serializers.ReadOnlyField(source='owner.username')
            instance.save()
            return instance

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=['Name', 'vat', 'Country', 'City', 'Founded_date', 'Postcode', 'Address', 'Phone_number',
                'Website', 'Email']

        def create(self, validated_data):
            """
            Create and return a new `Seller` instance, given the validated data.
            """
            return Seller.objects.create(**validated_data)

        def update (self, instance, validated_data):
            instance.Name = validated_data.get('Name', instance.Name)
            instance.vat = validated_data.get('vat', instance.vat)
            instance.Country = validated_data.get('Country', instance.Country)
            instance.City = validated_data.get('City', instance.City)
            instance.Founded_date = validated_data.get('Founded_date', instance.Founded_date)
            instance.Postcode = validated_data.get('Postcode', instance.Postcode)
            instance.Address = validated_data.get('Address', instance.Address)
            instance.Phone_number = validated_data.get('Phone_number', instance.Phone_number)
            instance.Website = validated_data.get('Website', instance.Website)
            instance.Email = validated_data.get('Email', instance.Email)
            instance.save()
            return instance




