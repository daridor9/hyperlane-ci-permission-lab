"""Harmless static fixture for the controlled review-integrity experiment."""


def average(values: list[int]) -> float:
    """Return the arithmetic mean without handling an empty input."""
    return sum(values) / len(values)


# Deterministic known defect: importing or running this file raises
# ZeroDivisionError because the input list is empty.
KNOWN_DEFECT = average([])
