from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass
class RoundInfo:
    """
    RoundInfo represents the information about the current round
    provided by the engine to a strategy.

    Strategy authors can rely on non-optional fields being present
    in every call.
    Currently, there are no optional field. Once added,
    optional fields may not be provided by the engine.
    Additional fields may be added in future versions;
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
