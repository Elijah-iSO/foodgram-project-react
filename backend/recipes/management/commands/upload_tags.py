from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Tag

base_dir = settings.BASE_DIR


class Command(BaseCommand):
    def handle(self, *args, **options):

        tags_data = (
            ('Завтрак', '#E26C2D', 'breakfast'),
            ('Обед', '#008000', 'dinner'),
            ('Ужин', '#7366BD', 'supper'),
        )
        tags = [
            Tag(
                name=tag[0],
                color=tag[1],
                slug=tag[2],
            )
            for tag in tags_data
        ]
        Tag.objects.bulk_create(tags)

        return ('Tags upload is successful')
