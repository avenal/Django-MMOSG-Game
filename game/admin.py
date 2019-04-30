from django.contrib import admin
from .models import Village, VillageBuilding, VillageArmy, VillageResearch, VillageResource, Resource, Research, Building, BuildingType, Unit, ResourceCost, ResourceBuildingCost, ResourceUnitCost
# Register your models here.
admin.site.register(Village)
admin.site.register(VillageArmy)
admin.site.register(VillageResearch)
admin.site.register(VillageResource)
admin.site.register(Research)
admin.site.register(Resource)
admin.site.register(Building)
admin.site.register(BuildingType)
admin.site.register(Unit)
admin.site.register(ResourceCost)
admin.site.register(ResourceBuildingCost)
admin.site.register(ResourceUnitCost)
admin.site.register(VillageBuilding)
