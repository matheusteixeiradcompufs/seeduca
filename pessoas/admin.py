from django.contrib import admin

from pessoas.models import Aluno, EhPCD, Telefone, Email, Funcionario


class TelefoneInline(admin.TabularInline):
    model = Telefone
    extra = 1


class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


class PCDInline(admin.TabularInline):
    model = EhPCD


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', )
    inlines = [TelefoneInline, EmailInline, PCDInline]


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', )
    inlines = [TelefoneInline, EmailInline]
