from django.contrib import admin
from rango.models import Category, Page
from rango.pageadmin import PageAdmin
from rango.models import UserProfile

admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)