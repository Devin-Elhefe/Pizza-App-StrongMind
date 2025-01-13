from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('toppings/', views.topping_list, name='topping_list'),
    path('toppings/add/', views.add_topping, name='add_topping'),
    path('toppings/delete/<int:topping_id>/', views.delete_topping, name='delete_topping'),
    path('toppings/update/<int:topping_id>/', views.update_topping, name='update_topping'),
    path('pizzas/', views.pizza_list, name='pizza_list'),
    path('pizzas/add/', views.add_pizza, name='add_pizza'),
    path('pizzas/delete/<int:pizza_id>/', views.delete_pizza, name='delete_pizza'),
    path('pizzas/update/<int:pizza_id>/', views.update_pizza, name='update_pizza'),
]