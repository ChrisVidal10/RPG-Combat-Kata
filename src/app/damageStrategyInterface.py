from abc import abstractmethod
from abc import ABCMeta


class DamageStrategyInterface(metaclass=ABCMeta):

    @abstractmethod
    def calculateDamage(self, attacker, target, damageAmount):
        pass
