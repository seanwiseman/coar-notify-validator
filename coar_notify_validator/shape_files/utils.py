import os

from .types import ShapefileType


SHAPE_FILES_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/shape_files/data"


SHAPE_FILE_TYPE_MAP = {
    "Accept:coar-notify:ReviewAction": ShapefileType.ACCEPT_REVIEW,

    "Reject": ShapefileType.ACKNOWLEDGE_AND_REJECT,
    "TentativeAccept": ShapefileType.ACKNOWLEDGE_AND_TENTATIVE_ACCEPT,
    "TentativeReject": ShapefileType.ACKNOWLEDGE_AND_TENTATIVE_REJECT,

    "Announce": ShapefileType.ANNOUNCE,
    "Announce:coar-notify:EndorsementAction": ShapefileType.ANNOUNCE_ENDORSE,
    "Announce:coar-notify:IngestAction": ShapefileType.ANNOUNCE_INGEST,
    "Announce:coar-notify:RelationshipAction": ShapefileType.ANNOUNCE_RELATIONSHIP,
    "Announce:coar-notify:ReviewAction": ShapefileType.ANNOUNCE_REVIEW,

    "Offer:coar-notify:EndorsementAction": ShapefileType.OFFER_ENDORSE,
    "Offer:coar-notify:IngestAction": ShapefileType.OFFER_INGEST,
    "Offer:coar-notify:ReviewAction": ShapefileType.OFFER_REVIEW,

    "Undo": ShapefileType.UNDO,
}


def read_shape_file(file_name: str) -> str:
    file_path = os.path.join(SHAPE_FILES_DIR, f"{file_name}.ttl")
    with open(file_path, 'r', encoding="utf-8") as shape_file:
        return shape_file.read()


def get_shape_file_type_from_notification_type(notification_type: list[str] | str) \
        -> ShapefileType | None:
    """
    Get the shape file type from a notification type.

    :param notification_type: list[str] | str
    :return: ShapefileType | None

    Examples:

    >>> get_shape_file_type_from_notification_type(["Accept", "coar-notify:ReviewAction"])
    ShapefileType.ACCEPT_REVIEW

    >>> get_shape_file_type_from_notification_type("Reject")
    ShapefileType.ACKNOWLEDGE_AND_REJECT

    >>> get_shape_file_type_from_notification_type("Invalid Type")
    None

    """
    if isinstance(notification_type, str):
        _notification_type = notification_type
    else:
        _notification_type = ":".join(notification_type)

    return SHAPE_FILE_TYPE_MAP.get(_notification_type, None)
