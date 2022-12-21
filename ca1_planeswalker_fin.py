# Name:                 Jamie O'Donovan
# Student Number:       121776739

# basic concept, crate cards similar to magic the gathering cards as python classes

from ca1_functions_fin import CardExceptionError
from typing import ClassVar

class Planeswalker:
    '''
    planeswalker cards class, has at a minimum\n
    name,mana cost, health value\n
    with effect text
    '''

    # attributes
    # using https://gatherer.wizards.com/pages/card/details.aspx?name=Liliana%20of%20the%20Veil as an example
    # name, self explanatory
    # (i.e., "Liliana of the Veil")
    __planeswalker_name = ClassVar[str]
    # misc info such as rarity, set etc.
    # (i.e., "Legendary", "Dominaria United")
    __planeswalker_info = ClassVar[dict[list]]
    # type, how the planeswalker can be cast, sorcery, instant etc.
    # (i.e., "Legendary Planeswalker")
    __planeswalker_type = ClassVar[dict[list]]
    # mana cost, starting hp
    # (i.e., 1any2black (1BB), 3)
    __planeswalker_stats = ClassVar[dict[list]]
    # planeswalker effects, can have none could have 3, varies
    # (i.e., "+1: Each player discards a card.", "−2: Target player sacrifices a creature.", "−6: Separate all permanents target player controls into two piles. That player sacrifices all permanents in the pile of their choice.")
    __planeswalker_effect = ClassVar[dict[list]]
    # lore of the card if available, cards will sometimes hae a quote attacked as flavour text
    #  (i.e., )
    __planeswalker_quote = ClassVar[str]

    def __init__(self, class_name, **kwargs) -> None:
        self.__card_code = class_name
        problem = "Problem with constructor"
        # input data from a dictionary using **kwargs 
        if len(kwargs) != 0:
            if "name" in kwargs.keys():
                self.__planeswalker_name = kwargs["name"]
            else:
                raise CardExceptionError(f"{problem} name for {self.__class__.__name__}.")
            if "type" in kwargs.keys():
                self.__planeswalker_type = kwargs["type"]
            else:
                raise CardExceptionError(f"{problem} type for {self.__class__.__name__}.")
            if "info" in kwargs.keys():
                self.__planeswalker_info = kwargs["info"]
            else:
                raise CardExceptionError(f"{problem} info for {self.__class__.__name__}.")
            if "stats" in kwargs.keys():
                self.__planeswalker_stats = kwargs["stats"]
            else:
                raise CardExceptionError(f"{problem} stats for {self.__class__.__name__}.")
            if "effect" in kwargs.keys():
                self.__planeswalker_effect = kwargs["effect"]
            else:
                raise CardExceptionError(f"{problem} effect for {self.__class__.__name__}.")
            if "quote" in kwargs.keys():
                if kwargs["quote"] == "":
                    self.__planeswalker_quote = "This card has no quote."
                else:
                    self.__planeswalker_quote = kwargs["quote"]
            else:
                raise CardExceptionError(f"{problem} quote for {self.__class__.__name__}.")

    @property
    def card_code(self):
        return self.__card_code

    @card_code.setter
    def card_code(self, toa: str):
        self.__card_code = toa
    # get and set for each attribute
    def get_planeswalker_name(self) -> dict:
        return self.__planeswalker_name
    def set_planeswalker_name(self, top: dict) -> None:
        self.__check_planeswalker_dict_values(self.__planeswalker_name, top)
    planeswalker_name = property(get_planeswalker_name, set_planeswalker_name)

    def get_planeswalker_type(self) -> dict:
        return self.__planeswalker_type
    def set_planeswalker_type(self, top: dict) -> None:
        self.__check_planeswalker_dict_values(self.__planeswalker_type, top)
    planeswalker_type = property(get_planeswalker_type, set_planeswalker_type)

    def get_planeswalker_stats(self) -> dict:
        return self.__planeswalker_stats
    def set_planeswalker_stats(self, sop: dict) -> None:
        self.__check_planeswalker_dict_values(self.__planeswalker_stats, sop)  
    planeswalker_stats = property(get_planeswalker_stats, set_planeswalker_stats)

    def get_planeswalker_effect(self) -> dict:
        return self.__planeswalker_effect
    def set_planeswalker_effect(self, sop: dict) -> None:
        self.__check_planeswalker_dict_values(self.__planeswalker_effect, sop)  
    planeswalker_effect = property(get_planeswalker_effect, set_planeswalker_effect)

    def get_planeswalker_quote(self) -> dict:
        return self.__planeswalker_quote
    def set_planeswalker_quote(self, sop: dict) -> None:
        self.__check_planeswalker_dict_values(self.__planeswalker_quote, sop)  
    planeswalker_quote = property(get_planeswalker_quote, set_planeswalker_quote)

    def __check_planeswalker_dict_values(self, start_dict: dict, input_dict: dict) -> dict:
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
        for value in self.__planeswalker_type["type"]:
            if i == 0:
                type_string += f"{value}"
            else:
                type_string += f", {value}"
            i += 1
        # format output for stats
        i = 0
        stats_string = ""
        for value in self.__planeswalker_stats:
            if i == 0:
                stats_string += f"{value} {self.__planeswalker_stats[value]}"
            else:
                stats_string += f"\n\t\t{value} {self.__planeswalker_stats[value]}"
            i += 1
        # format output for effect
        i = 0
        effect_string = ""
        for value in self.__planeswalker_effect["effect"]:
            if i == 0:
                effect_string += f"{value}"
            else:
                effect_string += f"\n\t\t{value}"
            i += 1
        # get info
        info = self.__planeswalker_info
        # get quote
        quote = self.__planeswalker_quote
        # return formatted data
        return f"Class:\t\t{Planeswalker.__name__}\nCard Code: \t{self.__class__.__name__}\nName: \t\t{self.planeswalker_name}\nRarity: \t{info['rarity']}\nSet: \t\t{info['set']}\nNumber: \t{info['card_num']}\nType: \t\t{type_string}\nStats: \t\t{stats_string}\nEffect(s):\t{effect_string}\nQuote:\t\t{quote}"