from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class Category(models.Model):
    cat_name = models.CharField(max_length=255)
    cat_desc = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
		return self.cat_name



class Query(models.Model):
    title = models.CharField(max_length=255)
    query_details = models.TextField()
    date = models.DateTimeField(default = datetime.now)
    query_by = models.ForeignKey(User, unique=True)
    query_cat = models.ManyToManyField(Category, related_name = "category")

    class Meta:
        verbose_name_plural = 'Queries'

    def __unicode__(self):
		return self.title


class Answer(models.Model):
    answer_text = models.TextField()
    answer_date = models.DateTimeField(default = datetime.now)
    answer_to_query =  models.ForeignKey(Query)
    answer_by = models.ForeignKey(User, unique=True)

    class Meta:
        verbose_name_plural = 'Answers'

    def __unicode__(self):
		return self.answer_text
