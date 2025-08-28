from abc import ABC, abstractmethod
from typing import Tuple

from common.types import RoundInfo


class Strategy(ABC):
    @abstractmethod
    def play(
        self,
        last_moves: Tuple[bool, bool] | Tuple[()],
        round_info: RoundInfo
    ) -> bool:
        """
        Abstract base class for strategies.

        Extend this class and implement the play() method to define your
        strategy.
        Place your .py file in the 'strategies' folder for auto-loading.

        Usage tip: Use last_moves and round_info to decide your move.
        Store any persistent state inside self if needed.

        Args:
            last_moves (Tuple[bool, bool] | Tuple[()]):
                A tuple of (my_last_move, opponent_last_move).
                None if this is the first round.
            round_info (RoundInfo):
                Information about the current round provided by the engine.

        Returns:
            bool: True for cooperate, False for defect.
        """
        pass
