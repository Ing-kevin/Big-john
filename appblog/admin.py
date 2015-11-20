from django.contrib import admin
from .models import Entrada
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.

@admin.register(Entrada)
class EntradaAdmin(MarkdownModelAdmin):
    pass
