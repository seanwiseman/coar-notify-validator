import pytest

from shape_files import ShapefileType


@pytest.fixture(scope="session")
def valid_offer_review_payload():
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
        "actor": {
            "id": "https://orcid.org/0000-0002-1825-0097",
            "name": "Josiah Carberry",
            "type": "Person"
        },
        "id": "urn:uuid:572b8e81-d92f-4ed5-8178-cc7f04f44cd1",
        "object": {
            "id": "https://research-organisation.org/repository/preprint/201203/421/",
            "ietf:cite-as": "https://doi.org/10.5555/12345680",
            "type": "sorg:AboutPage",
            "url": {
                  "id": "https://research-organisation.org/repository/preprint/201203/421/content.pdf",
                  "mediaType": "application/pdf",
                  "type": [
                    "Article",
                    "sorg:ScholarlyArticle"
                  ]
            }
        },
        "origin": {
            "id": "https://research-organisation.org/repository",
            "inbox": "https://research-organisation.org/inbox/",
            "type": "Service"
          },
        "target": {
            "id": "https://review-service.org/",
            "inbox": "https://review-service.org/inbox",
            "type": "Service"
        },
        "type": [
            "Offer",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }


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
    valid_offer_review_payload,
    valid_accept_review_payload,
    valid_announce_review_payload,
):
    return {
        ShapefileType.OFFER_REVIEW: valid_offer_review_payload,
        ShapefileType.ACCEPT_REVIEW: valid_accept_review_payload,
        ShapefileType.ANNOUNCE_REVIEW: valid_announce_review_payload,
    }


@pytest.fixture(scope="session")
def invalid_offer_review_payload():
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
        "actor": {
            "id": "https://orcid.org/0000-0002-1825-0097",
            "name": "Josiah Carberry",
            "type": "Person"
        },
        "id": "urn:uuid:572b8e81-d92f-4ed5-8178-cc7f04f44cd1",
        "object": {
            "id": "https://research-organisation.org/repository/preprint/201203/421/",
            "ietf:cite-as": "https://doi.org/10.5555/12345680",
            "type": "sorg:AboutPage",
            "url": {
                  "id": "https://research-organisation.org/repository/preprint/201203/421/content.pdf",
                  "mediaType": "application/pdf",
                  "type": [
                    "Article",
                    "sorg:ScholarlyArticle"
                  ]
            }
        },
        "origin": {
            "id": "https://research-organisation.org/repository",
            "inbox": "https://research-organisation.org/inbox/",
            "type": "Service"
          },
        "target": {
            "id": "https://review-service.org/",
            # Missing inbox - is required
            "type": "Service"
        },
        "type": [
            "Offer",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }


@pytest.fixture(scope="session")
def invalid_accept_review_payload():
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
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
            # Missing inbox - is required
            "type": "Service"
        },
        "type": [
            "Accept",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }


@pytest.fixture(scope="session")
def invalid_announce_review_payload():
    return {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
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
            # Missing inbox - is required
            "type": "Service"
        },
        "type": [
            "Announce",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }


@pytest.fixture(scope="session")
def invalid_payloads(
    invalid_offer_review_payload,
    invalid_accept_review_payload,
    invalid_announce_review_payload,
):
    return {
        ShapefileType.OFFER_REVIEW: invalid_offer_review_payload,
        ShapefileType.ACCEPT_REVIEW: invalid_accept_review_payload,
        ShapefileType.ANNOUNCE_REVIEW: invalid_announce_review_payload,
    }
