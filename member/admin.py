from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import SignupForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = SignupForm
    list_display = ('userMail', 'nickname', 'is_active', 'date_joined')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('userMail', 'password')}),
        (_('Personal info'), {'fields': ('nickname', )}),
        (_('Permissions'), {'fields': ('is_active',)}),
        (_('added info'), {'fields': ('location', 'is_sharer', 'point')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nickname', 'password1', 'password2')}
         ),
         (_('added info'), {'fields': ('location', 'is_sharer', 'point')}),
    )
    search_fields = ('userMail','nickname')
    ordering = ('-date_joined',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

