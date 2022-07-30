from django.contrib import admin

from .models import Product , Comments

# Register your models here.

class commentinline(admin.StackedInline):
    model = Comments
    
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [commentinline]


admin.site.register(Product,ProductAdmin)
admin.site.register(Comments)