import logging
import json
from rdflib import *
import pyshacl

from shape_files import ShapefileType
from shape_files.read_shape_files import read_shape_file
from validator.results_parser import parse_validation_results

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


shapeFiles = {}

JSONLD = 'json-ld'
TURTLE = 'ttl'


def get_shape_graph(shape_file: str) -> str:
    with open(shape_file, 'r') as f:
        return f.read()


def validate(shape_file_type: ShapefileType, payload: dict) -> tuple[bool, list[dict]]:
    instance_data_graph = None
    shacl_validation_graph = read_shape_file(shape_file_type.value)

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

        return conforms, parse_validation_results(report_text)
