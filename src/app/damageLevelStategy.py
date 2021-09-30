from app.damageStrategyInterface import DamageStrategyInterface


class DamageLevelStrategy(DamageStrategyInterface):

    LEVEL_DIFFERENCE_FOR_GREATER = 5
    LEVEL_DIFFERENCE_FOR_LOWER = 5
    PORCENTAGE_FOR_GREATER = 1.5
    PORCENTAGE_FOR_LOWER = 0.5
    
    def calculateDamage(self, attacker, target, damageAmount):
        if(self.isAttackerGreaterThanTarget(attacker, target)):
            return damageAmount * self.PORCENTAGE_FOR_GREATER

        if(self.isAttackerLowerThanTarget(attacker, target)):
            return damageAmount * self.PORCENTAGE_FOR_LOWER

        return damageAmount
        
    def isAttackerGreaterThanTarget(self, attacker, target):
        return attacker.level - self.LEVEL_DIFFERENCE_FOR_GREATER >= target.level

    def isAttackerLowerThanTarget(self, attacker, target):
        return attacker.level + self.LEVEL_DIFFERENCE_FOR_LOWER <= target.level