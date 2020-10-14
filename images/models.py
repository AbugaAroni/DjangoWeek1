from django.db import models
from django.db.models import Q

# Create your models here

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

class Blog_Images(models.Model):
    title = models.CharField(max_length =60)
    i_images = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE,)
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    def save_image(self):
         self.save()

    def delete_image(self):
         self.delete()

    def update_image(self):
        Images.objects.filter(title = self.title).update(title ='rick')

    def get_image_by_id(imgid):
        idImages = Images.objects.filter(id = imgid)
        return idImages

    @classmethod
    def search_image(cls, imgcategory):
        catImages = Images.objects.filter(category = imgcategory)
        return catImages

    @classmethod
    def search_by_title(cls,search_term):
        img = Blog_Images.objects.filter(Q(category__category_name=search_term))
        return img

    def filter_by_location(imglocation):
        catlocation = Images.objects.filter(location = imglocation)
        return catlocation
