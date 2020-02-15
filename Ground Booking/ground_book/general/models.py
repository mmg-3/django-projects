from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


def get_image_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "media/general/images/event_images/%s-%s" % (slug, filename)


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image1 = models.ImageField(upload_to=get_image_filename, verbose_name='Image1', blank=True)
    image2 = models.ImageField(upload_to=get_image_filename, verbose_name='Image2', blank=True)
    image3 = models.ImageField(upload_to=get_image_filename, verbose_name='Image3', blank=True)
    image4 = models.ImageField(upload_to=get_image_filename, verbose_name='Image4', blank=True)
    image5 = models.ImageField(upload_to=get_image_filename, verbose_name='Image5', blank=True)
    image6 = models.ImageField(upload_to=get_image_filename, verbose_name='Image6', blank=True)
    image7 = models.ImageField(upload_to=get_image_filename, verbose_name='Image7', blank=True)
    image8 = models.ImageField(upload_to=get_image_filename, verbose_name='Image8', blank=True)
    image9 = models.ImageField(upload_to=get_image_filename, verbose_name='Image9', blank=True)
    image10 = models.ImageField(upload_to=get_image_filename, verbose_name='Image10', blank=True)

    def __str__(self):
        return self.title


class AvailEvents(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    slug = models.SlugField(allow_unicode=True, unique=True)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Thumbnail', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('general:single', kwargs={'slug': self.slug})



