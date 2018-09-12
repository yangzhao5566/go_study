"""
Abstract Factory
"""


class Frog(object):
    def __int__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def interact_with(self, obstacle):
        """不同类型玩家遇到的不同障碍"""
        print("{} the Frog encounters {} and {}!".format(
            self, obstacle, obstacle.action()
        ))


class Bug(object):
    def __str__(self):
        return "a bug"

    def action(self):
        return "eats it"


class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Ork(object):
    def __str__(self):
        return "an evil ork"

    def action(self):
        return "kill it"


class WizardWorld(object):
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------ Wizard World -------"

    def make_obstacle(self):
        return Ork()


class GameEnvironment(object):
    """抽象工厂，根据不同的玩家类型创建不同的角色和障碍"""
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

