from django.test import TestCase
from .models import Editor,Locations,Categories,Images

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.abuga= Editor(first_name = 'Abuga', last_name ='Aroni', email ='abugaaroni@gmail.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.abuga,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.abuga.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.abuga.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

        self.abuga.delete_editor()
        editors = Editor.objects.filter(first_name='Abuga')
        self.assertEqual(len(editors), 0)

    #Testing display method
    def test_display_method(self):
        self.abuga.save_editor()
        goat = Editor.display_editor()
        editors = Editor.objects.all()

        self.assertTrue(len(editors), len(goat))

    # Testing update Method
    def test_update_method(self):
        self.abuga.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

        self.abuga.update_editor()
        editors = Editor.objects.filter(first_name='rick')
        self.assertTrue(len(editors) > 0)

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



#class ImagesTestClass(TestCase):
