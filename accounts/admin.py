from django.contrib import admin
from .models import Profile

admin.ModelAdmin.list_display


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name',
                    'last_name', 'email', 'phone', 'is_active']
    list_display_links = ['user', 'first_name', 'last_name']
    list_filter = ['user__is_active']
    list_per_page = 25
    search_fields = ['user__username', 'user__first_name',
                     'user__last_name', 'user__email', 'phone']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    def is_active(self, obj):
        return obj.user.is_active


admin.site.register(Profile, ProfileAdmin)
