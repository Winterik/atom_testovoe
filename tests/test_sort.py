from ..scripts.ColorSorting import ColorSorting
from typing import Final
import pytest

TEST_CASES: Final = [
    ('ССЗСКЗЗЗККСЗССКЗ', 'ЗСК', 'ЗЗЗЗЗЗССССССКККК'),  # positive case
    ('ССЗСКЗЗЗККСЗССКЗ', 'ЗКС', 'ЗЗЗЗЗЗККККСССССС'),  # positive case
    ('ССЗСКЗЗЗККСЗССКЗ', 'КЗС', 'ККККЗЗЗЗЗЗСССССС'),  # positive case
    ('ССЗСКЗЗЗККСЗССКЗ', 'КСЗ', 'ККККССССССЗЗЗЗЗЗ'),  # positive case
    ('ССЗСКЗЗЗККСЗССКЗ', 'СКЗ', 'ССССССККККЗЗЗЗЗЗ'),  # positive case
    ('ССЗСКЗЗЗККСЗССКЗ', 'СЗК', 'ССССССЗЗЗЗЗЗКККК'),  # positive case
    ('ССЗСКЗЗЗККСЗССКЗQQAZ', 'ЗСК', ValueError),      # negative case
    ('ССЗСКЗЗЗККСЗССКЗQQAZ', 'ЗК', ValueError),       # negative case
    ('ССЗСКЗЗЗККСЗССКЗ', 'ЗСКQ', ValueError),         # negative case
    ('ССЗСКЗЗЗККСЗССКЗ', 'ЗЗСКК', ValueError),        # negative case
    (123, 'ЗСК', ValueError),                         # negative case
    ('QWERTY', 123, ValueError),                      # negative case
]

@pytest.mark.parametrize(
    'sequence, colors, expected',
    TEST_CASES,
    ids=[f'Test case {i + 1}' for i, (sequence, _, _) in enumerate(TEST_CASES)]
)
def test_sort(sequence, colors, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            ColorSorting.sequence_sorting(sequence, colors)
    else:
        assert ColorSorting.sequence_sorting(sequence, colors) == expected, 'Ошибка выполнения теста!'