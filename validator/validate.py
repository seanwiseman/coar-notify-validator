import logging
import json
from rdflib import *
import pyshacl

from shape_files import ShapefileType
from shape_files.read_shape_files import read_shape_file
from validator.results_parser import parse_validation_results
from validator.exceptions import GraphParseError


_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


shapeFiles = {}

JSONLD = 'json-ld'
TURTLE = 'ttl'


def get_shape_graph(shape_file: str) -> str:
    with open(shape_file, 'r') as f:
        return f.read()


def validate(shape_file_type: ShapefileType, payload: dict) -> tuple[bool, list[dict]]:
    """
    Validate a COAR Notify payload against a SHACL shape file.

    :param shape_file_type: ShapefileType - The type of shape file to validate against.
    :param payload: dict - The payload to validate.
    :return: tuple[bool, list[dict]] - A tuple containing a boolean indicating whether the payload is valid and a list
    of validation results.

    Example:

    >>> from shape_files import ShapefileType
    >>> from validator.validate import validate

    >>> payload = {} # An actual review offer COAR Notify payload.

    >>> conforms, errors = validate(ShapefileType.OFFER_REVIEW, payload)
    >>> print(conforms)
    True
    >>> print(errors)
    []
    """
    instance_data_graph = Graph().parse(data=json.dumps(payload), format=JSONLD)

    if not instance_data_graph:
        raise GraphParseError("Unable to parse payload into Graph.")

    conforms, report_graph, report_text = pyshacl.validate(
        instance_data_graph,
        shacl_graph=read_shape_file(shape_file_type.value),
        data_graph_format=JSONLD,
        shacl_graph_format=TURTLE,
        inference="rdfs",
        debug=False,
        meta_shacl=False,
        serialize_report_graph=TURTLE,
    )

    report_g = Graph()
    report_g.parse(data=report_graph, format="ttl", encoding="utf-8")
    report_text = report_text.replace('"', '').replace('>', '')

    _logger.info(report_text)

    return conforms, parse_validation_results(report_text)
