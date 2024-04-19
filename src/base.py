"""A module for a Buffer class that handles insertion and extraction of items."""

from typing import Optional, Union
from src import constants
from utils import utils


class Buffer:
    """A Buffer class that handles insertion and extraction of items.

    This class supports two policies for item extraction -
    FIFO (First In First Out) and LIFO (Last In First Out).

    Attributes:
        policy (str): The policy for item extraction. Should be 'FIFO' or 'LIFO'.

    Example:
        >>> buffer = Buffer('FIFO')
        >>> buffer.insert(1)
        >>> item = buffer.extract()
        >>> print(item)
        1
    Methods:
    insert(item: Any) -> None:
        Inserts an item into the buffer.
        Example:
            >>> buffer.insert(2)
            >>> print(buffer.size())
            2

    extract() -> Optional[Any]:
        Extracts an item from the buffer according to the policy.
        Example:
            >>> item = buffer.extract()
            >>> print(item)
            2

    size() -> int:
        Returns the size of the buffer.
        Example:
            >>> print(buffer.size())
            1

    last_item() -> Any:
        Returns the last item in the buffer.
        Example:
            >>> buffer.insert(3)
            >>> print(buffer.last_item())
            3

    find_element(element: Any) -> None:
        Checks if an element is in the buffer.
        Example:
            >>> buffer.find_element(3)
            This element is in the position 0

    show() -> str:
        Returns the contents of the buffer.
        Example:
            >>> print(buffer.show())
            3
    """

    def __init__(self, policy):
        """Initialize the buffer with a policy."""
        self.buffer = []
        self._is_valid = self._validate_policy(policy)
        self._policy = self._define_policy(policy)

    def _validate_policy(self, policy) -> Union[bool, any]:
        """Validate the policy of the buffer."""
        if isinstance(policy, str) is False:
            raise ValueError(constants.VALID_POLICY)

        if policy.upper() not in constants.VALID_ORDER:
            raise ValueError(
                f"Invalid policy: {self._policy}. Expected 'FIFO' or 'LIFO'."
            )

        return True

    def _define_policy(self, policy) -> Union[str, any]:
        """Define the policy of the buffer."""
        return "FIFO" if policy.upper() == "FIFO" else "LIFO"

    def insert(self, item: any) -> None:
        """Insert an item into the buffer."""
        self.buffer.append(item)

    def size(self) -> int:
        """Return the size of the buffer."""
        return len(self.buffer)

    def find_element(self, element: Optional[int]) -> Union[int, any]:
        """Check if an element is in the buffer."""
        found_element = [value for value in self.buffer if element in self.buffer]
        if found_element:
            return found_element[0]
        return utils.custom_exception(constants.BUFFER_NOT_FOUND)

    @utils.is_empty
    def extract(self) -> int:
        """Extract an item from the buffer according to the policy."""
        return self.buffer.pop(0) if self._policy == "FIFO" else self.buffer.pop()

    @utils.is_empty
    def last_item(self) -> int:
        """Return the last item in the buffer."""
        return self.buffer[-1]

    @utils.is_empty
    def show(self) -> str:
        """Return the contents of the buffer."""
        return ", ".join(str(item) for item in self.buffer)
