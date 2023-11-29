from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from custom_user.forms import UserCreationForm, UserChangeForm
from custom_user.models import CustomUser


# Register your models here
class MyUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'username', 'date_joined', 'last_login','is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        #('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin','is_active',)}),
    )

    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields':('email', 'username', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'username',)
    ordering = ('email', 'username',)
    filter_horizontal = ()


admin.site.register(CustomUser, MyUserAdmin)
admin.site.unregister(Group)
