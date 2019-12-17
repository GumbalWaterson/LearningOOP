#!/usr/bin/env python3
import random


class Weapon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


default_weapon = Weapon('P225', 15)
first_weapon = Weapon('M4A1-S', 20)
second_weapon = Weapon('AK47', 35)
third_weapon = Weapon('M4A4', 25)
fourth_weapon = Weapon('AUG', 30)
fifth_weapon = Weapon('SG553', 30)
sixth_weapon = Weapon('SSG08', 80)
seventh_weapon = Weapon('AWP', 100)
weapons = [default_weapon, first_weapon, second_weapon,
           third_weapon, fourth_weapon, fifth_weapon,
           sixth_weapon, seventh_weapon]
helmets = [30, 10, 0]


class Fighter():
    def __init__(self, name, HP):
        self.name = name
        self.weapon = random.choice(weapons)
        self.helmet = random.choice(helmets)
        self.hp = HP + self.helmet

    def __str__(self):
        if self.helmet == 0:
            return ("""Welcome to the battle and you are {}
Your weapon is {} with {} damages
Unfortunately you have no protection
Total HPs you have is {}
Good luck have fun!\n""".format(self.name, self.weapon.name,
                    self.weapon.damage, self.hp))
        else:
            return ("""Welcome to the battle and you are {}
Your weapon is {} with {} damages
Congratulations! You have more {} Hps with helmet
Total HPs you have is {}
Good luck have fun!\n""".format(self.name, self.weapon.name,
                    self.weapon.damage, self.helmet, self.hp))

    def speech(self):
        if self.name == 'Counter-Terrorist':
            print('GO GO GO and show who we are!\n\n\n')
        else:
            print("Let's kill them all!\n\n\n")


def attack(attacker, get_attacked_er):
    get_attacked_er.hp = get_attacked_er.hp - attacker.weapon.damage
    print('{} shoots {}'.format(attacker.name,
                                get_attacked_er.name))


def get_attacked(get_attacked_er):
    if get_attacked_er.hp > 0:
        return ("{}'s HP remains {}\n"
                .format(get_attacked_er.name, get_attacked_er.hp))
    else:
        return ('{} died\n'.format(get_attacked_er.name))


def solve(player1, player2):
    '''Trả về tuple tên người thắng cuộc và lượng máu còn lại (int)'''
    print(player1)
    player1.speech()
    print(player2)
    player2.speech()
    rand_choice = random.choice([player1, player2])
    print("{} go first\n".format(rand_choice.name))
    if rand_choice == player1:
        while player1.hp > 0 and player2.hp > 0:
            if player1.hp > 0:
                attack(player1, player2)
            print(get_attacked(player2))
            if player2.hp > 0:
                attack(player2, player1)
            print(get_attacked(player1))
    else:
        while player1.hp > 0 and player2.hp > 0:
            if player2.hp > 0:
                attack(player2, player1)
            print(get_attacked(player1))
            if player1.hp > 0:
                attack(player1, player2)
            print(get_attacked(player2))
    if player1.hp > 0:
        print("{} wins\n".format(player1.name))
        return (player1.name, player1.hp)
    elif player2.hp > 0:
        print("{} wins!!!\n".format(player2.name))
        return (player2.name, player2.hp)


def main():
    # Thay đổi các dòng sau cho phù hợp
    player1 = Fighter('Counter-Terrorist', 100)
    player2 = Fighter('Terrorist', 100)
    print(solve(player1, player2))
    print("\nGAME OVER!!!")


if __name__ == "__main__":
    main()
