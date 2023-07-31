import pytest

from coar_notify_validator.shape_files import ShapefileType
from coar_notify_validator.validate import validate
from coar_notify_validator.exceptions import GraphParseError


@pytest.mark.parametrize(
    "shape_file_type, expected",
    [
        (
                ShapefileType.OFFER_REVIEW,
                (True, []),
        ),
        (
                ShapefileType.ACCEPT_REVIEW,
                (True, []),
        ),
        (
                ShapefileType.ANNOUNCE_REVIEW,
                (True, []),
        ),
    ],
)
def test_can_successfully_validate(shape_file_type, expected, valid_payloads):
    assert validate(shape_file_type, valid_payloads[shape_file_type]) == expected


@pytest.mark.parametrize(
    "shape_file_type, expected",
    [
        (
                ShapefileType.OFFER_REVIEW,
                (
                        False,
                        [
                            {
                                "focus_node": "<https://review-service.org/",
                                "message": "Less than 1 values on <https://review-service.org/-ldp:inbox",
                                "result_path": "ldp:inbox",
                                "severity": "sh:Violation",
                                "source_shape": "ex:InboxShape"
                            }
                        ]
                ),
        ),
        (
                ShapefileType.ACCEPT_REVIEW,
                (
                        False,
                        [
                            {
                                "focus_node": "<https://preprint-repository.org/",
                                "message": "Less than 1 values on <https://preprint-repository.org/-ldp:inbox",
                                "result_path": "ldp:inbox",
                                "severity": "sh:Violation",
                                "source_shape": "ex:InboxShape"
                            }
                        ]
                ),
        ),
        (
                ShapefileType.ANNOUNCE_REVIEW,
                (
                        False,
                        [
                            {
                                "focus_node": "<https://preprint-repository.org/",
                                "message": "Less than 1 values on <https://preprint-repository.org/-ldp:inbox",
                                "result_path": "ldp:inbox",
                                "severity": "sh:Violation",
                                "source_shape": "ex:InboxShape"
                            }

                        ]
                ),
        ),
    ],
)
def test_can_fail_validation(shape_file_type, expected, invalid_payloads):
    assert validate(shape_file_type, invalid_payloads[shape_file_type]) == expected


def test_raises_exception_when_empty_payload_passed():
    with pytest.raises(GraphParseError):
        validate(ShapefileType.ANNOUNCE_REVIEW, {})
