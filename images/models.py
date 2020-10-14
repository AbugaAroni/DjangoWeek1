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

    def update_editor(self):
        Editor.objects.filter(first_name = self.first_name).update(first_name ='rick')

    class Meta:
        ordering = ['first_name']


class Locations(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        Locations.objects.filter(location_name = self.location_name).update(location_name ='rick')

    def display_location():
        locs = Locations.objects.all()
        return locs

class Categories(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name

    def save_cat(self):
        self.save()

    def delete_cat(self):
        self.delete()

    def update_cat(self):
        Categories.objects.filter(category_name = self.category_name).update(category_name ='rick')

    def display_cat():
        catagories = Categories.objects.all()
        return catagories

class Images(models.Model):
    title = models.CharField(max_length =60)
    _images = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    location = models.ForeignKey('Locations', on_delete=models.CASCADE,)
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

    def save_image(self):
         self.save()

    def delete_image(self):
         self.delete()

    def update_image(self):
        Images.objects.filter(title = self.title).update(title ='rick')
