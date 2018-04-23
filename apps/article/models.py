#_*_encoding:utf-8_*_#
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=30,verbose_name='题目')
    image=models.ImageField(upload_to='article/%Y/%m',verbose_name='封面图',null=True,blank=True)
    content=models.TextField(max_length=10000,verbose_name='内容')
    add_time=models.DateTimeField(default=datetime.now,verbose_name='添加时间')
    click_nums=models.IntegerField(default=0,verbose_name='点击数')
    fav_nums=models.IntegerField(default=0,verbose_name='收藏数')
    tag=models.ManyToManyField('Tag')

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    name=models.CharField(max_length=10,verbose_name='标签')

    def __unicode__(self):
        return self.name