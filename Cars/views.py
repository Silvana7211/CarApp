from rest_framework import generics
from Cars.models import Car, Seller
from Cars.serializers import CarSerializer, SellerSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarList(generics.ListCreateAPIView):
    """
    List all cars, or add a new car.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('manufacturer', 'Model', 'year', 'Body_color', 'Body_color_original', 'Upholstery',
                    'Body_type', 'Number_of_doors', 'Country_version', 'Type', 'Gearing_type',
                    'Gears', 'Disp', 'Horsepower', 'Tork', 'Km_driven', 'Fuel', 'Price', 'Seller')



class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class SellerList(generics.ListCreateAPIView):
    """
    List all Sellers, or add a new seller.
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ( 'Name', 'vat', 'Country', 'City', 'Founded_date', 'Postcode', 'Address', 'Phone_number',
                'Website', 'Email')


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    queryset = Seller.objects.all()
    serializer_class = SellerSerializer