'''from django.contrib import admin
from django.urls import path
from .views import home, about, contact, wishlist, upload, login, signup

urlpatterns = [
   path('', home, name="home"),
   path('about', about, name="about"),
   path('contact', contact, name="contact"),
   path('wishlist', wishlist, name="wishlist"),
   path('upload', upload, name="upload"),
   path('login',login,name="login")
   path('signup',signup,name="signup")
   
]
'''
from django.contrib import admin
from django.urls import path
from .views import home, about, contact, add_wishlist, upload, login_user, signup_user, logout_user,product,wishlist,remove_wish,add_cart,remove_cart,cart,search_watch,product_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('upload/', upload, name="upload"),
    path('login/', login_user, name="login"),
    path('signup/', signup_user, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('product/<int:id>', product, name="product"),
    path('add_wishlist/<int:id>', add_wishlist, name="add_wishlist"),
    path('wishlist/', wishlist, name="wishlist"),
    path('remove_wish/<int:id>', remove_wish, name="remove_wish"),
    path('add_cart/<int:id>', add_cart, name="add_cart"),
    path('cart/', cart, name="cart"),
    path('remove_cart/<int:id>', remove_cart, name="remove_cart"),
    path('search/', search_watch, name='search_watch'),
   path('product/<int:watch_id>/', product_detail, name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)