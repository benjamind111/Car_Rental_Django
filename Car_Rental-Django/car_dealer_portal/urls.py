from django.urls import path
from car_dealer_portal.views import *

urlpatterns = [
    path('index/', index, name='dealer_index'),
    path('login/', login, name='dealer_login'),
    path('auth/', auth_view, name='dealer_auth'),
    path('logout/', logout_view, name='dealer_logout'),
    path('register/', register, name='dealer_register'),
    path('registration/', registration, name='dealer_registration'),
    path('add_vehicle/', add_vehicle, name='add_vehicle'),
    path('manage_vehicles/', manage_vehicles, name='manage_vehicles'),
    path('order_list/', order_list, name='order_list'),
    path('complete/', complete, name='complete'),
    path('history/', history, name='history'),
    path('delete/', delete, name='delete'),
]
