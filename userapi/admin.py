from django.contrib import admin
from .models import UserDetails

# Register your models here.
@admin.register(UserDetails)

class UserAdmin(admin.ModelAdmin):
    search_fields = ('login', 'created_at', 'email')
    list_display = ('admin_img','login','name','created_at')
    list_filter = ('created_at','email')
    readonly_fields = ('admin_img',)