from typing import Any

import ipd_lab.common.loader as loader
import ipd_lab.engines as engines
import ipd_lab.strategies as strategies
from ipd_lab.common.types import EngineConfigField


def main():
    strategy_class_list = loader.load_classes(strategies, strategies.Strategy)
    engine_class_list = loader.load_classes(engines, engines.Engine)

    # Make a display list for the strategies and classes
    strategy_display_list: str = "\n".join(
        f" {i:^3} | {strategy.__name__}"
        for i, strategy in enumerate(strategy_class_list, start=1)
    )
    engine_display_list: str = "\n".join(
        f" {i:^3} | {engine.__name__}"
        for i, engine in enumerate(engine_class_list, start=1)
    )

    # Ask for the engine to use
    chosen_engine: int
    print("Choose your engine:")
    print(engine_display_list + "\n")
    while True:
        try:
            value = int(input("Enter the engine number: "))
            if 0 < value <= len(engine_class_list):
                chosen_engine = value - 1
                break
        except:
            pass
    print(f"Chose engine {engine_class_list[chosen_engine].__name__}\n")

    # Select strategies
    strategy_remove_list: list[int] = []
    selection_done: bool = False
    while not selection_done:
        print(f"Strategies list:\n{strategy_display_list}")
        # Ask for list to remove
        while True:
            try:
                value = input(
                    "Enter the strategy number to remove "
                    "(Press Enter to save, 0 to redo): "
                )
                if not value:
                    selection_done = True
                    break

                value = int(value)
                if 0 < value <= len(strategy_class_list):
                    strategy_remove_list.append(value - 1)
                elif value == 0:
                    strategy_remove_list = []
                    break
            except:
                pass
    selected_strategy_class_list = []
    for n in range(len(strategy_class_list)):
        if n in strategy_remove_list:
            print(f"Removed strategy {strategy_class_list[n].__name__}")
            continue
        selected_strategy_class_list.append(strategy_class_list[n])

    # Get configuration options from the engine
    engine: engines.Engine = engine_class_list[chosen_engine]()
    engine.set_strategies(selected_strategy_class_list)
    engine_config_options: dict[str, EngineConfigField] = (
        engine.get_configuration()
    )

    # Get the user input for the configs
    engine_config_list: dict[str, Any] = {}
    while True:
        print("\n--Engine Configuration--\n")
        print("| Label: Type = Default Value |")
        # Get the value for each entry
        for entry in engine_config_options:
            proceed: bool = False
            while not proceed:  # Retry until a value is assigned
                try:
                    # Extract data for easier use
                    label: str = engine_config_options[entry].label
                    default_value = engine_config_options[entry].default
                    value_type = engine_config_options[entry].type

                    # Display the data

                    print(
                        f"| {label}: {value_type.__name__} ="
                        f" {default_value}|"
                    )
                    value = input(
                        "Enter the value " "(press Enter for default value): "
                    )

                    if not value:
                        engine_config_list[entry] = default_value
                    else:
                        value = value_type(value)
                        engine_config_list[entry] = value
                    break
                except ValueError:
                    print(f"Error, invalid input type!")

        # Ask if the values are good
        print("\n\nConfiguration to be used:")
        for entry in engine_config_list:
            print(
                f"{engine_config_options[entry].label} = "
                f"{engine_config_list[entry]}"
            )
        value = input("Press Enter to proceed, input anything to retry: ")
        if value:
            print("Retrying...")
            continue

        print("Trying to set the configuration...")
        response = engine.set_configuration(engine_config_list)
        if not response[0]:
            print("Failed! Engine response:")
            print(response[1])
            print("Retrying...")
            continue
        print("Success!")
        break


if __name__ == "__main__":
    main()
