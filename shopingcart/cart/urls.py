from django.urls import path
from search_app.views import SearchResult

from cart import views

app_name = 'cart'
urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('',views.cart_detail,name='cart_detail'),
    path('delete/<int:product_id>/', views.delete,name='delete'),
    path('item_delete/<int:product_id>/',views.item_delete,name='item_delete'),
    ]