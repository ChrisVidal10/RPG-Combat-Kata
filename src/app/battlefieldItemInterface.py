from abc import abstractmethod
from abc import ABCMeta


class BattlefieldItemInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def recieveDamage(self):
        pass
