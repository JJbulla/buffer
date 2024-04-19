import unittest

# from buffer.src.base import Buffer
# from base import Buffer
from src.base import Buffer


class TestBuffer(unittest.TestCase):
    """Test the Buffer class."""

    def setUp(self) -> None:
        self.buffer_fifo = Buffer("FIFO")
        self.buffer_lifo = Buffer("LIFO")

    def test_buffer_initialization(self):
        """Test the initialization of the buffer."""
        self.assertEqual(self.buffer_fifo.size(), 0)

    def test_buffer_insert(self):
        """Test the insertion of an item into the buffer."""
        buffer = self.buffer_fifo
        buffer.insert(1)
        self.assertEqual(buffer.size(), 1)

    def test_buffer_extract_fifo(self):
        """Test the extraction of an item from the buffer."""
        buffer = self.buffer_fifo
        buffer.insert(1)
        buffer.insert(2)
        self.assertEqual(buffer.extract(), 1)

    def test_buffer_extract_lifo(self):
        """Test the extraction of an item from the buffer."""
        buffer = self.buffer_lifo
        buffer.insert(1)
        buffer.insert(2)
        self.assertEqual(buffer.extract(), 2)

    def test_buffer_last_item(self):
        """Test the extraction of the last item from the buffer."""
        buffer = self.buffer_fifo
        buffer.insert(1)
        buffer.insert(2)
        self.assertEqual(buffer.last_item(), 2)

    def test_buffer_find_element(self):
        """Test the finding of an element in the buffer."""
        buffer = self.buffer_fifo
        buffer.insert(1)
        self.assertTrue(buffer.find_element(1), 1)

    def test_buffer_find_element_with_error(self):
        """Test the finding of an element in the buffer."""
        buffer = self.buffer_fifo
        with self.assertRaises(Exception):
            buffer.find_element(1)

    def test_buffer_show(self):
        """Test the showing of the buffer contents."""
        buffer = self.buffer_fifo
        buffer.insert(1)
        buffer.insert(2)
        self.assertEqual(buffer.show(), "1, 2")

    def test_buffer_invalid_policy(self):
        """Test the validation of the buffer policy."""
        with self.assertRaises(ValueError):
            self.buffer_fifo._validate_policy("INVALID_POLICY")

    def test_buffer_invalid_policy_by_value_error(self):
        """Test the validation of the buffer policy."""
        with self.assertRaises(ValueError):
            self.buffer_fifo._validate_policy(1)

    def test_buffer_extract_empty(self):
        """Test the extraction of an item from an empty buffer."""
        buffer = self.buffer_lifo
        with self.assertRaises(Exception):
            buffer.extract()

    def test_buffer_last_item_empty(self):
        """Test the extraction of the last item from an empty buffer."""
        buffer = self.buffer_lifo
        with self.assertRaises(Exception):
            buffer.last_item()

    def test_buffer_show_empty(self):
        """Test the showing of the buffer contents."""
        buffer = self.buffer_fifo
        with self.assertRaises(Exception):
            buffer.show()
