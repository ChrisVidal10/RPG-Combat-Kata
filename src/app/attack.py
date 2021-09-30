

class Attack():
    def __init__(self, damageStrategy, damage):
        self.damageStrategy = damageStrategy
        self.damage = damage

    def calculateDamage(self, attacker, target):
        return self.damageStrategy.calculateDamage(attacker, target, self.damage)
