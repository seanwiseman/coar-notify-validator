
def parse_validation_results(result_text: str) -> list[dict]:
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
