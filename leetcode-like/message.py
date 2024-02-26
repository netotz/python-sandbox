"""
And now here is my secret
               ^15
And now her ...
And now ...
    
There is an animal with four legs
"""

from ctypes.wintypes import LARGE_INTEGER
import pytest


def crop_message(message: str, max_length: int) -> str:
    if len(message) <= max_length:
        return message

    words = []

    first = 0

    # O(n)
    for i, c in enumerate(message):
        if c == " ":
            words.append((first, len(message[first:i])))
            first = i + 1

    current_sum = 4
    last_word_pos = 0

    # O(n)
    for i, (f, l) in enumerate(words):
        current_sum += l + (0 if f == 0 else 1)

        if current_sum > max_length:
            last_word_pos = i - 1
            break

    if last_word_pos < 0:
        return "..."

    last_word_start, last_word_len = words[last_word_pos]
    last_char_pos = last_word_start + last_word_len - 1
    substring = message[: last_char_pos + 1]

    print(words)

    return substring + " ..."


@pytest.mark.parametrize(
    "message,max_length,expected",
    [
        ("And now here is my secret", 15, "And now ..."),
        ("There is an animal with four legs", 15, "There is an ..."),
        ("super dog", 4, "..."),
        ("how are you", 20, "how are you"),
    ],
)
def test_crop_message(message, max_length, expected):
    assert crop_message(message, max_length) == expected
