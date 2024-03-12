from weapon import fists
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.hp_max = health
        self.weapon = fists
    
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(0, target.health)
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, 
                 name: str, 
                 health: int) -> None:
        
        super().__init__(name=name, health=health)
        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color = "green2")

    def equip(self,weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} has equipped {weapon.name}!")
    
    def drop(self) -> None:
        self.weapon = self.default_weapon
        print(f"{self.name} has dropped the {self.weapon.name}!")

class Enemy(Character):
    def __init__(self, 
                 name: str, 
                 health: int,
                 weapon) -> None:
        
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self, color = "red")
