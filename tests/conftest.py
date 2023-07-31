import pytest

from shape_files import ShapefileType


@pytest.fixture(scope="session")
def valid_accept_review_payload():
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
        "actor": {
            "id": "https://review-service.org/",
            "name": "Review Service",
            "type": "Service"
        },
        "context": {
            "id": "https://doi.org/10.1101/2022.10.06.511170"
        },
        "id": "urn:uuid:572b8e81-d92f-4ed5-8178-cc7f04f44cd1",
        "object": {
            "id": "urn:uuid:0370c0fb-bb78-4a9b-87f5-bed307a509dd",
            "object": "https://preprint-repository.org/repository/preprint/201203/421/",
            "type": [
              "Offer",
              "coar-notify:ReviewAction"
            ]
        },
        "origin": {
            "id": "https://review-service.org/",
            "inbox": "https://review-service.org/inbox",
            "type": "Service"
        },
        "target": {
            "id": "https://preprint-repository.org/",
            "inbox": "https://preprint-repository.org/inbox",
            "type": "Service"
        },
        "type": [
            "Accept",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }


@pytest.fixture(scope="session")
def valid_announce_review_payload():
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
        "actor": {
            "id": "https://review-service.org/",
            "name": "Review Service",
            "type": "Service"
        },
        "context": {
            "id": "https://doi.org/10.1101/2022.10.06.511170"
        },
        "id": "urn:uuid:572b8e81-d92f-4ed5-8178-cc7f04f44cd1",
        "object": {
            "id": "https://review-service.org/reviews/1223155",
            "ietf:cite-as": "10.5072/zenodo.1223155",
            "type": [
                "Document",
                "sorg:Review"
            ]
        },
        "origin": {
            "id": "https://review-service.org/",
            "inbox": "https://review-service.org/inbox",
            "type": "Service"
        },
        "target": {
            "id": "https://preprint-repository.org/",
            "inbox": "https://preprint-repository.org/inbox",
            "type": "Service"
        },
        "type": [
            "Announce",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }


@pytest.fixture(scope="session")
def valid_payloads(
    valid_announce_review_payload,
    valid_accept_review_payload,
):
    return {
        ShapefileType.ACCEPT_REVIEW: valid_accept_review_payload,
        ShapefileType.ANNOUNCE_REVIEW: valid_announce_review_payload,
    }
