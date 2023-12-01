# Decorator pattern is used to dynamically add
# a new feature to an object without changing its implementation.
# It differs from #inheritance because the new feature is added
# only to that particular object, not to the entire subclass


class TextTag:
    """Represents a base text tag"""

    def __init__(self, text: str) -> None:
        self._text = text

    def render(self) -> str:
        # Basic rendering method for the text
        return self._text


class BoldWrapper(TextTag):
    """Wraps a tag in <b>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        # Renders the wrapped text in <b> tags
        return f"<b>{self._wrapped.render()}</b>"


class ItalicWrapper(TextTag):
    """Wraps a tag in <i>"""

    def __init__(self, wrapped: TextTag) -> None:
        self._wrapped = wrapped

    def render(self) -> str:
        # Renders the wrapped text in <i> tags
        return f"<i>{self._wrapped.render()}</i>"


def main():
    """
    # Demonstration of Design Patterns and Principles

    # Create a simple text tag and wrap it in both bold and italic tags
    >>> simple_hello = TextTag("hello, world!")
    >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    # Display the original and the specially formatted text
    >>> print("before:", simple_hello.render())
    before: hello, world!

    >>> print("after:", special_hello.render())
    after: <i><b>hello, world!</b></i>
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
