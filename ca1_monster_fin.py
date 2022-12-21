# Name:                 Jamie O'Donovan
# Student Number:       121776739

# basic concept, crate cards similar to magic the gathering cards as python classes

from ca1_functions_fin import CardExceptionError
from typing import ClassVar

class Monster:
    '''
    monster cards class, has at a minimum\n
    name,mana cost, power value, toughness value\n
    with optional data such as lore text, effect text
    '''

    # attributes
    # using https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid=574587 as an example
        # card code, card set and card number
        # (i.e., du107)
    __card_code = ClassVar[str]
    # name, self explanatory
    # (i.e., "Sheoldred, the Apocalypse")
    __monster_name = ClassVar[str]
    # misc info such as rarity, set etc.
    # (i.e., "Mythic", "Dominaria United")
    __monster_info = ClassVar[dict]
    # type, typically the race of the monster sometimes a class, can have multiple 
    # (i.e., "Phyrexian Prator")
    __monster_type = ClassVar[dict[list]]
    # mana cost, power, toughness 
    # (i.e., 2any2black (2BB), 4, 5)
    __monster_stats = ClassVar[dict[list]]
    # monster effects, can have none could have 3, varies
    # (i.e., "Deathtouch", "Whenever you draw a card, you gain 2 life.", "Whenever an opponent draws a card, they lose 2 life.")
    __monster_effect = ClassVar[dict[list]]
    # lore of the card if available, cards will sometimes hae a quote attacked as flavour text
    #  (i.e., "Gix failed, I shall not.")
    __monster_quote = ClassVar[str]

    def __init__(self, class_name, **kwargs) -> None:
        self.__card_code = class_name
        problem = "Problem with constructor"
        # input data from a dictionary using **kwargs 
        if len(kwargs) != 0:
            if "name" in kwargs.keys():
                self.__monster_name = kwargs["name"]
            else:
                raise CardExceptionError(f"{problem} name for {self.__class__.__name__}.")
            if "type" in kwargs.keys():
                self.__monster_type = kwargs["type"]
            else:
                raise CardExceptionError(f"{problem} type for {self.__class__.__name__}.")
            if "info" in kwargs.keys():
                self.__monster_info = kwargs["info"]
            else:
                raise CardExceptionError(f"{problem} info for {self.__class__.__name__}.")
            if "stats" in kwargs.keys():
                self.__monster_stats = kwargs["stats"]
            else:
                raise CardExceptionError(f"{problem} stats for {self.__class__.__name__}.")
            if "effect" in kwargs.keys():
                if kwargs["effect"] == "":
                    self.__monster_effect = "This card has no effect."
                else:
                    self.__monster_effect = kwargs["effect"]
            else:
                raise CardExceptionError(f"{problem} effect for {self.__class__.__name__}.")
            if "quote" in kwargs.keys():
                if kwargs["quote"] == "":
                    self.__monster_quote = "This card has no quote."
                else:
                    self.__monster_quote = kwargs["quote"]
            else:
                raise CardExceptionError(f"{problem} quote for {self.__class__.__name__}.")

    @property
    def card_code(self):
        return self.__card_code

    @card_code.setter
    def card_code(self, toa: str):
        self.__card_code = toa
    # get and set for each attribute
    def get_monster_name(self) -> dict:
        return self.__monster_name
    def set_monster_name(self, top: dict) -> None:
        self.__check_monster_dict_values(self.__monster_name, top)
    monster_name = property(get_monster_name, set_monster_name)

    def get_monster_type(self) -> dict:
        return self.__monster_type
    def set_monster_type(self, top: dict) -> None:
        self.__check_monster_dict_values(self.__monster_type, top)
    monster_type = property(get_monster_type, set_monster_type)

    def get_monster_stats(self) -> dict:
        return self.__monster_stats
    def set_monster_stats(self, sop: dict) -> None:
        self.__check_monster_dict_values(self.__monster_stats, sop)  
    monster_stats = property(get_monster_stats, set_monster_stats)

    def get_monster_effect(self) -> dict:
        return self.__monster_effect
    def set_monster_effect(self, sop: dict) -> None:
        self.__check_monster_dict_values(self.__monster_effect, sop)  
    monster_effect = property(get_monster_effect, set_monster_effect)

    def get_monster_quote(self) -> dict:
        return self.__monster_quote
    def set_monster_quote(self, sop: dict) -> None:
        self.__check_monster_dict_values(self.__monster_quote, sop)  
    monster_quote = property(get_monster_quote, set_monster_quote)

    def __check_monster_dict_values(self, start_dict: dict, input_dict: dict) -> dict:
        for key in input_dict.keys():
            if key in start_dict.keys():
                start_dict[key] = input_dict[key]
            else:
                raise CardExceptionError(f"Problem with the input key: \"{key}\" for {self.__class__.__name__}.")
        return start_dict
        
    def __str__(self) -> str:
        # format output for type(s)
        i = 0
        type_string = ""
        for value in self.__monster_type["type"]:
            if i == 0:
                type_string += f"{value}"
            else:
                type_string += f", {value}"
            i += 1
        # format output for stats
        i = 0
        stats_string = ""
        for value in self.__monster_stats:
            if i == 0:
                stats_string += f"{value} {self.__monster_stats[value]}"
            else:
                stats_string += f"\n\t\t{value} {self.__monster_stats[value]}"
            i += 1
        # format output for effect
        i = 0
        effect_string = ""
        for value in self.__monster_effect["effect"]:
            if i == 0:
                effect_string += f"{value}"
            else:
                effect_string += f"\n\t\t{value}"
            i += 1
        # get info
        info = self.__monster_info
        # get quote
        quote = self.__monster_quote
        # return formatted data
        return f"Class:\t\t{Monster.__name__}\nCard Code: \t{self.__class__.__name__}\nName: \t\t{self.monster_name}\nRarity: \t{info['rarity']}\nSet: \t\t{info['set']}\nNumber: \t{info['card_num']}\nType: \t\t{type_string}\nStats: \t\t{stats_string}\nEffect(s):\t{effect_string}\nQuote:\t\t{quote}"