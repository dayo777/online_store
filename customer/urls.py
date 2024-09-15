from django.urls import path, include
from customer import views


app_name = 'customer_app'

urlpatterns = [
    path('', views.CustomerCreateGet.as_view(), name='customer-create-list'),
    path('<int:pk>/', views.CustomerCreateGet.as_view(), name='customer-detail'),
]