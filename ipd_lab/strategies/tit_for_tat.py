from typing import Tuple

from ipd_lab.common.types import RoundInfo
from . import Strategy


class TitForTat(Strategy):
    def play(
        self, last_moves: Tuple[bool, bool] | Tuple[()], round_info: RoundInfo
    ) -> bool:
        if not last_moves:
            return True

        return last_moves[1]

    def get_description(self) -> str:
        return "test"
