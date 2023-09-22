from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="django", slug='django')

    def test_category_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """

        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1, title='django beginners', created_by_id=1,
            slug='django-beginners', price='20.00', image='django.img'
        )

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """

        data = self.data1
        self.assertEqual(str(data), 'django beginners')
