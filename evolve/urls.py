from django.conf.urls.defaults import *
from evolve.feeds import RssFeed, AtomFeed
from evolve.models import Idea 
from django.conf import settings

feeds = { 
    'rss': RssFeed,
    'atom': AtomFeed,
}

idea_dict = {
    'model': Idea,
    'base_url': '/ideas/',
}

urlpatterns = patterns('',
    (r'^rss/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds, 'url': 'rss'}),
    (r'^atom/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds, 'url': 'atom'}),
)

urlpatterns += patterns('django.views.generic.create_update',
    (r'^create/$', 'create_object', dict(model=Idea, login_required=True, extra_context={'STATE_DEFAULT': settings.STATE_DEFAULT})),
)

urlpatterns += patterns('sorted_paginated_authored_archived_list_view.views',
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', 'sorted_paginated_authored_archived_list', idea_dict),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', 'sorted_paginated_authored_archived_list', idea_dict),
    (r'^(?P<year>\d{4})/$', 'sorted_paginated_authored_archived_list', idea_dict),
    (r'^$', 'sorted_paginated_authored_archived_list', idea_dict),
)
