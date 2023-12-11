#rpg game.py

import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    def is_alive(self):
        return self.health > 0

def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        print("\nPlayer Stats:")
        print(f"Health: {player.health}")
        print(f"Attack: {player.attack}")
        print("\nEnemy Stats:")
        print(f"Health: {enemy.health}")
        print(f"Attack: {enemy.attack}")

        action = input("\nEnter 'attack' to attack: ").lower()

        if action == 'attack':
            player_damage = random.randint(1, player.attack)
            enemy_damage = random.randint(1, enemy.attack)

            print(f"\nYou deal {player_damage} damage to {enemy.name}.")
            enemy.take_damage(player_damage)

            if enemy.is_alive():
                print(f"{enemy.name} deals {enemy_damage} damage to you.")
                player.take_damage(enemy_damage)

    if player.is_alive():
        print(f"\nYou defeated {enemy.name}! You have {player.health} health remaining.")
        return True
    else:
        print(f"\nYou were defeated by {enemy.name}. Game Over!")
        return False

def main():
    print("Welcome to the Simple RPG Game!")

    player_name = input("Enter your character's name: ")
    player = Character(name=player_name, health=50, attack=10, defense=5)

    enemy_list = [
        Character(name="Goblin", health=20, attack=8, defense=2),
        Character(name="Orc", health=30, attack=12, defense=4),
        Character(name="Dragon", health=50, attack=20, defense=10)
    ]

    for enemy in enemy_list:
        if not battle(player, enemy):
            break

if __name__ == "__main__":
    main()
