#_*_coding:utf-8_*_
__author__ = 'bobby'
__date__ = '2018-03-24 20:33'
import re
from django import forms

from article.models import Article

class ArticleForms(forms.ModelForm):
    class Meta:
        model=Article
        fields=['content','title']