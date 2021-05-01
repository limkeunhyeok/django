from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['quest_text']
    list_filter = ['pub_date']
    list_display = ('quest_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['quest_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)