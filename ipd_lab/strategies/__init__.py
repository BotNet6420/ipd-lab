from abc import ABC, abstractmethod
from typing import Tuple

from ipd_lab.common.types import RoundInfo


class Strategy(ABC):
    """
    Abstract base class for strategies.

    Extend this class and implement the methods to define
    your strategy.
    Place your .py file in the 'strategies' folder for auto-loading.
    """

    @abstractmethod
    def play(
        self, last_moves: Tuple[bool, bool] | Tuple[()], round_info: RoundInfo
    ) -> bool:
        """
        Called by the engine for the strategy to make a decision.

        This method is called by the engine on each round,
        for the strategy to decide whether to cooperate or defect.

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

    @abstractmethod
    def get_description(self) -> str:
        """
        Returns:
            str: A description of this strategy to be displayed in the UI.
        """
        pass
