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

    words = []

    first = 0
    current_sum = 4
    last_inserted = -1

    # O(n)
    for i, c in enumerate(message):
        if c != " ":
            continue

        word_len = len(message[first:i])
        words.append((first, word_len))
        first = i + 1
        last_inserted += 1

        current_sum += word_len + (0 if last_inserted == 0 else 1)

        if current_sum > max_length:
            break

    last_inserted -= 1

    if last_inserted < 0:
        return "..."

    last_word_start, last_word_len = words[last_inserted]
    last_char_pos = last_word_start + last_word_len - 1
    substring = message[: last_char_pos + 1]

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
