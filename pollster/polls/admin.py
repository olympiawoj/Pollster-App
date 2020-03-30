from django.contrib import admin

# Register your models here.

from.models import Question, Choice

admin.site.site_header = "Pollster Admin" 
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice 
    #how many extra fields do we want
    extra = 3

#name of model and admin
class QuestionAdmin(admin.ModelAdmin):
    #name, dict with fields, 
    #fieldsets is a tuple, so we need a hanging comma
    fieldsets = [(None, {'fields': ['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)