from .models import Unit, Village, VillageArmy
from django_q.tasks import schedule
import datetime

def attack(from_id, to_id, warriors, swordsmans):
    warrior = Unit.objects.get(name="Warrior")
    swordsman = Unit.objects.get(name="Swordsman")
    attack_power = warriors * warrior.attack + swordsmans * swordsman.attack
    print(str(attack_power))
    attacker = Village.objects.get(id=from_id)
    defender = Village.objects.get(id=to_id)
    defender_army = VillageArmy.objects.filter(village=defender)
    defence_power = 0
    
    for unit in defender_army:
        defence_power += unit.quantity * unit.unit.defence
        print(str(defence_power))
    ratio = attack_power/defence_power
    att_warriors_left = warriors
    att_swordsmans_left = swordsmans
    if ratio <= 1:
        att_warriors_left = 0
        att_swordsmans_left = 0
        for unit in defender_army:
            unit.quantity = int(unit.quantity * (1-ratio))
            unit.save()
    else:
        att_warriors_left = int(att_warriors_left * (1/ratio))
        att_swordsmans_left = int(att_swordsmans_left * (1/ratio))
        for unit in defender_army:
            unit.quantity = 0
            unit.save()
        schedule('game.tasks.attack_back',
         from_id, att_warriors_left, att_swordsmans_left, 
         schedule_type='O', repeats=1, next_run=datetime.datetime.now()+datetime.timedelta(minutes=1))        

def attack_back(from_id, warriors, swordsmans):
    village = Village.objects.get(id=from_id)
    army = village.get_army()
    warriors_army = army.get(unit__name="Warrior")
    swordsman_army = army.get(unit__name="Swordsman")
    warriors_army.quantity+=warriors
    warriors_army.save()
    swordsman_army.quantity+=swordsmans
    swordsman_army.save()