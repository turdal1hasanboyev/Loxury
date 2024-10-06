from django.urls import path

from .views import jewellery, about, shop, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('jewellery/', jewellery, name='jewellery'),
    path('about/', about, name='about'),
    path('shop/', shop, name='shop'),
]
