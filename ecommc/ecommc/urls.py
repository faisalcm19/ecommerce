"""
URL configuration for ecommc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecom import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home_view'),
    path('user/reg',views.UserRegisterView.as_view(),name='reg_view'),
    path('login',views.UserLoginView.as_view(),name='login_view'),
    path('logout',views.Userlogout.as_view(),name='log_out'),
    path('product/detil/<int:id>',views.ProductDetailView.as_view(),name='detail_view'),
    path('cart/<int:id>',views.AddtoCart.as_view(),name='add_cart'),
    path('cart/list',views.Cartlist.as_view(),name='cart_list'),
    path('placeorder/<int:cart_id>',views.Placeorderview.as_view(),name='place_order'),
    path('cart/delete/<int:id>',views.CartdeletView.as_view(),name='cart_delet'),
   
    
   
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

