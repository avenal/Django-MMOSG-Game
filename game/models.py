from django.db import models

class Village(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30)
    points  = models.IntegerField()
    map_x = models.IntegerField()
    map_y = models.IntegerField()
    morale = models.IntegerField(default = 100)
    owned_by = models.ForeignKey('accounts.CustomUser', models.DO_NOTHING, blank=True)
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if self.id is None:
        # village not created
            super(Village, self).save(*args, **kwargs)
            palace = Building.objects.get(name="Palace")
            sawmill = Building.objects.get(name="Sawmill")
            quarry = Building.objects.get(name="Quarry")
            iron_mine = Building.objects.get(name="IronMine")
            
            village_palace = VillageBuilding(lvl=1, bonus=3, building=palace, village=self)
            village_palace.save()

            village_sawmill = VillageBuilding(lvl=1, bonus=120, building=sawmill, village=self)
            village_sawmill.save()

            village_quarry = VillageBuilding(lvl=1, bonus=120, building=quarry, village=self)
            village_quarry.save()

            village_iron_mine = VillageBuilding(lvl=1, bonus=120, building=iron_mine, village=self)
            village_iron_mine.save()

        else:
            pass

class BuildingType(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=25)
    def __str__(self):
        return str(self.name)

class Building(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=25)
    building_type = models.ForeignKey(BuildingType, models.DO_NOTHING)
    def __str__(self):
        return str(self.name)


class Resource(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    def __str__(self):
        return str(self.name)

class VillageResource(models.Model):
    id = models.AutoField(primary_key = True)
    resource = models.ForeignKey(Resource, models.DO_NOTHING)
    quantity = models.IntegerField()
    village = models.ForeignKey(Village, models.DO_NOTHING)
    def __str__(self):
        return str(self.resource) + ": " + str(self.village)

class Unit(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=20)
    time_to_recruit = models.FloatField()
    speed = models.IntegerField()
    attack = models.IntegerField()
    deffence = models.IntegerField()
    loot = models.IntegerField()
    def __str__(self):
        return str(self.name)

class ResourceCost(models.Model):
    id = models.AutoField(primary_key = True)
    resource = models.ForeignKey(Resource, models.DO_NOTHING)
    cost = models.IntegerField()
    def __str__(self):
        return str(self.resource)+": "+str(self.cost)

class ResourceUnitCost(models.Model):
    id = models.AutoField(primary_key = True)
    resource_cost = models.ForeignKey(ResourceCost, models.DO_NOTHING)
    unit = models.ForeignKey(Unit, models.DO_NOTHING)
    def __str__(self):
        return str(self.resource_cost)+ ": " + str(self.unit)

class ResourceBuildingCost(models.Model):
    id = models.AutoField(primary_key = True)
    resource_cost = models.ForeignKey(ResourceCost, models.DO_NOTHING)    
    building = models.ForeignKey(Building, models.DO_NOTHING)    
    def __str__(self):
        return str(self.resource_cost) + ": " + str(self.building)

class VillageArmy(models.Model):
    id = models.AutoField(primary_key = True)
    unit = models.ForeignKey(Unit, models.DO_NOTHING)
    quantity = models.IntegerField()
    village = models.ForeignKey(Village, models.DO_NOTHING)
    def __str__(self):
        return str(self.quantity)+ " " + str(self.unit) + " " + str(self.village)

class Research(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=25)
    def __str__(self):
        return str(self.name)

class VillageResearch(models.Model):
    id = models.AutoField(primary_key = True)
    research = models.ForeignKey(Research, models.DO_NOTHING)
    village = models.ForeignKey(Village, models.DO_NOTHING)
    def __str__(self):
        return str(self.research) + " " + str(self.village)

class VillageBuilding(models.Model):
    id = models.AutoField(primary_key = True)
    lvl = models.IntegerField(default = 0)
    bonus = models.IntegerField()
    building = models.ForeignKey(Building, models.DO_NOTHING)
    village = models.ForeignKey(Village, models.DO_NOTHING)
    def __str__(self):
        return str(self.building) +" "+ str(self.lvl) +" "+ str(self.village)