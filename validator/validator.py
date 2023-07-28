import logging
import json
from rdflib import *
import pyshacl


_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


shapeFiles = {}

JSONLD = 'json-ld'
TURTLE = 'ttl'


def get_shape_graph(shape_file: str) -> str:
    with open(shape_file, 'r') as f:
        return f.read()


def is_valid(shape_filename: str, payload: dict) -> bool:
    instance_data_graph = None
    shacl_validation_graph = get_shape_graph(shape_filename)

    try:
        instance_data_graph = Graph().parse(data=json.dumps(payload), format=JSONLD)
    except Exception:
        _logger.exception('Failed to parse payload as JSON-LD')

    if instance_data_graph:
        conforms, report_graph, report_text = pyshacl.validate(
            instance_data_graph,
            shacl_graph=shacl_validation_graph,
            data_graph_format=JSONLD,
            shacl_graph_format=TURTLE,
            inference="rdfs",
            debug=True,
            meta_shacl=False,
            serialize_report_graph=TURTLE,
        )

        report_g = Graph()
        report_g.parse(data=report_graph, format="ttl", encoding="utf-8")

        report_text = report_text.replace('"', '').replace('>', '')

        _logger.info(report_text)

        return conforms


if __name__ == "__main__":
    payload = {
        "@context": [
            "https://www.w3.org/ns/activitystreams",
            "https://purl.org/coar/notify"
        ],
        "actor": {
            "id": "https://sandbox.prereview.org/",
            "name": "PREreview",
            "type": "Service"
        },
        "context": {
            "id": "https://doi.org/10.1101/2022.10.06.511170"
        },
        "id": "urn:uuid:572b8e81-d92f-4ed5-8178-cc7f04f44cd1",
        # "object": {
        #     "id": "https://sandbox.prereview.org/reviews/1223155",
        #     "ietf:cite-as": "10.5072/zenodo.1223155",
        #     "type": [
        #         "Document",
        #         "sorg:Review"
        #     ]
        # },
        # "origin": {
        #     "id": "https://sandbox.prereview.org/",
        #     "inbox": "https://sandbox.prereview.org/inbox",
        #     "type": "Service"
        # },
        "target": {
            "id": "https://bioxriv.org/",
            "inbox": "http://notify-inbox.info/inbox",
            "type": "Service"
        },
        "type": [
            "Announce",
            "coar-notify:ReviewAction"
        ],
        "updated": "2022-10-06T15:00:00.000000"
    }

    valid = is_valid('./shapefiles/announce-review-shape.ttl', payload)
    print(f'The payload is valid: {valid}')
