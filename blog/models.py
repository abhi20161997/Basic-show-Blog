# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	def approved_comments(self):
		return self.comments.filter(approved_comment=True)

class Meta:
	ordering = ['-created']

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('blog.views.post', args=[self.slug])

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
