from evolve.models import Idea
from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from django.conf import settings

class RssFeed(Feed):
    title = _("Ideas")
    link = "/ideas/" 
    description = _("Ideas")
    def items(self):
        return Idea.published_objects.all().order_by('-pub_date')[:5]

class AtomFeed(RssFeed):
    feed_type = Atom1Feed
