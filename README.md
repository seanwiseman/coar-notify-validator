# coar-notify-validator


### Installation

```bash
python setup.py install
```


### Usage

#### Validate a COAR Notify payload against the schema

```python
from shape_files import ShapefileType
from validator.validate import validate

valid_payload = {
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

conforms, errors = validate(ShapefileType.ANNOUNCE_REVIEW, valid_payload)

print(conforms)  # True
print(errors)  # []

invalid_payload = {
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
        # Missing inbox - should be required
        "type": "Service"
    },
    "type": [
        "Announce",
        "coar-notify:ReviewAction"
    ],
    "updated": "2022-10-06T15:00:00.000000"
}

conforms, errors = validate(ShapefileType.ANNOUNCE_REVIEW, invalid_payload)
print(conforms)  # False
print(errors)
# [
#     {
#         "focus_node": "<https://preprint-repository.org/",
#         "message": "Less than 1 values on <https://preprint-repository.org/-ldp:inbox",
#         "result_path": "ldp:inbox",
#         "severity": "sh:Violation",
#         "source_shape": "ex:InboxShape"
#     }
# 
# ]


```