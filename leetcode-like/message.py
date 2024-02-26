"""
And now here is my secret
               ^15
And now her ...
And now ...
    
There is an animal with four legs
"""

import pytest


def crop_message(message: str, max_length: int) -> str:
    if len(message) <= max_length:
        return message

    last_space_pos = -1

    # O(n)
    for i, c in enumerate(message):
        if c == " ":
            last_space_pos = i

        # +1 because of 0-indexing
        # +4 because length of " ..."
        if i + 1 + 4 > max_length:
            break

    if last_space_pos < 0:
        return "..."

    return message[:last_space_pos] + " ..."


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
