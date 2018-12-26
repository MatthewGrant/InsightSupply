from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=25)
    color = models.CharField(max_length=7, unique=True)  # uniuqe hex color
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


def get_default_category():
    return Category.objects.get_or_create(name='default', color='#FFFFFF')


class Insight(models.Model):
    category = models.ForeignKey(
        Category,
        default=get_default_category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    caption = models.CharField(max_length=255)
    source_url = models.TextField(max_length=2000, validators=[URLValidator()])
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """A string representation of the model."""
        return "Category: {}, Caption: {}".format(self.category.name, self.caption)

# TODO:
# use another model to store scraped Articles and reference in Insight
# class Article(models.Model):
#     author = model.CharField(max_length=255, blank=True)
#     title = model.CharField(max_length=255)
#     categories = model.ManyToManyField(Category)
#     tags = models.ManyToManyField(Tag, blank=True)
#     url = model.TextField()
#     html = RichTextField()
#     published_date = models.DateTimeField(null=True)
#     scraped_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)
#
