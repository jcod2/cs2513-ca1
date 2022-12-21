# Name:                 Jamie O'Donovan
# Student Number:       121776739

from ca1_monster_fin import Monster
from ca1_spell_fin import Spell
from ca1_planeswalker_fin import Planeswalker

class dmu107(Monster):
    '''
    Sheoldred, the Apocalypse
    '''
    def __init__(self, **kwargs:str) -> None:
        super().__init__(str(self.__class__.__name__), **kwargs)

class knd101(Spell):
    '''
    Invoke Despair
    '''
    def __init__(self, **kwargs:str) -> None:
        super().__init__(str(self.__class__.__name__), **kwargs)

class dmu97(Planeswalker):
    '''
    Liliana of the Veil
    '''
    def __init__(self, **kwargs:str) -> None:
        super().__init__(str(self.__class__.__name__), **kwargs)

dmu107_name = "Sheoldred, the Apocalypse"
dmu107_type = {"type": ["Legendary Creature", "Phyrexian Praetor"]}
dmu107_info = {"rarity": "Mythic Rare", "card_num": 107, "set": "Dominaria United"}
dmu107_stats = {"mana cost": "2BB", "power": 4, "toughness": 5}
dmu107_effect = {"effect": ["Deathtouch", "Whenever you draw a card, you gain 2 life.", "Whenever an opponent draws a card, they lose 2 life."]}
dmu107_quote = "\"Gix failed. I shall not.\""

sheoldred = dmu107(name=dmu107_name, type=dmu107_type, info=dmu107_info, stats=dmu107_stats, effect=dmu107_effect, quote=dmu107_quote)

print(sheoldred.monster_type)
print(sheoldred.monster_name)
print(sheoldred.monster_stats)
print(sheoldred.monster_effect)
print(sheoldred.monster_quote)
print(sheoldred)

knd101_name = "Invoke Despair"
knd101_type = "Sorcery"
knd101_info = {"rarity": "Rare", "card_num": 101, "set": "Kamigawa: Neon Dynasty"}
knd101_stats = {"mana cost": "1BBBB"}
knd101_effect = {"effect": ["Target opponent sacrifices a creature. If they can't, they lose 2 life and you draw a card. Then repeat this process for an enchantment and a planeswalker."]}
knd101_quote = "Although officials said it was a sewer failure, the people whispered that it was a warning of night's reach."

invoke = knd101(name=knd101_name, type=knd101_type, info=knd101_info, stats=knd101_stats, effect=knd101_effect, quote=knd101_quote)

print(invoke.spell_type)
print(invoke.spell_name)
print(invoke.spell_stats)
print(invoke.spell_effect)
print(invoke.spell_quote)
print(invoke)

dmu97_name = "Liliana of the Veil"
dmu97_type = {"type": ["Legendary Planeswalker", "Lilana"]}
dmu97_info = {"rarity": "Mythic Rare", "card_num": 97, "set": "Dominaria United"}
dmu97_stats = {"mana cost": "1BB", "health": 3}
dmu97_effect = {"effect": ["+1: Each player discards a card.", "−2: Target player sacrifices a creature.", "−6: Separate all permanents target player controls into two piles. That player sacrifices all permanents in the pile of their choice."]}
dmu97_quote = ""

liliana = dmu97(name=dmu97_name, type=dmu97_type, info=dmu97_info, stats=dmu97_stats, effect=dmu97_effect, quote=dmu97_quote)

print(liliana.planeswalker_type)
print(liliana.planeswalker_name)
print(liliana.planeswalker_stats)
print(liliana.planeswalker_effect)
print(liliana.planeswalker_quote)
print(liliana)

# given how cards interact with each other most attributes can be changed via card effects
sheoldred.set_monster_stats({"power": 8})
print(sheoldred.monster_stats["power"])

invoke.set_spell_stats({"mana cost": "3BBBB"})
print(invoke.spell_stats["mana cost"])

liliana.set_planeswalker_stats({"health": 6})
print(liliana.planeswalker_stats["health"])

sheoldred.set_monster_stats({"toughness": 10})
print(sheoldred.monster_stats["toughness"])

sheoldred.set_monster_type({"type": "Elf Warrior?"})
print(sheoldred.monster_type["type"])

hand = sheoldred.monster_name, invoke.spell_name, liliana.planeswalker_name, sheoldred.monster_name, invoke.spell_name
print(hand)