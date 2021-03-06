from django.test import TestCase
from .models import Locations,Categories,Blog_Images

# Create your tests here.

class CategoriesTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.abugacat= Categories(category_name = 'Mombasa')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abugacat,Categories))

    # Testing Save Method
    def test_save_method(self):
        self.abugacat.save_cat()
        cats = Categories.objects.all()
        self.assertTrue(len(cats) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abugacat.save_cat()
        cats = Categories.objects.all()
        self.assertTrue(len(cats) > 0)

        self.abugacat.delete_cat()
        cats = Categories.objects.filter(category_name='Mombasa')
        self.assertEqual(len(cats), 0)

    #Testing display method
    def test_display_method(self):
        self.abugacat.save_cat()
        goat = Categories.display_cat()
        catz = Categories.objects.all()
        self.assertTrue(len(catz), len(goat))

    # Testing update Method
    def test_update_method(self):
        self.abugacat.save_cat()
        cats = Categories.objects.all()
        self.assertTrue(len(cats) > 0)

        self.abugacat.update_cat()
        catzz = Categories.objects.filter(category_name='rick')
        self.assertTrue(len(catzz) > 0)


class LocationsTestClass(TestCase):

        def setUp(self):
            self.abugaloc= Locations(location_name = 'Mombasa')

        # Testing  instance
        def test_instance(self):
            self.assertTrue(isinstance(self.abugaloc,Locations))

        # Testing Save Method
        def test_save_method(self):
            self.abugaloc.save_location()
            locs = Locations.objects.all()
            self.assertTrue(len(locs) > 0)

        # Testing Delete Method
        def test_delete_method(self):
            self.abugaloc.save_location()
            locs = Locations.objects.all()
            self.assertTrue(len(locs) > 0)

            self.abugaloc.delete_location()
            cats = Locations.objects.filter(location_name='Mombasa')
            self.assertEqual(len(cats), 0)

        #Testing display method
        def test_display_method(self):
            self.abugaloc.save_location()
            goat = Locations.display_location()
            catz = Locations.objects.all()
            self.assertTrue(len(catz), len(goat))

        # Testing update Method
        def test_update_method(self):
            self.abugaloc.save_location()
            locs = Locations.objects.all()
            self.assertTrue(len(locs) > 0)

            self.abugaloc.update_location()
            loczz = Locations.objects.filter(location_name='rick')
            self.assertTrue(len(loczz) > 0)


class ImagesTestClass(TestCase):

        def setUp(self):
            self.abugaloc= Locations(location_name = 'Mombasa')
            self.abugaloc.save_location()
            self.abugacat= Categories(category_name = 'Potrait')
            self.abugacat.save_cat()

            self.abugaimage= Blog_Images(title= 'Cool pic',i_images='image',  description='Lorem ipsum dolor sit amet.', locations= self.abugaloc)

        # Testing  instance
        def test_instance(self):
            self.assertTrue(isinstance(self.abugaimage,Blog_Images))

        # Testing Save Method
        def test_save_method(self):
            self.abugaimage.save_image()
            imag = Blog_Images.objects.all()
            self.assertTrue(len(imag) > 0)

        # Testing Delete Method
        def test_delete_method(self):
            self.abugaimage.save_image()
            imag = Blog_Images.objects.all()
            self.assertTrue(len(imag) > 0)

            self.abugaimage.delete_image()
            imag1 = Blog_Images.objects.filter(title='Cool pic')
            self.assertEqual(len(imag1), 0)

        # Testing update Method
        def test_update_method(self):
            self.abugaimage.save_image()
            imag = Blog_Images.objects.all()
            self.assertTrue(len(imag) > 0)

            self.abugaimage.update_image()
            imagz = Blog_Images.objects.filter(title='rick')
            self.assertTrue(len(imagz) > 0)

        # Testing get(id) Method
        def test_get_id_method(self):
            self.abugaimage.save_image()
            imag = Blog_Images.objects.all()
            self.assertTrue(len(imag) > 0)

            xyz = Blog_Images.get_image_by_id(self.abugaimage.id)
            self.assertTrue(len(xyz)> 0)

        # Testing get(loc) Method
        def test_filter_loc_method(self):
            self.abugaimage.save_image()
            imag = Blog_Images.objects.all()
            self.assertTrue(len(imag) > 0)

            xzy = Blog_Images.filter_by_location(self.abugaimage.locations)
            self.assertTrue(len(xzy)> 0)
