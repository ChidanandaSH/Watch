from django.contrib import admin
from .models import Watches, WatchesUploads, Wishlist, Cart, Watch_Review,CartItem


# Register your models here.
admin.site.register(Watches)

# Register your models here.



class WatchesUploadsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'image','count')
    list_filter = ('name', 'price')
    search_fields = ['name', 'description','price']
admin.site.register(WatchesUploads, WatchesUploadsAdmin)




#class WishlistAdmin(admin.ModelAdmin):
#   list_display = ('user', 'products')
#    list_filter = ('user', 'products')
admin.site.register(Wishlist)



#class CartAdmin(admin.ModelAdmin):
#    list_display = ('user', 'products')
#    list_filter = ('user', 'products')
admin.site.register(Cart)
admin.site.register(CartItem)


class Watch_ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'products','rating','review')
    list_filter = ('user', 'products', 'rating', 'review')
admin.site.register(Watch_Review)

