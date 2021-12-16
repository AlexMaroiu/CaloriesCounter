from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Articol)
# admin.site.register(Mancat)


@admin.register(Articol)
class ArticolAdmin(admin.ModelAdmin):
    list_display = ('nume', 'firma', 'calorii')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return queryset

        return queryset.filer(owner=user)


@admin.register(Mancat)
class MancatAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_articol_nume', 'amount', 'data')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return queryset

        return queryset.filer(owner=user)


@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('username', 'zi', 'calorii')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return queryset

        return queryset.filer(owner=user)
