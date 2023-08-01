
def parse_validation_results(result_text: str) -> list[dict]:
    """
    Parses the results of a SHACL validation and returns a list of dictionaries
    containing the results.

    :param result_text: str - the text output of a SHACL validation
    :return: list[dict] - list of dictionaries containing the results

    Example:

    >>> results_text = '''Constraint Violation in MinCountConstraintComponent:
    Severity: sh:Violation
    Source Shape: [sh:minCount Literal("1", datatype=xsd:integer); sh:path[sh:inversePath rdf:type]]
    Focus Node: as:Announce
    Result Path: [ sh:inversePath rdf:type ]
    Message: Less than 1 values on as:Announce->[ sh:inversePath rdf:type ]'''

    >>> results = parse_validation_results(results_text)

    >>> print(results)
    [
        {
            "severity": "sh:Violation",
            "source_shape": "[sh:minCount Literal(\"1\");sh:path [sh:inversePath rdf:type]]",
            "focus_node": "as:Announce",
            "result_path": "[ sh:inversePath rdf:type ]",
            "message": "Less than 1 values on as:Announce->[ sh:inversePath rdf:type ]",
        }
    ]
    """
    results = []
    violation_indexes = []
    results_text_rows = result_text.split("\n")

    for i, row in enumerate(results_text_rows):
        if "Constraint Violation" in row:
            violation_indexes.append(i)

    for index in violation_indexes:
        results.append(
            {
                "severity": results_text_rows[index + 1].split("Severity: ")[1],
                "source_shape": results_text_rows[index + 2].split("Source Shape: ")[1],
                "focus_node": results_text_rows[index + 3].split("Focus Node: ")[1],
                "result_path": results_text_rows[index + 4].split("Result Path: ")[1],
                "message": results_text_rows[index + 5].split("Message: ")[1],
            }
        )

    return results
