from django.contrib import admin

# Register your models here.
from .models import Profile,Question,Answer

class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

admin.site.register(Profile)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)