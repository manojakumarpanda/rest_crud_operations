from django.contrib import admin
from .models import profile

# Register your models here.
class Proflie_Admin(admin.ModelAdmin):
    list_filter = ['id','name']


admin.site.site_header='User_curd'
admin.site.site_title='User_curd'
admin.site.index_header='User_curd Admin'
admin.site.register(profile,Proflie_Admin)