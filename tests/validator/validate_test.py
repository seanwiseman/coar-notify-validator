import pytest

from shape_files import ShapefileType
from validator.validate import validate


@pytest.mark.parametrize(
    "shape_file_type, expected",
    [
        (
            ShapefileType.ANNOUNCE_REVIEW,
            (True, []),
        ),
        (
            ShapefileType.ACCEPT_REVIEW,
            (True, []),
        ),
    ],
)
def test_can_successfully_validate(shape_file_type, expected, valid_payloads):
    assert validate(shape_file_type, valid_payloads[shape_file_type]) == expected
