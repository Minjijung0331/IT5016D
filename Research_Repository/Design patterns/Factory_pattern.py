# factory design pattern that defines an interface for creating an object
# but allows subclasses change the type of object

from typing import Dict
from typing import Protocol
from typing import Type


# Protocol to define the interface for Localizer
class Localizer(Protocol):
    def localize(self, msg: str) -> str:
        pass


# Implementation of GreekLocalizer which translates English words to Greek
class GreekLocalizer:
    """A simple localizer a la gettext"""

    def __init__(self) -> None:
        # Translations dictionary for English to Greek
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        # Return translation if available, else return the original message
        return self.translations.get(msg, msg)


# Implementation of EnglishLocalizer which echoes the input message
class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


# Factory function to create instances of Localizer based on the specified language
def get_localizer(language: str = "English") -> Localizer:
    """Factory"""
    # Dictionary mapping language names to their corresponding Localizer classes
    localizers: Dict[str, Type[Localizer]] = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    # Create an instance of the specified Localizer class and return it
    return localizers[language]()


# Main function to demonstrate the usage of localizers
def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")

    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


# Run doctests when the script is executed
if __name__ == "__main__":
    import doctest

    doctest.testmod()
