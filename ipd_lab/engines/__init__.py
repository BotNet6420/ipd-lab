from abc import ABC, abstractmethod
from typing import Any, Type

from ipd_lab.strategies import Strategy
from ipd_lab.common.types import EngineConfigField


class Engine(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """
        Returns:
            str: A description of this engine to be displayed in the UI.
        """
        pass

    @abstractmethod
    def get_configuration(self) -> dict[str, EngineConfigField]:
        """
        Retrieve the engine's list of configurable options.

        This method is used by the main app to fetch the list of
        all available customization options provided by the engine.
        These configuration options are later returned to the engine
        using the set_configuration method.

        This method will not be called until after the strategy list
        has been provided via set_strategies

        Returns:
            dict[str, EngineConfigField]: A dictionary mapping
            each option's internal name to its corresponding
            EngineConfigField.
        """
        pass

    @abstractmethod
    def set_configuration(
        self, configuration: dict[str, Any]
    ) -> tuple[bool, str]:
        """
        Set the engine's configurable options.

        This method is used by the main app to send the list of
        engine configuration options alongside their values
        to initialize the engine.

        Args:
              configuration (dict[str, Any]): A dictionary mapping
              each options given internal name to its corresponding
              user given value.

        Returns:
            tuple[bool, str]: A tuple with the first item indicating
            success (True) or failure (False), and a string
            to be displayed to the user.
        """
        pass

    @abstractmethod
    def set_strategies(self, strategies: list[Type[Strategy]]) -> None:
        """
        Set the strategies to be used by the engine.

        This method is used by the main app to send a list of strategies
        to the engine.
        The list will contain the classes themselves, and not instances.

        This method will be called before get_configuration. This should
        allow the engine to dynamically adjust the available
        configuration options base on the available strategies
        (e.g. include a chance field for each strategy).

        Args:
             strategies (list[Type[Strategy]]): A list of Strategy
             subclasses to be used by the engine.
        """
        pass

    @abstractmethod
    def run_simulation(self) -> str:
        """
        Run the simulation using the provided configurations

        This method will be called by the main app after
        set_configuration has been called to run the simulation
        using the previously provided configurations and strategies.

        Returns:
            A string representing the results of the simulation.
        """
        pass
