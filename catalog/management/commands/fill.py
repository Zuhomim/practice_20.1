from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'name': 'category_1', 'description': 'desc_1'},
            {'name': 'category_2', 'description': 'desc_2'},
            {'name': 'category_3', 'description': 'desc_3'},
            {'name': 'category_4', 'description': 'desc_4'},
        ]

        categories_for_create = []
        for category_item in category_list:
            categories_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()

        Category.objects.bulk_create(categories_for_create)
