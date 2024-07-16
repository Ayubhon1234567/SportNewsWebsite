from django.contrib import admin

from pages.models import NewsModel, ContactModel, PlayerModel, DefendersModel, ManagerModel, MatchModel, GoalModel, \
    AssistModel


# Register your models here.


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['name','author']
    search_fields = ['description','image']
    list_filter = ['created_at','updated_at']

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display =['name','subject']
    search_fields = ['email','subject']
    list_filter = ['created_at','updated_at']

@admin.register(PlayerModel)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display = ['name','position']
    search_fields = ['number','image']

@admin.register(DefendersModel)
class DefenderModelAdmin(admin.ModelAdmin):
    list_display = ['name','number']
    search_fields = ['position','image']

@admin.register(ManagerModel)
class MangerModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['position','image']


@admin.register(MatchModel)
class MatchModelAdmin(admin.ModelAdmin):
    list_display = ['team1','team2','city1','city2']
    search_fields = ['balance1','balance2','time','image1','image2','turnir','time']
    list_filter = ['date']

@admin.register(GoalModel)
class GoalModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['score','number']

@admin.register(AssistModel)
class AssistModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['score','number']




