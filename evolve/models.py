from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from published_manager.managers import PublishedManager
from tagging.fields import TagField

class Idea(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Author"))
    pub_date = models.DateTimeField(auto_now_add = True, verbose_name=_("Date Published"))
    parent_idea = models.ForeignKey("self", verbose_name="Parent Idea")
    state = models.CharField(maxlength=1, choices=settings.STATE_CHOICES, default=settings.STATE_DEFAULT, verbose_name=_("State of object"))
    content = models.TextField(_("Content"))
    ip_address = models.IPAddressField(verbose_name=_("Author's IP Address"))
    slug = models.SlugField(prepopulate_from=('title',), unique=True, verbose_name=_("Slug Field"), blank=True, null=True)
    objects = models.Manager()
    published_objects = PublishedManager()
    tags = TagField(help_text=_("Enter key terms seperated with a space that you want to associate with this Idea"), verbose_name=_("Tags"))

    def __str__(self):
        return "%s" % (self.content)

#    class Meta:
#        ordering = ['content']
#        verbose_name = "Idea"
#        verbose_name_plural = "Ideas"
#        unique_together = (("parent_idea", "content"),)

    class Admin:
        pass
#        ordering = ['content']
#        search_fields = ['content']
