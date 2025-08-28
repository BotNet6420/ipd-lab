from dataclasses import dataclass
from typing import Dict, Tuple, Type, Any


@dataclass
class RoundInfo:
    """
    RoundInfo represents the information about the current round
    provided by the engine to a strategy.

    Strategy authors can rely on non-optional fields being present
    in every call.
    Additional fields may be added in future versions;
    Currently, there are no optional field. Once added,
    optional fields may not be provided by the engine.
    strategies can safely ignore fields they don’t use.

    Attributes:
        round_number (int): Index of the current round (starting at 0).
        payoff_matrix (Dict[Tuple[bool, bool], Tuple[int, int]]):
            The standard payoff for all possible moves:
            Keys are tuples (my_move, opponent_move) where True = cooperate,
            False = defect.
            Values are tuples (my_score, opponent_score).
    """
    round_number: int
    payoff_matrix: Dict[Tuple[bool, bool], Tuple[int, int]]


@dataclass
class EngineConfigField:
    """
    Represents a single configuration field provided by an engine.

    Engines can define any number of these fields in their configuration
    dictionary.
    The main app can then read the label, type and default value
    in order to display them and to receive inputs,
    allowing a uniform way to handle custom engine configurations.

    Attributes:
        type (Type): The type of this field.
        default (Any): The default value of this field.
        label (str): The text to be displayed as the name of this field.
    """
    type: Type
    default: Any
    label: str
