from django.conf import settings
from django.db import models
from rest_framework import reverse as api_reverse
from django.urls import reverse

# Create your models here.
class relations(models.Model):
    """This class represents the relationship model."""
    relation_hindi = models.CharField(max_length=100, blank=False, unique=False)
    relation_english = models.CharField(max_length=100, blank=False, unique=False)
    relation_type = models.CharField(max_length=5, blank=False, unique=False)
    relation_subtype = models.CharField(max_length=5, blank=False, unique=False)
    relation_link = models.CharField(max_length=5, blank=True, unique=False)
    relation_desc = models.CharField(max_length=25, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    def get_api_url(self):
        return reverse("readOne", kwargs={'id': self.id})

class relation_desc(models.Model):
    """This class represents the relationship model description."""
    relation = models.CharField(max_length=100, blank=False, unique=False)
    relation_type = models.CharField(max_length=5, blank=False, unique=False)
    relation_subtype = models.CharField(max_length=5, blank=False, unique=False)
    relation_link = models.CharField(max_length=5, blank=True, unique=False)
    relation_desc = models.CharField(max_length=25, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class relation_hierarchy(models.Model):
    """This class represents the relationship hierarchy model."""
    l1_relation = models.CharField(max_length=5, blank=False, unique=False)
    l2_relation = models.CharField(max_length=5, blank=False, unique=False)
    l3_relation = models.CharField(max_length=5, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)