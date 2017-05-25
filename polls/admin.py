# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)



####There are numerous options and functionality to customize the admin site in Django.

