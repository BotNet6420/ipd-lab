import ipd_lab.common.loader as loader
import ipd_lab.engines as engines
import ipd_lab.strategies as strategies


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
                value = int(
                    input(
                        "Enter the strategy number to remove "
                        "(0 to save, -1 to redo): "
                    )
                )
                if 0 < value <= len(strategy_class_list):
                    strategy_remove_list.append(value - 1)
                elif value == 0:
                    selection_done = True
                    break
                elif value == -1:
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

    # TODO: Set up the engine
    engine = engine_class_list[chosen_engine]()
    engine.set_strategies(selected_strategy_class_list)


if __name__ == "__main__":
    main()
