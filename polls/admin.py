from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):  ##Can be StackedInLine too
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
	('Questions', 			{'fields': ['question']}),
	('Date Information', {'fields':['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
# Register your models here.
