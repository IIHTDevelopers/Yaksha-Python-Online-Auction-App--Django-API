"""OnlineAuctionAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from auctionapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('seller/',views.SellerView.as_view()),
    path('seller_id/<int:pk>/',views.SellerView.as_view()),

    path('product/',views.ProductView.as_view()),
    path('product_id/<int:pk>/',views.ProductView.as_view()),

    path('customer/',views.CustomerView.as_view()),
    path('customer_id/<int:pk>/',views.CustomerView.as_view()),

    path('get_products/',views.GetProductView.as_view()),
    path('place_bid/',views.BidsView.as_view()),
    path('list_products/',views.BidsView.as_view()),
    path('list_products_by_date/',views.BidsByDateView.as_view()),
    path('list_products_by_category/',views.ListProductsByCategoryView.as_view())


]
