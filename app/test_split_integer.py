import pytest
from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value(
    value: int,
    num_parts: int
) -> None:
    assert sum(split_integer(value, num_parts)) == value


def test_should_split_into_equal_parts_when_value_divisible_by_parts(
    value: int,
    num_parts: int
) -> None:
    assert len(set(split_integer(value, num_parts))) == 1


def test_should_return_part_equals_to_value_when_split_into_one_part(
    value: int
) -> None:
    split_once = split_integer(value, 1)
    assert split_once[0] == value


def test_parts_should_be_sorted_when_they_are_not_equal(
    value: int,
    num_parts: int
) -> None:
    sort_split = sorted(split_integer(value, num_parts))
    assert sort_split == split_integer(value, num_parts)


def test_should_add_zeros_when_value_is_less_than_number_of_parts(
    value: int,
    num_parts: int
) -> None:
    assert len(split_integer(value, num_parts)) == num_parts
