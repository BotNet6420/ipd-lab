from types import ModuleType
from typing import Type, List
import pkgutil, importlib, inspect


def load_classes(package: ModuleType, base_class: Type) -> List[Type]:
    """
    Dynamically discover and load all concrete subclasses of a given base class
    from the submodules of a package.

    This function imports each submodule within the provided package, inspects
    its members, and collects any classes that inherit from the specified
    base class. Abstract classes are excluded, so only instantiable subclasses
    are returned.

    Args:
        package (ModuleType): The imported package to search (not a string).
            Example: ``import package`` then pass ``package``.
        base_class (Type): The base class to match subclasses of.

    Returns:
        List[Type]: A list of discovered concrete subclass types.
            These can be instantiated or used directly.
    """
    classes: List[Type] = []

    package_path = package.__path__
    prefix = package.__name__ + "."

    # Iterate over each submodule in the package
    for _, name, ispkg in pkgutil.iter_modules(package_path, prefix):
        module = importlib.import_module(name)

        # Iterate over each class of the module
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, base_class) and obj is not base_class:
                if not inspect.isabstract(obj):  # skip abstract subclasses
                    classes.append(obj)

    return classes
