from django.db import models
from django.template.defaultfilters import slugify
from django_markdown.models import MarkdownField


class Entrada(models.Model):
    """docstring for Entrada"""
    titulo = models.CharField(max_length = 20)
    contenido = MarkdownField()
    seccionales = ((1, "Barranquilla"), (2, "Cali"), (3, "Bogota"), (4, "Cucuta"))
    autor = models.IntegerField(choices=seccionales)
    slug = models.SlugField(editable=False)
    img = models.ImageField(upload_to="imgenes")

    def __unicode__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)

