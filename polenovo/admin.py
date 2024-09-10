from django.contrib import admin
from .models import Plants, Team, Expert, CheckList
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class PlantsAdmin(admin.ModelAdmin):
    list_display = 'title', 'titleL','family', 'maxPoints',
# класс обработки данных


class PlantsResource(resources.ModelResource):

    class Meta:
        model = Plants

# вывод данных на странице
class PlantsAdmin(ImportExportModelAdmin):
    resource_classes = [PlantsResource]

admin.site.register(Plants, PlantsAdmin)

@admin.register(Team)

class TeamAdmin(admin.ModelAdmin):
    list_display = "title","school","points","expert",


@admin.register(Expert)

class ExpertAdmin(admin.ModelAdmin):
    list_display = "name",

@admin.register(CheckList)

class CheckListAdmin(admin.ModelAdmin):
    list_display = "team","plant","vid",'fam'
