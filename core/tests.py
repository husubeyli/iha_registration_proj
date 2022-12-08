from django.test import TestCase
from core.models import CategoryIHA


class CategoryIHAModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        super(CategoryIHAModelTest, cls).setUpClass()
        # Set up non-modified objects used by all test methods
        category = CategoryIHA.objects.create(name='test')

    def test_name_label(self):
        category = CategoryIHA.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Ad')

    def test_name_max_length(self):
        category = CategoryIHA.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_object_name_is_name(self):
        category = CategoryIHA.objects.get(id=1)
        expected_object_name = f'{category.name}'
        self.assertEqual(str(category), expected_object_name)
