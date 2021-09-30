import pytest
from app.attack import Attack
from app.character import Character
from app.damageLevelStategy import DamageLevelStrategy

class TestCharacter(object):

    INITIAL_HEALTH = 1000

    def setup_method(self):
        self.character = Character()
        self.character2 = Character()

    def test_create_character(self):
        assert self.character.health == 1000
        assert self.character.level == 1
        assert self.character.alive == True

    def test_character_can_deal_damage_to_characters(self):
        damage = Attack(DamageLevelStrategy(), 100)
        self.character.dealDamage(self.character2, damage)
        assert self.INITIAL_HEALTH - damage.damage == self.character2.health

    def test_character_recieve_damage_greater_than_current_health(self):
        damage = Attack(DamageLevelStrategy(), 2000)
        self.character.dealDamage(self.character2, damage)
        assert self.character2.health == 0
        assert self.character2.alive == False

    @pytest.mark.parametrize(
        "testInputDamage, testInputHeal, isAlive, expected",
        [(Attack((DamageLevelStrategy()), 50), 100, True, 1000),
         (Attack((DamageLevelStrategy()), 500), 100, True, 600),
         (Attack((DamageLevelStrategy()), 0), 100, True, 1000),
         (Attack((DamageLevelStrategy()), 1000), 100, False, 0)],
    )
    def test_character_being_healed(self, testInputDamage, testInputHeal, isAlive, expected):
        damage = testInputDamage
        health = testInputHeal
        self.character.dealDamage(self.character2, damage)
        self.character2.recieveHealth(health)
        assert self.character2.alive == isAlive
        assert self.character2.health == expected

    def test_character_cant_damage_itself(self):
        damage = Attack((DamageLevelStrategy()), 50)
        self.character.dealDamage(self.character, damage)
        assert self.character.health == self.INITIAL_HEALTH


    @pytest.mark.parametrize(
        "levelAttacker, levelTarget, expectedHealth",
        [(1, 6, 950),
        (6, 1, 850)]
    )
    def test_character_deal_damage_with_differents_levels(self, levelAttacker, levelTarget, expectedHealth):
        damage = Attack((DamageLevelStrategy()), 100)
        self.character.setLevel(levelAttacker)
        self.character2.setLevel(levelTarget)
        self.character.dealDamage(self.character2, damage)
        assert self.character2.health == expectedHealth

    
