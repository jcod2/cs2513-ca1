# Name:                 Jamie O'Donovan
# Student Number:       121776739

# basic concept, crate cards similar to magic the gathering cards as python classes

from ca1_functions_fin import CardExceptionError
from typing import ClassVar

class Spell:
    '''
    spell cards class, has at a minimum\n
    name,mana cost, power value, toughness value\n
    with optional data such as lore text, effect text
    '''

    # attributes
    # using https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=548399 as an example
    # name, self explanatory
    # (i.e., "Invoke Despair")
    __spell_name = ClassVar[str]
    # misc info such as rarity, set etc.
    # (i.e., "Rare", "Kamigawa: Neon Dynasty")
    __spell_info = ClassVar[dict[list]]
    # type, how the spell can be cast, sorcery, instant etc.
    # (i.e., "Sorcery")
    __spell_type = ClassVar[str]
    # mana cost
    # (i.e., 1any4black (4BB))
    __spell_stats = ClassVar[dict]
    # spell effects, can have none could have 3, varies
    # (i.e., "Target opponent sacrifices a creature. If they can't, they lose 2 life and you draw a card. Then repeat this process for an enchantment and a planeswalker.")
    __spell_effect = ClassVar[dict[list]]
    # lore of the card if available, cards will sometimes hae a quote attacked as flavour text
    #  (i.e., "Although officials said it was a sewer failure, the people whispered that it was a warning of night's reach.")
    __spell_quote = ClassVar[str]

    def __init__(self, class_name, **kwargs) -> None:
        self.__card_code = class_name
        problem = "Problem with constructor"
        # input data from a dictionary using **kwargs 
        if len(kwargs) != 0:
            if "name" in kwargs.keys():
                self.__spell_name = kwargs["name"]
            else:
                raise CardExceptionError(f"{problem} name for {self.__class__.__name__}.")
            if "type" in kwargs.keys():
                self.__spell_type = kwargs["type"]
            else:
                raise CardExceptionError(f"{problem} type for {self.__class__.__name__}.")
            if "info" in kwargs.keys():
                self.__spell_info = kwargs["info"]
            else:
                raise CardExceptionError(f"{problem} info for {self.__class__.__name__}.")
            if "stats" in kwargs.keys():
                self.__spell_stats = kwargs["stats"]
            else:
                raise CardExceptionError(f"{problem} stats for {self.__class__.__name__}.")
            if "effect" in kwargs.keys():
                self.__spell_effect = kwargs["effect"]
            else:
                raise CardExceptionError(f"{problem} effect for {self.__class__.__name__}.")
            if "quote" in kwargs.keys():
                self.__spell_quote = kwargs["quote"]
            else:
                raise CardExceptionError(f"{problem} quote for {self.__class__.__name__}.")

    @property
    def card_code(self):
        return self.__card_code

    @card_code.setter
    def card_code(self, toa: str):
        self.__card_code = toa
    # get and set for each attribute
    def get_spell_name(self) -> dict:
        return self.__spell_name
    def set_spell_name(self, top: dict) -> None:
        self.__check_spell_dict_values(self.__spell_name, top)
    spell_name = property(get_spell_name, set_spell_name)

    def get_spell_type(self) -> dict:
        return self.__spell_type
    def set_spell_type(self, top: dict) -> None:
        self.__check_spell_dict_values(self.__spell_type, top)
    spell_type = property(get_spell_type, set_spell_type)

    def get_spell_stats(self) -> dict:
        return self.__spell_stats
    def set_spell_stats(self, sop: dict) -> None:
        self.__check_spell_dict_values(self.__spell_stats, sop)  
    spell_stats = property(get_spell_stats, set_spell_stats)

    def get_spell_effect(self) -> dict:
        return self.__spell_effect
    def set_spell_effect(self, sop: dict) -> None:
        self.__check_spell_dict_values(self.__spell_effect, sop)  
    spell_effect = property(get_spell_effect, set_spell_effect)

    def get_spell_quote(self) -> dict:
        return self.__spell_quote
    def set_spell_quote(self, sop: dict) -> None:
        self.__check_spell_dict_values(self.__spell_quote, sop)  
    spell_quote = property(get_spell_quote, set_spell_quote)

    def __check_spell_dict_values(self, start_dict: dict, input_dict: dict) -> dict:
        for key in input_dict.keys():
            if key in start_dict.keys():
                start_dict[key] = input_dict[key]
            else:
                raise CardExceptionError(f"Problem with the input key: \"{key}\" for {self.__class__.__name__}.")
        return start_dict
        
    def __str__(self) -> str:
        # format output for stats
        i = 0
        stats_string = ""
        for value in self.__spell_stats:
            if i == 0:
                stats_string += f"{value} {self.__spell_stats[value]}"
            else:
                stats_string += f"\n\t\t{value} {self.__spell_stats[value]}"
            i += 1
        # format output for effect
        i = 0
        effect_string = ""
        for value in self.__spell_effect["effect"]:
            if i == 0:
                effect_string += f"{value}"
            else:
                effect_string += f"\n\t\t{value}"
            i += 1
        # type info
        types = self.__spell_type
        # get info
        info = self.__spell_info
        # get quote
        quote = self.__spell_quote
        # return formatted data
        return f"Class:\t\t{Spell.__name__}\nCard Code: \t{self.__class__.__name__}\nName: \t\t{self.spell_name}\nRarity: \t{info['rarity']}\nSet: \t\t{info['set']}\nNumber: \t{info['card_num']}\nType: \t\t{types}\nStats: \t\t{stats_string}\nEffect(s):\t{effect_string}\nQuote:\t\t{quote}"