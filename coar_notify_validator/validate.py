import json
from rdflib import Graph
import pyshacl

from coar_notify_validator.shape_files import ShapefileType
from coar_notify_validator.shape_files.read_shape_files import read_shape_file
from coar_notify_validator.results_parser import parse_validation_results
from coar_notify_validator.exceptions import GraphParseError


shapeFiles = {}

JSONLD = 'json-ld'
TURTLE = 'ttl'


def get_shape_graph(shape_file_path: str) -> str:
    with open(shape_file_path, 'r', encoding="utf-8") as shape_file:
        return shape_file.read()


def validate(shape_file_type: ShapefileType, payload: dict) -> tuple[bool, list[dict]]:
    """
    Validate a COAR Notify payload against a SHACL shape file.

    :param shape_file_type: ShapefileType - The type of shape file to validate against.
    :param payload: dict - The payload to validate.
    :return: tuple[bool, list[dict]] - a boolean indicating whether the payload is valid
    and a list of validation results.

    Example:

    >>> from coar_notify_validator.shape_files import ShapefileType
    >>> from coar_notify_validator.validate import validate

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

    conforms, _, report_text = pyshacl.validate(
        instance_data_graph,
        shacl_graph=read_shape_file(shape_file_type.value),
        data_graph_format=JSONLD,
        shacl_graph_format=TURTLE,
        inference="rdfs",
        debug=False,
        meta_shacl=False,
        serialize_report_graph=TURTLE,
    )
    report_text = report_text.replace('"', '').replace('>', '')

    return conforms, parse_validation_results(report_text)
