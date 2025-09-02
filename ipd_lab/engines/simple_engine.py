from typing import Any, Type

from ipd_lab.common import types
from ipd_lab.common.types import EngineConfigField
from ipd_lab.strategies import Strategy
from . import Engine


class SimpleEngine(Engine):
    def __init__(self):
        self.rounds: int = 0
        # E.g. {"TitForTat" : <class ...>, ...}
        self.strategy_list: dict[str, Type[Strategy]] = {}
        # E.g. [(TitForTat, AlwaysDefect), ...]
        self.pairs: list[tuple[str, str]] = []

    def get_description(self) -> str:
        description = (
            "A simple engine that plays a tournament between "
            "strategy pairs, not including versus themselves."
        )
        return description

    def get_configuration(self) -> dict[str, EngineConfigField]:
        conf = EngineConfigField(int, 10, "Number of rounds")
        return {"rounds": conf}

    def set_configuration(
        self, configuration: dict[str, Any]
    ) -> tuple[bool, str]:
        if configuration["rounds"] <= 0:
            return False, "'rounds' was set to a non-positive value!"

        try:
            self.rounds = configuration["rounds"]
        except Exception as e:
            return False, str(e)

        return True, "Success"

    def set_strategies(self, strategies: list[Type[Strategy]]) -> None:
        self.strategy_list = {
            strategy.__name__: strategy for strategy in strategies
        }

        # Make the pairs
        length: int = len(self.strategy_list)
        for i in range(length):
            for j in range(i + 1, length):
                self.pairs.append(
                    (strategies[i].__name__, strategies[j].__name__)
                )

    def run_simulation(self) -> str:
        scores = {strategy: 0 for strategy in self.strategy_list}
        payoff_matrix = {
            (True, True): (3, 3),
            (True, False): (0, 5),
            (False, True): (5, 0),
            (False, False): (1, 1),
        }

        for pair in self.pairs:
            # Make the players
            p1: Strategy = self.strategy_list[pair[0]]()
            p2: Strategy = self.strategy_list[pair[1]]()

            last_moves = ()

            # Play the rounds
            for n in range(self.rounds):
                round_info = types.RoundInfo(
                    round_number=n, payoff_matrix=payoff_matrix
                )

                last_moves: tuple[bool, bool] | tuple[()] = (
                    p1.play(last_moves, round_info),
                    p2.play(last_moves[::-1], round_info),
                )

                score: tuple[int, int] = payoff_matrix[last_moves]

                scores[pair[0]] += score[0]
                scores[pair[1]] += score[1]

        name_width = max(max(len(name) for name in scores), 13)
        score_width = max(max(len(str(score)) for score in scores.values()), 5)
        title: str = (
            f"{'':-^{name_width + score_width + 15}}\n"
            f"| {'Index':^5} | {'Strategy Name':^{name_width}} |"
            f" {'Score':^{score_width}} |\n"
            f"{'':-^{name_width + score_width + 15}}"
        )
        fields: str = "\n".join(
            f"| {i:^5} | {key:^{name_width}} | {scores[key]:^{score_width}} |"
            for i, key in enumerate(scores, start=1)
        )
        table: str = f"{title}\n{fields}"

        result: str = f"Simulation Done! Here are the results:\n\n{table}"

        return result
