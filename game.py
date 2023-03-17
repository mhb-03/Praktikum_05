import random

class Hero:
    def __init__(self, name, health, attackpower, armorlevel, dodge_chance, crit_chance, crit_damage):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.armorlevel = armorlevel
        self.dodge_chance = dodge_chance
        self.crit_chance = crit_chance
        self.crit_damage = crit_damage
    
    @staticmethod
    def _process_attack(attacker, defender, attack_power):
        # Check if the attack is dodged
        if random.random() < defender.dodge_chance:
            print(f"{defender.name} menghindar dari serangan {attacker.name}")
            return

        # Calculate critical hit multiplier
        crit_multiplier = 1.0
        if random.random() < attacker.crit_chance:
            crit_multiplier = attacker.crit_damage
            print(f"{attacker.name} melakukan serangan CRITICAL!")

        # Calculate damage taken by opponent and update health
        attack_diterima = attack_power/defender.armorlevel*crit_multiplier
        defender.health -= attack_diterima
        print(f"{attacker.name} menyerang {defender.name}, serangan terasa: {attack_diterima:.2f}, darah tersisa {defender.health:.2f}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        Hero._process_attack(self, lawan, self.attackpower)

    def diserang(self, lawan, attackpower_lawan):
        Hero._process_attack(lawan, self, attackpower_lawan)


sniper = Hero('sniper', 100, 20, 5, 0.3, 0.35, 2.0)
rikimaru = Hero('rikimaru', 100, 10, 10, 0.3, 0.5, 2.0)

sniper.serang(rikimaru)
print()

rikimaru.serang(sniper)
print()

rikimaru.serang(sniper)
print()

rikimaru.serang(sniper)
print()

rikimaru.serang(sniper)
print()

rikimaru.serang(sniper)
print()

rikimaru.serang(sniper)