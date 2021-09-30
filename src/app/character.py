from app.attack import Attack
from app.battlefieldItemInterface import BattlefieldItemInterface


class Character(BattlefieldItemInterface):

    MIN_HEALTH = 0
    MAX_HEALTH = 1000
    
    def __init__(self, level = 1):
        self.health = 1000
        self.level = level
        self.alive = True

    def recieveDamage(self, damageAmount):
        self.health -= min(damageAmount, self.health)
        self.__recalculateLifeStatus()

    def __recalculateLifeStatus(self):
        if self.health == self.MIN_HEALTH:
            self.alive = False

    def dealDamage(self, target: BattlefieldItemInterface, attack):
        if not self.__amIHurtingMyself(self, target):
            target.recieveDamage(attack.calculateDamage(self, target))

    def recieveHealth(self, healthAmount):
        if (self.alive):
            self.health = min(healthAmount + self.health, self.MAX_HEALTH)

    def __amIHurtingMyself(self, attacker, target):
        return attacker == target

    def setLevel(self, level):
        self.level = level
