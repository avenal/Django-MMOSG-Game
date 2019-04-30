from .models import Unit, Village, VillageArmy
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
