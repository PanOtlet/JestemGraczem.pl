from meta.views import Meta
from django.conf import settings


def meta_generator(meta=None):
    if meta is None:
        meta = {}
    generate_meta = Meta()
    generate_meta.title = meta['title'] + ' | ' + settings.META['title'] if meta.get('title', []) else settings.META[
        'title']
    generate_meta.description = meta['description'] if meta.get('description', []) else settings.META['description']
    generate_meta.keywords = meta['keywords'] if meta.get('keywords', []) else settings.META['keywords']

    generate_meta.extra_custom_props = [
        ('http-equiv', 'Content-Type', 'text/html; charset=UTF-8'),
    ]
    generate_meta.extra_props = {
        'viewport': 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
    }

    return generate_meta
