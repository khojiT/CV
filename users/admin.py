from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserAdmin(UserAdmin):
    model = User
    exclude = ('username',)
    list_display = ('__str__','mobile_number', 'is_active',)
    list_filter = ( 'is_staff', 'is_active',)
    search_fields = ('mobile_number', 'first_name','last_name','melli_code')
    ordering = ('date_joined',)
    fieldsets = (
        (None, {'classes': ('wide',),
            'fields': ('mobile_number', 'password',)}),
        ('اطلاعات شخصی',{'fields': ( 'first_name' ,'last_name' , 'melli_code' ) } ),
        ('دسترسی ها', {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions', 'groups', ) } ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile_number', 'password1', 'password2')}
        ),
        ('اطلاعات شخصی',{'fields': ( 'first_name' ,'last_name' ,'melli_code')}),
        ('دسترسی ها', {'fields': ('is_staff', 'is_active', 'is_superuser', 'user_permissions', 'groups',)}),
    )


admin.site.register(User,UserAdmin)