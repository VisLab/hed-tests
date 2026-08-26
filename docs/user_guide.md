# HED test suite user guide

## Introduction

### What is HED?

HED (Hierarchical Event Descriptors) is a framework for systematically describing events and experimental metadata in machine-actionable form. HED provides:

- **Controlled vocabulary** for annotating experimental data and events
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)

For more information, visit the HED project [homepage](https://www.hedtags.org) and the [resources page](https://www.hedtags.org/hed-resources).

### What is the HED test suite?

The **HED test suite** (`hed-tests` repository) is the official collection of JSON test cases for validating HED validator implementations. It provides:

- **Comprehensive test coverage**: 137 test cases covering 34 error codes
- **Multiple test types**: String, sidecar, event, and combo tests
- **Correction guidance**: Explanations, common causes, and correction strategies that validators can pass on to annotators
- **Cross-platform consistency**: Single source of truth for all validators
- **Machine-readable specification**: Tests document expected validation behavior

#### Purpose

The test suite serves three primary purposes:

1. **Validator validation**: Ensure Python, JavaScript, and future implementations produce consistent results
2. **Specification documentation**: Provide executable examples of HED validation rules
3. **Correction guidance**: Give HED validators structured explanations and corrections to suggest to annotators

### Related tools and resources

- **[HED homepage](https://www.hedtags.org)**: Overview and links for HED
- **[HED Python validator](https://github.com/hed-standard/hed-python)**: Python implementation (primary consumer)
- **[HED JavaScript validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation (primary consumer)
- **[HED schemas](https://github.com/hed-standard/hed-schemas)**: Standardized vocabularies referenced in tests
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification (source of truth for rules)
- **[HED online tools](https://hedtools.org/hed)**: Web-based validation tools
- **[HED examples](https://github.com/hed-standard/hed-examples)**: Example annotated datasets

______________________________________________________________________

## Getting started

### Clone the repository

Get the test suite from GitHub:

```bash
# Clone the repository and enter it
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

### Set up the environment

Create and activate a virtual environment, then install the development dependencies:

```powershell
# Windows PowerShell
python -m venv .venv
.venv/Scripts/activate.ps1
pip install -e ".[dev,docs]"
```

```bash
# Linux/macOS
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
```

Activate the environment before running any commands in this guide.

### Repository structure

```
hed-tests/
|-- json_test_data/                     # All test data
|   |-- validation_test_data/           # One file per validation error code
|   |-- schema_test_data/               # One file per schema error code
|   |-- validation_tests.json           # Consolidated validation tests
|   |-- validation_code_dict.json       # Maps error codes to test names
|   |-- validation_testname_dict.json   # Maps test names to error codes
|   |-- schema_tests.json               # Consolidated schema tests
|   |-- schema_code_dict.json           # Maps error codes to test names
|   `-- schema_testname_dict.json       # Maps test names to error codes
|-- src/
|   |-- scripts/                        # Utility scripts
|   `-- schemas/                        # JSON schema for test validation
|-- docs/                               # Documentation (this site)
`-- tests/                              # Test utilities
```

Test files are organized by error code in the `json_test_data` directory. Tests that are relevant to validation of HED annotations are in the `validation_test_data` subdirectory, while the tests that are relevant only to HED schema development are organized in the `schema_test_data` subdirectory.

### Test structure

Tests for a specific error code are in a single file named by the most likely HED error code and must conform to a JSON schema available in `src/schemas/test_schema.json`.

```{admonition} **A validator might give a different error code**
---
class: tip
---
Because the exact error code that a validator assigns to an error depends heavily on the order in which it evaluates types of errors, a given test may produce a different error code. 
```

Each test has a `alt_codes` key that gives acceptable alternative error codes.

### Maintenance scripts

Four scripts in `src/scripts/` maintain the test suite. All run from the repository root, and CI runs all four on every push. The typical workflow when adding or editing a test:

1. Edit or add a test file in `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/` (one error code per file).
2. Validate the structure with `validate_test_structure.py`.
3. Regenerate the consolidated files with `consolidate_tests.py`.
4. Check the result with `check_coverage.py` and `python -m unittest discover tests`.
5. Commit the edited file **and** the regenerated consolidated files together.

### Validating the tests

`validate_test_structure.py` checks that test files conform to the JSON schema in `src/schemas/test_schema.json`: JSON syntax, required fields, field types, and test structure.

```bash
# Validate all test directories
python src/scripts/validate_test_structure.py

# Validate one directory
python src/scripts/validate_test_structure.py json_test_data/schema_test_data

# Validate a single file
python src/scripts/validate_test_structure.py --file json_test_data/validation_test_data/TAG_INVALID.json
```

Options: `--schema <path>` validates against a different schema file; `--verbose` shows per-file detail.

### Consolidate tests

`consolidate_tests.py` combines the individual per-error-code files into the generated files at the top of `json_test_data/` that validators actually consume (see `json_test_data/README.md`):

```bash
# Regenerate all six consolidated files:
#   - validation_tests.json (all validation tests)
#   - validation_code_dict.json (error codes to test names)
#   - validation_testname_dict.json (test names to error codes)
#   - schema_tests.json (all schema tests)
#   - schema_code_dict.json (error codes to test names)
#   - schema_testname_dict.json (test names to error codes)
python src/scripts/consolidate_tests.py

# Preview what would be regenerated without writing anything
python src/scripts/consolidate_tests.py --dry-run
```

Options: `--dry-run` previews the consolidation without writing files; `--verbose` shows detailed processing information.

```{admonition} **Always regenerate after editing tests**
---
class: warning
---
Run `consolidate_tests.py` after every test edit and commit the regenerated
files together with the edit. CI runs the script but does not fail when the
committed copies are stale, so a forgotten regeneration silently leaves
validators consuming outdated tests.
```

### Check test coverage

`check_coverage.py` reports which error codes have tests, how many test cases each has, which test types (string/sidecar/event/combo) are covered, and whether the correction guidance fields are complete. Use it to find coverage gaps before adding tests, and run it for current statistics rather than trusting any count written in documentation:

```bash
# Print the coverage report to the console
python src/scripts/check_coverage.py

# Write the coverage report to a markdown file instead
python src/scripts/check_coverage.py --markdown report.md
```

### Generate test index

`generate_test_index.py` regenerates `docs/test_index.md`, the searchable index of every test case organized by error code. The index is generated - edit tests, not the index.

```bash
# Regenerate docs/test_index.md (the default output)
python src/scripts/generate_test_index.py

# Write the index to a different file
python src/scripts/generate_test_index.py --output some_other_file.md

# Produce the index as JSON (give it its own output file so the
# markdown index is not overwritten with JSON)
python src/scripts/generate_test_index.py --format json --output test_index.json
```

After regenerating, run the repository's markdown formatter so the index passes CI's format check:

```bash
# Format the regenerated index with the settings CI checks
python -m mdformat --wrap no --number docs/test_index.md
```

______________________________________________________________________

## Test format specification

### Test format overview

Each JSON test file in the HED Test Suite follows a standardized structure to ensure consistent validation testing across all HED validator implementations.

### File structure

Test files are located in:

- `json_test_data/validation_test_data/` - Tests for validation error codes
- `json_test_data/schema_test_data/` - Tests for schema validation errors

Each file contains an array of test case objects.

### Test case schema

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": ["PLACEHOLDER_INVALID"],
        "name": "tag-invalid-in-schema",
        "description": "Human-readable description of what is being tested",
        "warning": false,
        "schema": "8.4.0",
        "error_category": "semantic",
        "common_causes": ["List of common causes"],
        "explanation": "Detailed explanation a validator can use to suggest a correction",
        "correction_strategy": "How to fix the issue",
        "correction_examples": [
            {
                "wrong": "Invalid HED string",
                "correct": "Corrected HED string",
                "explanation": "Why the correction works"
            }
        ],
        "definitions": [
            "(Definition/Acc/#, (Acceleration/# m-per-s^2, Red))"
        ],
        "tests": {
            "string_tests": {...},
            "sidecar_tests": {...},
            "event_tests": {...},
            "combo_tests": {...}
        }
    }
]
```

### Required fields

#### error_code

**Type**: `string`

The HED error code being tested. Must match the filename (e.g., `TAG_INVALID.json`).

**Example**: `"TAG_INVALID"`

#### name

**Type**: `string`

A unique, descriptive identifier for the test case. Use lowercase with hyphens.

**Example**: `"tag-invalid-in-schema"`

#### description

**Type**: `string`

Human-readable description of what the test case validates.

**Example**: `"Test that tags not in schema are detected as invalid"`

#### schema

**Type**: `string`

HED schema version for this test case.

**Example**: `"8.4.0"`

#### tests

**Type**: `object`

Container for all test data. Must include at least one test type.

### Optional fields

#### alt_codes

**Type**: `array[string]`

Alternative error codes that might be reported for this condition. Useful when multiple validators use different codes for the same error.

**Example**: `["PLACEHOLDER_INVALID"]`

#### warning

**Type**: `boolean` (default: `false`)

Whether this test should produce a warning instead of an error.

#### error_category

**Type**: `string`

Semantic category of the error. One of:

- `"syntax"` - Basic syntax errors (parentheses, commas, etc.)
- `"semantic"` - Tag meaning errors (invalid tags, wrong values)
- `"value"` - Value-specific errors (units, placeholders)
- `"consistency"` - Internal consistency errors (definition usage)
- `"uniqueness"` - Duplicate detection errors
- `"schema"` - Schema structure errors

#### common_causes

**Type**: `array[string]`

List of common reasons this error occurs. Used by validators to point annotators at typical mistakes.

**Example**:

```json
[
    "Typo in tag name",
    "Using deprecated tag",
    "Tag from wrong schema version"
]
```

#### explanation

**Type**: `string`

Detailed explanation of the error, written so that a HED annotation validator can use it to suggest corrections to annotators.

**Example**: `"Tags must exist in the active HED schema. Extensions are allowed but the base tag must be valid."`

#### correction_strategy

**Type**: `string`

General approach to fixing this error.

**Example**: `"Check the tag against the schema browser at hedtags.org. Use the correct tag path or a valid extension."`

#### correction_examples

**Type**: `array[object]`

Concrete examples showing wrong → correct transformations.

**Structure**:

```json
[
    {
        "wrong": "Invalidtag",
        "correct": "Event",
        "explanation": "Use a tag that exists in the schema"
    }
]
```

#### definitions

**Type**: `array[string]`

HED definition strings required for the test case. These are evaluated before the test strings.

**Example**:

```json
[
    "(Definition/Acc/#, (Acceleration/# m-per-s^2, Red))"
]
```

### Test types

#### string_tests

Tests for raw HED strings.

**Structure**:

```json
{
    "fails": [
        "Red, Invalidtag",
        "Blue, Typo/Tag"
    ],
    "passes": [
        "Red, Blue",
        "Event, Sensory-event"
    ]
}
```

- `fails`: Array of HED strings that should produce the error
- `passes`: Array of HED strings that should NOT produce the error

#### sidecar_tests

Tests for BIDS JSON sidecar files.

**Structure**:

```json
{
    "fails": [
        {
            "sidecar": {
                "event_type": {
                    "HED": {
                        "stimulus": "Invalidtag"
                    }
                }
            }
        }
    ],
    "passes": [
        {
            "sidecar": {
                "event_type": {
                    "HED": {
                        "stimulus": "Sensory-event"
                    }
                }
            }
        }
    ]
}
```

Each item is an object with a `sidecar` property containing a BIDS sidecar JSON structure.

#### event_tests

Tests for tabular event data with HED annotations.

**Structure**:

```json
{
    "fails": [
        [
            ["onset", "duration", "HED"],
            [4.5, 0, "Red, Invalidtag"]
        ]
    ],
    "passes": [
        [
            ["onset", "duration", "HED"],
            [4.5, 0, "Red, Blue"]
        ]
    ]
}
```

Each test is a 2D array:

- First row: Column headers (must include at least one HED column)
- Subsequent rows: Event data

#### combo_tests

Combined sidecar + event tests (realistic BIDS scenarios).

**Structure**:

```json
{
    "fails": [
        {
            "sidecar": {
                "event_type": {
                    "HED": {
                        "show": "Sensory-event"
                    }
                }
            },
            "events": [
                ["onset", "duration", "event_type", "HED"],
                [4.5, 0, "show", "Invalidtag"]
            ]
        }
    ],
    "passes": [...]
}
```

Combines a sidecar definition with event data that uses categorical values from the sidecar.

### Validation rules

#### Required structure

1. **At least one test**: Every test case must have at least one test type with data
2. **Both fails and passes**: Each test type should include both failing and passing examples
3. **Valid JSON**: All test data must be valid JSON
4. **Consistent error_code**: Must match the filename

#### Naming conventions

- **File names**: `ERROR_CODE.json` (uppercase, underscores)
- **Test names**: `error-code-specific-scenario` (lowercase, hyphens)
- **Error codes**: Match official HED specification

#### Correction guidance

Required for every validation test (`json_test_data/validation_test_data/`), optional for schema tests (`json_test_data/schema_test_data/`). These fields exist so that HED annotation validators can suggest corrections to annotators; write them for that audience:

- `explanation`: Why this error occurs
- `common_causes`: Typical mistakes
- `correction_strategy`: How to fix
- `correction_examples`: Concrete before/after examples

### Example test file

Here's a complete example from `TAG_INVALID.json`:

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": [],
        "name": "tag-invalid-basic",
        "description": "Basic test for tags not in the schema",
        "warning": false,
        "schema": "8.4.0",
        "error_category": "semantic",
        "common_causes": [
            "Typo in tag name",
            "Using a tag from a different schema version",
            "Attempting to use custom tags without proper extension syntax"
        ],
        "explanation": "Tags must exist in the active HED schema. Each tag path must be found in the schema vocabulary, though extensions to valid tags are allowed using the extension syntax.",
        "correction_strategy": "Verify the tag exists in the schema using the schema browser at hedtags.org. Check for typos, ensure you're using the correct schema version, or use proper extension syntax for custom additions.",
        "correction_examples": [
            {
                "wrong": "Invalidtag",
                "correct": "Event",
                "explanation": "Use a tag that exists in the schema"
            },
            {
                "wrong": "Red, Sensory/Invalidtag",
                "correct": "Red, Sensory-event",
                "explanation": "The full tag path must be valid"
            }
        ],
        "definitions": [],
        "tests": {
            "string_tests": {
                "fails": [
                    "Invalidtag",
                    "Red, Invalidtag",
                    "Sensory/Invalidtag"
                ],
                "passes": [
                    "Red",
                    "Event",
                    "Sensory-event"
                ]
            }
        }
    }
]
```

### Lookup dictionaries

In addition to the individual test files, consolidated lookup dictionaries enable efficient test discovery.

**`validation_code_dict.json`** — maps error codes to test case names:

```json
{
    "TAG_INVALID": [
        "tag-invalid-in-schema",
        "tag-extension-invalid-duplicate"
    ],
    "UNITS_INVALID": [
        "units-invalid-for-unit-class",
        "units-invalid-si-units"
    ]
}
```

**`validation_testname_dict.json`** — maps test case names to all error codes they validate:

```json
{
    "tag-invalid-in-schema": ["TAG_INVALID", "PLACEHOLDER_INVALID"],
    "character-invalid-non-printing": ["CHARACTER_INVALID", "TAG_INVALID"]
}
```

`schema_code_dict.json` and `schema_testname_dict.json` provide equivalent lookups for schema tests.

**Usage:**

```python
import json

with open("json_test_data/validation_code_dict.json") as f:
    code_dict = json.load(f)
tests_for_tag_invalid = code_dict["TAG_INVALID"]

with open("json_test_data/validation_testname_dict.json") as f:
    name_dict = json.load(f)
codes = name_dict["tag-invalid-in-schema"]
```

Dictionaries are automatically regenerated by `src/scripts/consolidate_tests.py`.

______________________________________________________________________

______________________________________________________________________

## Validator integration guide

### Integration overview

The HED Test Suite provides standardized JSON test cases that all HED validators should pass. By integrating these tests, you ensure your validator:

- **Matches the specification**: Validates HED according to the official rules
- **Maintains consistency**: Produces the same results as other validators
- **Prevents regressions**: Catches changes in validation behavior
- **Documents behavior**: Tests serve as executable specifications

### Getting the tests

#### Method 1: Git clone (recommended)

Clone the repository to access all tests:

```bash
# Clone the repository and enter it
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

Update periodically to get new tests:

```bash
# Pull the latest tests from the main branch
git pull origin main
```

#### Method 2: Download ZIP

Download the latest tests as a ZIP file:

```
https://github.com/hed-standard/hed-tests/archive/refs/heads/main.zip
```

#### Method 3: Submodule

Add as a git submodule to your validator repository:

```bash
# Add the test suite as a submodule under tests/hed-tests
git submodule add https://github.com/hed-standard/hed-tests.git tests/hed-tests

# Fetch the submodule contents
git submodule update --init --recursive
```

### Integration approaches

#### Approach 1: Direct test execution

Read test files and execute them directly in your test framework.

**Python example (unittest)**:

```python
import json
import unittest
from pathlib import Path


class TestHedValidation(unittest.TestCase):
    """Test HED validation using the test suite."""

    @classmethod
    def setUpClass(cls):
        """Load all test cases once before running tests."""
        cls.test_cases = []
        test_dir = Path("hed-tests/json_test_data/validation_test_data")

        for test_file in test_dir.glob("*.json"):
            with open(test_file) as f:
                cases = json.load(f)
                for case in cases:
                    cls.test_cases.append((test_file.stem, case))

    def test_validation_suite(self):
        """Run each test case from the suite."""
        for error_code, test_case in self.test_cases:
            with self.subTest(error_code=error_code, test_name=test_case["name"]):
                schema = load_schema(test_case["schema"])

                # Test failing strings
                if "string_tests" in test_case.get("tests", {}):
                    for hed_string in test_case["tests"]["string_tests"].get("fails", []):
                        issues = validate_hed_string(hed_string, schema)
                        self.assertTrue(
                            any(issue.code == error_code for issue in issues), f"Expected {error_code} for: {hed_string}"
                        )

                    # Test passing strings
                    for hed_string in test_case["tests"]["string_tests"].get("passes", []):
                        issues = validate_hed_string(hed_string, schema)
                        self.assertFalse(
                            any(issue.code == error_code for issue in issues), f"Unexpected {error_code} for: {hed_string}"
                        )


if __name__ == "__main__":
    unittest.main()
```

**JavaScript Example (Jest)**:

```javascript
const fs = require('fs');
const path = require('path');
const { validateHedString } = require('./validator');

describe('HED Validation Tests', () => {
    const testDir = 'hed-tests/json_test_data/validation_test_data';
    const files = fs.readdirSync(testDir);
    
    files.forEach(filename => {
        const errorCode = path.basename(filename, '.json');
        const testCases = JSON.parse(
            fs.readFileSync(path.join(testDir, filename), 'utf8')
        );
        
        describe(errorCode, () => {
            testCases.forEach(testCase => {
                test(testCase.name, () => {
                    const schema = loadSchema(testCase.schema);
                    
                    // Test failing strings
                    const fails = testCase.tests?.string_tests?.fails || [];
                    fails.forEach(hedString => {
                        const issues = validateHedString(hedString, schema);
                        expect(issues.some(i => i.code === errorCode)).toBe(true);
                    });
                    
                    // Test passing strings
                    const passes = testCase.tests?.string_tests?.passes || [];
                    passes.forEach(hedString => {
                        const issues = validateHedString(hedString, schema);
                        expect(issues.some(i => i.code === errorCode)).toBe(false);
                    });
                });
            });
        });
    });
});
```

#### Approach 2: Generate test cases

Generate test files in your native test format from the JSON.

**Example**: Convert JSON to Python unittest files:

```python
import json
from pathlib import Path


def generate_test_file(json_path, output_path):
    """Generate a Python test file from JSON test cases."""
    with open(json_path) as f:
        test_cases = json.load(f)

    error_code = json_path.stem

    test_code = f"""
import unittest
from hed_validator import validate_hed_string, load_schema

class Test{error_code}(unittest.TestCase):
"""

    for i, case in enumerate(test_cases):
        test_code += f'''
    def test_{case["name"].replace("-", "_")}(self):
        """Test: {case["description"]}"""
        schema = load_schema("{case["schema"]}")

'''
        if "string_tests" in case.get("tests", {}):
            for hed_string in case["tests"]["string_tests"].get("fails", []):
                test_code += f'''
        issues = validate_hed_string("{hed_string}", schema)
        self.assertTrue(any(i.code == "{error_code}" for i in issues))
'''
            for hed_string in case["tests"]["string_tests"].get("passes", []):
                test_code += f'''
        issues = validate_hed_string("{hed_string}", schema)
        self.assertFalse(any(i.code == "{error_code}" for i in issues))
'''

    with open(output_path, "w") as f:
        f.write(test_code)
```

#### Approach 3: Test report comparison

Run tests and compare your results against a reference implementation.

```python
def compare_validation_results(test_case, reference_issues, your_issues):
    """Compare validation results against reference implementation."""
    error_code = test_case["error_code"]

    # Check if both found (or didn't find) the error
    ref_found = any(i.code == error_code for i in reference_issues)
    your_found = any(i.code == error_code for i in your_issues)

    if ref_found != your_found:
        return {"test": test_case["name"], "expected": ref_found, "actual": your_found, "status": "MISMATCH"}

    return {"status": "MATCH"}
```

### Test types Implementation

#### String tests

Simplest test type - raw HED strings.

```python
def run_string_tests(test_case, schema):
    """Execute string_tests from a test case."""
    error_code = test_case["error_code"]
    string_tests = test_case["tests"].get("string_tests", {})

    # Test strings that should fail
    for hed_string in string_tests.get("fails", []):
        issues = validate_hed_string(hed_string, schema)
        assert any(i.code == error_code for i in issues), f"Expected {error_code} for: {hed_string}"

    # Test strings that should pass
    for hed_string in string_tests.get("passes", []):
        issues = validate_hed_string(hed_string, schema)
        assert not any(i.code == error_code for i in issues), f"Unexpected {error_code} for: {hed_string}"
```

#### Sidecar tests

Test BIDS JSON sidecar validation.

```python
def run_sidecar_tests(test_case, schema):
    """Execute sidecar_tests from a test case."""
    error_code = test_case["error_code"]
    sidecar_tests = test_case["tests"].get("sidecar_tests", {})
    
    for sidecar_obj in sidecar_tests.get("fails", []):
        sidecar = sidecar_obj["sidecar"]
        issues = validate_sidecar(sidecar, schema)
        assert any(i.code == error_code for i in issues)
    
    for sidecar_obj in sidecar_tests.get("passes", []):
        sidecar = sidecar_obj["sidecar"]
        issues = validate_sidecar(sidecar, schema)
        assert not any(i.code == error_code for i in issues)
```

#### Event tests

Test tabular event data.

```python
def run_event_tests(test_case, schema):
    """Execute event_tests from a test case."""
    error_code = test_case["error_code"]
    event_tests = test_case["tests"].get("event_tests", {})
    
    for event_data in event_tests.get("fails", []):
        headers = event_data[0]
        rows = event_data[1:]
        issues = validate_events(headers, rows, schema)
        assert any(i.code == error_code for i in issues)
    
    for event_data in event_tests.get("passes", []):
        headers = event_data[0]
        rows = event_data[1:]
        issues = validate_events(headers, rows, schema)
        assert not any(i.code == error_code for i in issues)
```

#### Combo tests

Combined sidecar + event tests (most realistic).

```python
def run_combo_tests(test_case, schema):
    """Execute combo_tests from a test case."""
    error_code = test_case["error_code"]
    combo_tests = test_case["tests"].get("combo_tests", {})
    
    for combo in combo_tests.get("fails", []):
        sidecar = combo["sidecar"]
        headers = combo["events"][0]
        rows = combo["events"][1:]
        
        issues = validate_bids_dataset(sidecar, headers, rows, schema)
        assert any(i.code == error_code for i in issues)
    
    for combo in combo_tests.get("passes", []):
        sidecar = combo["sidecar"]
        headers = combo["events"][0]
        rows = combo["events"][1:]
        
        issues = validate_bids_dataset(sidecar, headers, rows, schema)
        assert not any(i.code == error_code for i in issues)
```

### Handling definitions

Some tests require definitions to be loaded before validation:

```python
def run_test_with_definitions(test_case, schema):
    """Run test case with definition pre-loading."""
    # Load definitions first
    definitions = test_case.get("definitions", [])
    definition_dict = {}

    for def_string in definitions:
        name, definition = parse_definition(def_string)
        definition_dict[name] = definition

    # Now run tests with definitions available
    for hed_string in test_case["tests"]["string_tests"]["fails"]:
        issues = validate_hed_string(hed_string, schema, definitions=definition_dict)
        # ... assertions
```

### Error code mapping

Your validator might use different error codes. Use the `alt_codes` field:

```python
def check_error_match(issue, expected_code, alt_codes):
    """Check if an issue matches expected code or alternates."""
    if issue.code == expected_code:
        return True
    
    return issue.code in alt_codes
```

Example from test case:

```json
{
    "error_code": "TAG_INVALID",
    "alt_codes": ["PLACEHOLDER_INVALID"],
    ...
}
```

### CI/CD integration

Add test suite validation to your CI pipeline:

**GitHub Actions Example**:

```yaml
name: HED Test Suite

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Clone HED test suite
        run: |
          git clone https://github.com/hed-standard/hed-tests.git
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install -e .
      
      - name: Run HED test suite
        run: |
          python -m unittest tests.test_hed_validation -v
```

### Example integrations

#### hed-python

```python
# tests/test_validation_suite.py
import json
import unittest
from pathlib import Path


class TestValidationSuite(unittest.TestCase):
    def test_validation_suite(self):
        test_dir = Path("hed-tests/json_test_data/validation_test_data")
        for test_file in test_dir.glob("*.json"):
            with self.subTest(test_file=test_file.name):
                with open(test_file) as f:
                    test_cases = json.load(f)
                # ... run tests
```

#### hed-javascript

```javascript
// tests/validation.test.js
const testData = require('./hed-tests/json_test_data/validation_tests.json');

describe('HED Validation Suite', () => {
    testData.forEach(testCase => {
        // ... run tests
    });
});
```

#### Using lookup dictionaries

```python
import json

with open("hed-tests/json_test_data/validation_code_dict.json") as f:
    code_dict = json.load(f)

tag_tests = code_dict.get("TAG_INVALID", [])
print(f"TAG_INVALID is validated by {len(tag_tests)} tests")

with open("hed-tests/json_test_data/validation_tests.json") as f:
    all_tests = json.load(f)

filtered_tests = [t for t in all_tests if t["name"] in tag_tests]
```

### Reporting issues

If your validator produces different results:

1. **Verify the test case**: Ensure you're parsing the JSON correctly
2. **Check schema version**: Make sure you're using the correct schema
3. **Review the specification**: Check the HED specification for clarification
4. **File an issue**: Report discrepancies at https://github.com/hed-standard/hed-tests/issues

Include:

- Test case name and error code
- Expected vs actual behavior
- Your validator implementation (Python, JavaScript, etc.)
- Schema version used

### Integration best practices

1. **Run all tests**: Don't cherry-pick - run the entire suite
2. **Automate execution**: Integrate tests into CI/CD
3. **Track coverage**: Monitor which tests pass/fail over time
4. **Update regularly**: Pull latest tests periodically
5. **Report discrepancies**: Help improve the test suite
6. **Use schema versions**: Respect the schema version in each test
7. **Handle all test types**: Support string, sidecar, event, and combo tests

______________________________________________________________________

## Error code categories

Tests are organized by error code, mapping to validation rules in the HED specification.

### Syntax errors

- `CHARACTER_INVALID` - Invalid characters in tags
- `COMMA_MISSING` - Missing required commas
- `PARENTHESES_MISMATCH` - Unmatched parentheses
- `TAG_EMPTY` - Empty tag elements

### Semantic errors

- `TAG_INVALID` - Tags not in schema
- `TAG_EXTENDED` - Tag extension warnings (warning)
- `TAG_EXTENSION_INVALID` - Invalid tag extensions
- `VALUE_INVALID` - Invalid tag values
- `UNITS_INVALID` - Invalid or missing units

### Definition errors

- `DEFINITION_INVALID` - Malformed definitions
- `DEF_INVALID` - Invalid definition usage
- `DEF_EXPAND_INVALID` - Definition expansion errors

### Sidecar errors

- `SIDECAR_INVALID` - Invalid sidecar structure
- `SIDECAR_BRACES_INVALID` - Curly brace errors
- `SIDECAR_KEY_MISSING` - Missing required keys

### Schema errors

- `SCHEMA_ATTRIBUTE_INVALID` - Invalid schema attributes
- `SCHEMA_ATTRIBUTE_VALUE_INVALID` - Invalid schema attribute values
- `SCHEMA_CHARACTER_INVALID` - Invalid characters in schema
- `SCHEMA_DEPRECATION_ERROR` - Deprecation errors
- `SCHEMA_DUPLICATE_NODE` - Duplicate schema nodes
- `SCHEMA_HEADER_INVALID` - Invalid schema headers
- `SCHEMA_LIBRARY_INVALID` - Invalid library references
- `SCHEMA_LOAD_FAILED` - Schema loading failures
- `SCHEMA_SECTION_MISSING` - Missing required schema sections
- `WIKI_DELIMITERS_INVALID` - Invalid wiki delimiters in schema

### Temporal errors

- `TEMPORAL_TAG_ERROR` - Temporal tag issues (Onset/Offset/Inset)

### Other

- `ELEMENT_DEPRECATED` - Deprecated element usage (warning)
- `PLACEHOLDER_INVALID` - Invalid placeholder usage
- `TAG_EXPRESSION_REPEATED` - Repeated tag expressions
- `TAG_GROUP_ERROR` - Tag group structure errors
- `TAG_NAMESPACE_PREFIX_INVALID` - Invalid namespace prefix
- `TAG_NOT_UNIQUE` - Non-unique tag usage
- `TAG_REQUIRES_CHILD` - Tag requires child node

______________________________________________________________________

## Test index

The complete, searchable test index of every test case is in [test_index.md](test_index.md); run `check_coverage.py` for current counts.

______________________________________________________________________

## Contributing

Thank you for your interest in contributing to the HED test suite! This section provides guidelines for adding new tests, improving existing ones, and maintaining test quality.

### Types of contributions

#### Adding new test cases

Add tests for:

- **Uncovered error codes**: Check [test_coverage.md](test_coverage.md) for gaps
- **Edge cases**: Unusual scenarios not yet tested
- **Common mistakes**: Real-world errors developers encounter
- **Complex scenarios**: Multi-condition tests

#### Improving existing tests

Enhance tests by:

- Adding correction guidance (`explanation`, `common_causes`, `correction_examples`)
- Including additional test types (sidecar, event, combo tests)
- Expanding failing/passing cases
- Clarifying descriptions

#### Documentation and tooling

- Clarify test format specifications or add integration examples
- Improve validation scripts or add coverage analysis features
- Enhance CI/CD workflows

### Setting up to contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/hed-tests.git
   cd hed-tests
   ```
3. **Set up the environment** (see [Set up the environment](#set-up-the-environment) in Getting started)
4. **Create a feature branch**:
   ```bash
   git checkout -b feature/add-new-tests
   ```

### Adding new test cases

#### Step 1: Identify the error code

Determine which error code your test validates. Error codes should match the HED specification:

- Validation errors: `TAG_INVALID`, `UNITS_INVALID`, etc.
- Schema errors: `SCHEMA_ATTRIBUTE_INVALID`, etc.

If adding a completely new error code, create a new test file.

#### Step 2: Choose the test file

- **Existing error code**: Edit the corresponding file in `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/`
- **New error code**: Create a new file named `ERROR_CODE.json`

#### Step 3: Write the test case

Follow this template:

```json
{
    "error_code": "TAG_INVALID",
    "alt_codes": [],
    "name": "descriptive-test-name",
    "description": "Clear description of what this tests",
    "warning": false,
    "schema": "8.4.0",
    "error_category": "semantic",
    "common_causes": [
        "First common cause",
        "Second common cause"
    ],
    "explanation": "Detailed explanation a validator can use to suggest a correction",
    "correction_strategy": "How to fix this error",
    "correction_examples": [
        {
            "wrong": "Invalid HED string",
            "correct": "Corrected HED string",
            "explanation": "Why this correction works"
        }
    ],
    "definitions": [],
    "tests": {
        "string_tests": {
            "fails": ["HED string that should fail validation"],
            "passes": ["HED string that should pass validation"]
        }
    }
}
```

#### Step 4: Include multiple test types

Whenever possible, include multiple test types. See [Test types](#test-types) for full format details.

- **String tests** (always include): Raw HED strings
- **Sidecar tests**: JSON sidecar validation
- **Event tests**: Tabular event data
- **Combo tests**: Combined sidecar + event (most realistic scenarios)

#### Step 5: Add correction guidance

Validation tests must include these fields; they let HED annotation validators suggest corrections to annotators. Schema tests may omit them:

- `explanation`: Detailed explanation of why this error occurs
- `common_causes`: List of typical reasons annotators encounter this error
- `correction_strategy`: General approach to fixing the error
- `correction_examples`: Concrete before/after examples

#### Step 6: Validate your test

Before committing, validate the test structure and regenerate the consolidated files:

```bash
# Validate the file you edited against the test schema
python src/scripts/validate_test_structure.py --file json_test_data/validation_test_data/YOUR_FILE.json

# Regenerate the consolidated files
python src/scripts/consolidate_tests.py
```

### Quality checklist

Before submitting a PR, ensure:

- [ ] **Valid JSON**: No syntax errors
- [ ] **Passes schema validation**: Validated with `validate_test_structure.py`
- [ ] **Both fails and passes**: Each test type includes both
- [ ] **Correction guidance included** (validation tests): explanation, causes, corrections
- [ ] **Clear descriptions**: Self-explanatory test names
- [ ] **Correct schema version**: Matches the schema you tested against
- [ ] **Realistic examples**: Uses practical HED strings
- [ ] **Consolidated files updated**: Run `consolidate_tests.py` after all edits

### Testing against validators

If possible, test your cases against existing validators before submitting:

**Python (hed-python)**:

```python
from hed import HedString, load_schema

schema = load_schema("8.4.0")
hed_string = HedString("Your test string", schema)
issues = hed_string.validate()
# Verify error code appears/doesn't appear as expected
```

**JavaScript (hed-javascript)**:

```javascript
const { validateHedString } = require('hed-javascript');
const issues = validateHedString('Your test string', schema);
// Verify error code appears/doesn't appear as expected
```

### Pull request process

1. **Commit your changes** with a clear message:
   ```bash
   git add json_test_data/validation_test_data/TAG_INVALID.json
   git commit -m "Add edge case tests for TAG_INVALID"
   ```
2. **Push to your fork**: `git push origin feature/add-new-tests`
3. **Open a pull request** on GitHub with a clear title and description
4. **Address review feedback**: Maintainers may request changes; push updates to the same branch
5. **Merge**: Once approved, maintainers will merge your PR

**PR description template**:

```markdown
## Description
Brief summary of changes.

## Changes made
- Added X new test cases for ERROR_CODE
- Improved Y test with additional metadata

## Testing
- [x] Validated with validate_test_structure.py
- [x] Tested against hed-python validator

## Related issues
Closes #123
```

### Best practices

**Writing tests**:

- Start with `string_tests`, add more test types for coverage
- Test edge cases and common real-world mistakes
- Include both obvious and subtle scenarios
- Write explanations that help a validator suggest a correction to the annotator

**Organization**:

- One error code per file
- Use descriptive, consistent test names
- Run `consolidate_tests.py` after every edit

### Test case examples

**Good test case**:

```json
{
    "error_code": "TAG_INVALID",
    "name": "tag-invalid-nested-groups",
    "description": "Test invalid tags within nested groups",
    "schema": "8.4.0",
    "error_category": "semantic",
    "common_causes": ["Typo in tag name within complex annotation"],
    "explanation": "Even within nested groups, all tags must exist in the schema.",
    "correction_strategy": "Verify each tag path in nested groups using the schema browser.",
    "correction_examples": [
        {
            "wrong": "(Red, (Invalidtag, Blue))",
            "correct": "(Red, (Event, Blue))",
            "explanation": "Replace invalid nested tag with valid schema tag"
        }
    ],
    "tests": {
        "string_tests": {
            "fails": ["(Red, (Invalidtag, Blue))"],
            "passes": ["(Red, (Event, Blue))"]
        }
    }
}
```

**Bad test case** (avoid this):

```json
{
    "error_code": "TAG_INVALID",
    "name": "test1",
    "description": "test",
    "schema": "8.4.0",
    "tests": {
        "string_tests": {
            "fails": ["x"],
            "passes": ["y"]
        }
    }
}
```

Problems: non-descriptive name, vague description, no correction guidance, unclear test strings.

### Code of conduct

Please be respectful and professional in all interactions. By contributing, you agree that your contributions will be licensed under the MIT License.

______________________________________________________________________

## Support

### HED resources

- **[HED homepage](https://www.hedtags.org)**: Project overview
- **[HED specification](https://www.hedtags.org/hed-specification)**: Formal validation rules
- **[HED schemas](https://github.com/hed-standard/hed-schemas)**: Vocabulary definitions
- **[HED Python validator](https://github.com/hed-standard/hed-python)**: Python implementation
- **[HED JavaScript validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation

### Getting help

- **Issues**: [GitHub Issues](https://github.com/hed-standard/hed-tests/issues)
- **Discussions**: [GitHub Discussions](https://github.com/orgs/hed-standard/discussions)
- **Email**: [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)

______________________________________________________________________

**End of User Guide**
