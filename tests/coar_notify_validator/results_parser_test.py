import pytest

from coar_notify_validator.results_parser import parse_validation_results


@pytest.mark.parametrize(
    "result_text, expected",
    [
        (
                """ Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
                    Severity: sh:Violation
                    Source Shape: [ sh:minCount Literal("1", datatype=xsd:integer) ; sh:path [ sh:inversePath rdf:type ] ]
                    Focus Node: as:Announce
                    Result Path: [ sh:inversePath rdf:type ]
                    Message: Less than 1 values on as:Announce->[ sh:inversePath rdf:type ]"""
                ,
                [
                    {
                        "severity": "sh:Violation",
                        "source_shape": "[ sh:minCount Literal(\"1\", datatype=xsd:integer) ; sh:path [ sh:inversePath rdf:type ] ]",
                        "focus_node": "as:Announce",
                        "result_path": "[ sh:inversePath rdf:type ]",
                        "message": "Less than 1 values on as:Announce->[ sh:inversePath rdf:type ]",
                    }
                ],
        ),
        (
            """Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
                Severity: sh:Violation
                Source Shape: [ sh:minCount Literal(1, datatype=xsd:integer) ; sh:path [ sh:inversePath rdf:type ] ]
                Focus Node: sorg:Review
                Result Path: [ sh:inversePath rdf:type ]
                Message: Less than 1 values on sorg:Review-[ sh:inversePath rdf:type ]
            Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
                Severity: sh:Violation
                Source Shape: [ sh:minCount Literal(1, datatype=xsd:integer) ; sh:path [ sh:inversePath rdf:type ] ]
                Focus Node: as:Document
                Result Path: [ sh:inversePath rdf:type ]
                Message: Less than 1 values on as:Document-[ sh:inversePath rdf:type ]""",
            [
                {
                    "severity": "sh:Violation",
                    "source_shape": "[ sh:minCount Literal(1, datatype=xsd:integer) ; sh:path [ sh:inversePath rdf:type ] ]",
                    "focus_node": "sorg:Review",
                    "result_path": "[ sh:inversePath rdf:type ]",
                    "message": "Less than 1 values on sorg:Review-[ sh:inversePath rdf:type ]",
                },
                {
                    "severity": "sh:Violation",
                    "source_shape": "[ sh:minCount Literal(1, datatype=xsd:integer) ; sh:path [ sh:inversePath rdf:type ] ]",
                    "focus_node": "as:Document",
                    "result_path": "[ sh:inversePath rdf:type ]",
                    "message": "Less than 1 values on as:Document-[ sh:inversePath rdf:type ]",
                },
            ]
        ),
    ]
)
def test_parse_validation_results(result_text, expected):
    assert parse_validation_results(result_text) == expected


