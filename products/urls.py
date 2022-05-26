from django.urls import path,include
from .import views


urlpatterns = [
    path('home/', views.home,name='home'),
    path('category/<int:categoryid>/', views.category,name='category'),
    path('product/<int:productid>/', views.Product,name='Product'),
    path('newproducts/', views.newproducts,name='newproducts'),
    # ---------------------------------------------------------- #
    path('addcart/<int:proid>/', views.addcart, name='Addcarts'),
    path('cartitem/', views.cartitem, name='Cartitem'),
    path('deleteitem/<int:proid>/', views.deleteitem, name='Delete'),
]
