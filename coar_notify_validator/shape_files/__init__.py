from enum import Enum


class ShapefileType(Enum):
    ACCEPT_REVIEW = "accept-review-shape"

    ACKNOWLEDGE_AND_REJECT = "acknowledge-and-reject-shape"
    ACKNOWLEDGE_AND_TENTATIVE_ACCEPT = "acknowledge-and-tentative-accept-shape"
    ACKNOWLEDGE_AND_TENTATIVE_REJECT = "acknowledge-and-tentative-reject-shape"

    ANNOUNCE = "announce-shape"
    ANNOUNCE_ENDORSE = "announce-endorse-shape"
    ANNOUNCE_INGEST = "announce-ingest-shape"
    ANNOUNCE_RELATIONSHIP = "announce-relationship-shape"
    ANNOUNCE_REVIEW = "announce-review-shape"

    OFFER_ENDORSE = "offer-endorse-shape"
    OFFER_INGEST = "offer-ingest-shape"
    OFFER_REVIEW = "offer-review-shape"

    UNDO = "undo-shape"
