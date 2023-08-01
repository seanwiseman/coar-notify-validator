import pytest

from coar_notify_validator.shape_files import ShapefileType
from coar_notify_validator.validate import validate_by_payload_type
from coar_notify_validator.exceptions import GraphParseError


@pytest.mark.parametrize(
    "notification_type, shape_file_type, expected",
    [
        (
            ["Offer", "coar-notify:ReviewAction"],
            ShapefileType.OFFER_REVIEW,
            (True, []),
        ),
        (
            ["Accept", "coar-notify:ReviewAction"],
            ShapefileType.ACCEPT_REVIEW,
            (True, []),
        ),
        (
            ["Announce", "coar-notify:ReviewAction"],
            ShapefileType.ANNOUNCE_REVIEW,
            (True, []),
        ),
    ],
)
def test_can_successfully_validate(notification_type, shape_file_type, expected, valid_payloads):
    assert validate_by_payload_type(notification_type, valid_payloads[shape_file_type]) == expected


@pytest.mark.parametrize(
    "notification_type, shape_file_type, expected",
    [
        (
            ["Offer", "coar-notify:ReviewAction"],
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
            ["Accept", "coar-notify:ReviewAction"],
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
            ["Announce", "coar-notify:ReviewAction"],
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
def test_can_fail_validation(notification_type, shape_file_type, expected, invalid_payloads):
    assert validate_by_payload_type(notification_type, invalid_payloads[shape_file_type]) == expected


def test_raises_exception_when_empty_payload_passed():
    with pytest.raises(GraphParseError):
        validate_by_payload_type(["Offer", "coar-notify:ReviewAction"], {})