import feedparser
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from service.models import RSS, LinkBlog


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        rss = RSS.objects.all()
        list = []
        for r in rss:
            self.stdout.write('Generowanie: ' + self.style.SUCCESS(r.title))
            feed = feedparser.parse(r.url)
            for f in feed.entries:
                try:
                    link = LinkBlog.objects.get(url=f.link)
                    print('Exist: ' + f.title)
                except ObjectDoesNotExist:
                    LinkBlog.objects.create(
                        url=f.link,
                        description=f.summary,
                        image='https://via.placeholder.com/640x480?text='+r.title,
                        accepted=True,
                        sponsored=False,
                        partner=True,
                        iframe=True,
                        title=f.title
                    )
                    self.stdout.write(self.style.SUCCESS(f.title))
                    # self.stdout.write(self.style.SUCCESS(f.link))
                    # self.stdout.write(self.style.SUCCESS(f.summary))
                    # self.stdout.write(self.style.SUCCESS(f.published))
                    # self.stdout.write(self.style.SUCCESS('https://via.placeholder.com/640x480?text='+f.title))
                    # self.stdout.write(self.style.SUCCESS(f.date))
