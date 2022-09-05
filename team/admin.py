from django.contrib import admin

from .models import Workers


class WorkersAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'phone', 'position')


admin.site.register(Workers, WorkersAdmin)

# Register your models here.
