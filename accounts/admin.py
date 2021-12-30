from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


# Register your models here.
class AccountUserAdmin(UserAdmin):
    list_display = ('email', 'username','first_name', 'last_name','date_joined' ,'last_login','is_active' )
    list_display_links = ('email', 'username','first_name', 'last_name')                            #in admin folder along with email we can click on these fields also to get the details
    readonly_fields = ('date_joined' ,'last_login')
    ordering = ('-date_joined',)


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountUserAdmin)
