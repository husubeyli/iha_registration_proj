from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Marka(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryIHA(models.Model):
    name = models.CharField('Ad', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class IHA(models.Model):
    name = models.CharField('Ad', max_length=255)
    weight = models.DecimalField(_("Weight"), max_digits=10, decimal_places=2)

    categories = models.ForeignKey(
        'core.CategoryIHA', related_name='ihas', on_delete=models.CASCADE, blank=True, null=True)
    markas = models.ForeignKey(
        'core.Marka', related_name='ihas', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(_("slug"), editable=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(IHA, self).save(*args, **kwargs)
        self.slug = f'{self.name.lower()}-{self.id}'
        # self.save()
        super(IHA, self).save(*args, **kwargs)  # Call the real save() method

    def get_absolute_url(self):
        """ Returns the detail URL. """
        return reverse("core:iha_detail", kwargs={"slug": self.slug})
