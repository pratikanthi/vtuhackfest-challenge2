from django.db import models
from django.db.models import signals
from datetime import datetime
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import vtubeat.settings as settings


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_picture = models.ImageField(upload_to = settings.MEDIA_ROOT,null=True, blank=True)
    college_name = models.CharField(null=True, blank=True, max_length=255)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

signals.post_save.connect(create_user_profile,sender=User, weak=False,dispatch_uid='models.create_user_profile')


class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_desc = models.TextField()
    cat_slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
		return self.cat_name



class Query(models.Model):

    title = models.CharField(max_length=255)
    query_details = models.TextField()
    date = models.DateTimeField(default = datetime.now)
    query_by = models.ForeignKey(User)
    query_cat = models.ForeignKey(Category,null=True)
    query_slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Queries'

    def __unicode__(self):
		return self.title


class Answer(models.Model):

    answer_text = models.TextField()
    answer_date = models.DateTimeField(default = datetime.now)
    answer_to_query =  models.ForeignKey(Query)
    answer_by = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Answers'

    def __unicode__(self):
		return self.answer_text
