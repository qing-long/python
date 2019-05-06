import datetime

from django.contrib import admin
from django.utils import timezone

from .models import Choice, Question

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [(None, {
        'fields': ['question_text']
    }), ('Date information', {
        'fields': ['pub_date'],
        'classes': ['collapse']
    })]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestAdmin)
admin.site.register(Choice)
