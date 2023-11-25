from django.contrib import admin
from django.contrib.admin import ModelAdmin

from escolas.models import Escola, Telefone, Email


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


@admin.register(Escola)
class EscolaAdmin(ModelAdmin):
    inlines = [TelefoneInline, EmailInline, ]


# @admin.register(Telefone)
# class TelefoneAdmin(ModelAdmin):
#     ...
#
#
# @admin.register(Email)
# class EmailAdmin(ModelAdmin):
#     ...
