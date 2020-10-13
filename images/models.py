from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    def display_editor():
        editors = Editor.objects.all()
        return editors

    class Meta:
        ordering = ['first_name']


class Locations(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

class Categories(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

class Images(models.Model):
    _images = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ManyToManyField(Locations)
    Category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title
