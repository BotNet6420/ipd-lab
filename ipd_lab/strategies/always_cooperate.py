from typing import Tuple

from ipd_lab.common.types import RoundInfo
from . import Strategy


class AlwaysCooperate(Strategy):
    def play(
        self, last_moves: Tuple[bool, bool] | Tuple[()], round_info: RoundInfo
    ) -> bool:
        return True

    def get_description(self) -> str:
        return "test"
