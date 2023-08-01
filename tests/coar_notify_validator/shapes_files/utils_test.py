import pytest

from coar_notify_validator.shape_files.types import ShapefileType
from coar_notify_validator.shape_files.utils import get_shape_file_type_from_notification_type


@pytest.mark.parametrize(
    "notification_type, expected",
    [
        (["Accept", "coar-notify:ReviewAction"], ShapefileType.ACCEPT_REVIEW),
        ("Reject", ShapefileType.ACKNOWLEDGE_AND_REJECT),
        ("TentativeAccept", ShapefileType.ACKNOWLEDGE_AND_TENTATIVE_ACCEPT),
        ("TentativeReject", ShapefileType.ACKNOWLEDGE_AND_TENTATIVE_REJECT),
        ("Announce", ShapefileType.ANNOUNCE),
        (["Announce", "coar-notify:EndorsementAction"], ShapefileType.ANNOUNCE_ENDORSE),
        (["Announce", "coar-notify:IngestAction"], ShapefileType.ANNOUNCE_INGEST),
        (["Announce", "coar-notify:RelationshipAction"], ShapefileType.ANNOUNCE_RELATIONSHIP),
        (["Announce", "coar-notify:ReviewAction"], ShapefileType.ANNOUNCE_REVIEW),
        (["Offer", "coar-notify:EndorsementAction"], ShapefileType.OFFER_ENDORSE),
        (["Offer", "coar-notify:IngestAction"], ShapefileType.OFFER_INGEST),
        (["Offer", "coar-notify:ReviewAction"], ShapefileType.OFFER_REVIEW),
        ("Undo", ShapefileType.UNDO),
    ]
)
def test_can_find_shape_file_from_type(notification_type, expected):
    assert get_shape_file_type_from_notification_type(notification_type) == expected
