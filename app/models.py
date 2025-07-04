from django.db import models
from django.urls import reverse
# Create your models here.c
class Project(models.Model):
    TAG_CHOICES = [
        ('API', 'API'),
        ('full_stack', 'Full Stack'),
        ('ML', 'Machine Learning'),
        ('NLP', 'Natural Language Processing'),
        ('computer_vision', 'Computer Vision'),
        ('mobile', 'Mobile'),
    ]

    tag = models.CharField(max_length=30, choices=TAG_CHOICES)

    image = models.ImageField(upload_to="images/", null=True, blank=True)
    image_alt = models.CharField(max_length=200, null=True, blank=True, verbose_name="Image Alt Text")
    updated = models.DateTimeField(auto_now=True)
    brief_description = models.TextField(null=True, blank=True, verbose_name="Brief Project Description")
    live_link = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name="Project Title")
    description = models.TextField(null=True, blank=True, verbose_name="Detailed Project Description")
    tag_1 = models.CharField(max_length=200, null=True, blank=True, verbose_name="Project Tag 1")
    tag_2 = models.CharField(max_length=200, null=True, blank=True, verbose_name="Project Tag 2")
    tag_3 = models.CharField(max_length=200, null=True, blank=True, verbose_name="Project Tag 3")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("engine_detail", args=[str(self.id)])

