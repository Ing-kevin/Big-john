from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField

class Entrada(models.Model):
    """docstring for Entrada"""
    titulo = models.CharField(max_length = 20)
    contenido = MarkdownField()
    slug = models.SlugField(editable = False)

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)
