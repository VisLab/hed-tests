# HED Test Suite User Guide

**Complete guide to the HED Test Suite**

______________________________________________________________________

## Table of Contents

1. [Introduction](#introduction)
   - [What is HED?](#what-is-hed)
   - [What is the HED Test Suite?](#what-is-the-hed-test-suite)
   - [Related Tools and Resources](#related-tools-and-resources)
2. [Getting Started](#getting-started)
   - [Clone the Repository](#clone-the-repository)
   - [Repository Structure](#repository-structure)
   - [Test Structure](#test-structure)
   - [Validating the Tests](#validating-the-tests)
   - [Consolidate Tests](#consolidate-tests)
   - [Check Test Coverage](#check-test-coverage)
   - [Generate Test Index](#generate-test-index)
3. [Test Format Specification](#test-format-specification)
   - [Overview](#test-format-overview)
   - [File Structure](#file-structure)
   - [Test Case Schema](#test-case-schema)
   - [Required Fields](#required-fields)
   - [Optional Fields](#optional-fields)
   - [Test Types](#test-types)
   - [Validation Rules](#validation-rules)
   - [Example Test File](#example-test-file)
4. [Test Coverage Report](#test-coverage-report)
   - [Summary Statistics](#summary-statistics)
   - [Test Type Coverage](#test-type-coverage)
   - [Coverage by Error Code](#coverage-by-error-code)
   - [Files by Error Code](#files-by-error-code)
5. [Validator Integration Guide](#validator-integration-guide)
   - [Overview](#integration-overview)
   - [Getting the Tests](#getting-the-tests)
   - [Test File Structure](#test-file-structure-integration)
   - [JSON Format](#json-format)
   - [Integration Approaches](#integration-approaches)
   - [Test Types Implementation](#test-types-implementation)
   - [Handling Definitions](#handling-definitions)
   - [Error Code Mapping](#error-code-mapping)
   - [CI/CD Integration](#cicd-integration)
   - [Reporting Issues](#reporting-issues)
   - [Best Practices](#integration-best-practices)
6. [Complete Test Index](#complete-test-index)
   - [Quick Navigation](#quick-navigation-index)
   - [Detailed Test Listings](#detailed-test-listings)

______________________________________________________________________

## Introduction

### What is HED?

HED (Hierarchical Event Descriptors) is a framework for systematically describing events and experimental metadata in machine-actionable form. HED provides:

- **Controlled vocabulary** for annotating experimental data and events
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)

For more information, visit the HED project [homepage](https://www.hedtags.org) and the [resources page](https://www.hedtags.org/hed-resources).

### What is the HED Test Suite?

The **HED test suite** (`hed-tests` repository) is the official collection of JSON test cases for validating HED validator implementations. It provides:

- **Comprehensive test coverage**: 136 test cases covering 33 error codes
- **Multiple test types**: String, sidecar, event, and combo tests
- **AI-friendly metadata**: Explanations, common causes, and correction strategies
- **Cross-platform consistency**: Single source of truth for all validators
- **Machine-readable specification**: Tests document expected validation behavior

#### Purpose

The test suite serves three primary purposes:

1. **Validator validation**: Ensure Python, JavaScript, and future implementations produce consistent results
2. **Specification documentation**: Provide executable examples of HED validation rules
3. **AI training**: Enable AI systems to understand HED validation through structured examples

### Related Tools and Resources

- **[HED homepage](https://www.hedtags.org)**: Overview and links for HED
- **[HED Python validator](https://github.com/hed-standard/hed-python)**: Python implementation (primary consumer)
- **[HED JavaScript validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation (primary consumer)
- **[HED schemas](https://github.com/hed-standard/hed-schemas)**: Standardized vocabularies referenced in tests
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification (source of truth for rules)
- **[HED online tools](https://hedtools.org/hed)**: Web-based validation tools
- **[HED examples](https://github.com/hed-standard/hed-examples)**: Example annotated datasets

______________________________________________________________________

## Getting Started

### Clone the Repository

Get the test suite from GitHub:

```bash
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

### Repository Structure

```
hed-tests/
├── json_test_data/                     # All test data
│   ├── validation_test_data/           # 25 validation error test files
│   ├── schema_test_data/               # 17 schema error test files
│   ├── validation_tests.json           # Consolidated validation tests
│   ├── validation_code_dict.json       # Maps error codes to test names
│   ├── validation_testname_dict.json   # Maps test names to error codes
│   ├── schema_tests.json               # Consolidated schema tests
│   ├── schema_code_dict.json           # Maps error codes to test names
│   └── schema_testname_dict.json       # Maps test names to error codes
├── src/
│   ├── scripts/                        # Utility scripts
│   └── schemas/                        # JSON schema for test validation
├── docs/                               # Documentation (this site)
└── tests/                              # Test utilities
```

Test files are organized by error code in the `json_test_data` directory. Tests that are relevant to validation of HED annotations are in the `validation_test_data` subdirectory, while the tests that are relevant only to HED schema development are organized in the `schema_test_data` subdirectory.

### Test Structure

Tests for a specific error code are in a single file named by the most likely HED error code and must conform to a JSON schema available in `src/schemas/test_schema.json`.

```{admonition} **A validator might give a different error code**
---
class: tip
---
Because the exact error code that a validator assigns to an error depends heavily on the order in which it evaluates types of errors, a given test may produce a different error code. 
```

Each test has a `alt_codes` key that gives acceptable alternative error codes.

### Validating the Tests

Ensure test files conform to the JSON schema:

```bash
# Validate a single test file
python src/scripts/validate_test_structure.py json_test_data/validation_test_data/TAG_INVALID.json

# Validate all tests
python src/scripts/validate_test_structure.py json_test_data/validation_test_data
python src/scripts/validate_test_structure.py json_test_data/schema_test_data
```

### Consolidate Tests

Generate consolidated test files and lookup dictionaries:

```powershell
python src/scripts/consolidate_tests.py

# Creates:
#   - validation_tests.json (all validation tests)
#   - validation_code_dict.json (error codes to test names)
#   - validation_testname_dict.json (test names to error codes)
#   - schema_tests.json (all schema tests)
#   - schema_code_dict.json (error codes to test names)
#   - schema_testname_dict.json (test names to error codes)
```

The consolidation process creates both combined test files and lookup dictionaries for efficient test discovery.

### Check Test Coverage

Analyze test coverage statistics:

```powershell
python src/scripts/check_coverage.py

# Output:
# HED Test Suite Coverage Report
# =====================================
# Total test files: 42
# Total test cases: 136
# Error codes covered: 33
# ...
```

### Generate Test Index

Create a searchable test index:

```powershell
python src/scripts/generate_test_index.py

# Creates: docs/test_index.md
```

______________________________________________________________________

## Test Format Specification

### Test Format Overview

Each JSON test file in the HED Test Suite follows a standardized structure to ensure consistent validation testing across all HED validator implementations.

### File Structure

Test files are located in:

- `json_test_data/validation_test_data/` - Tests for validation error codes
- `json_test_data/schema_test_data/` - Tests for schema validation errors

Each file contains an array of test case objects.

### Test Case Schema

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
        "explanation": "Detailed explanation for AI/developers",
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

### Required Fields

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

### Optional Fields

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

List of common reasons this error occurs. Used by AI systems to understand typical mistakes.

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

Detailed explanation of the error for AI systems and developers.

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

### Test Types

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

### Validation Rules

#### Required Structure

1. **At least one test**: Every test case must have at least one test type with data
2. **Both fails and passes**: Each test type should include both failing and passing examples
3. **Valid JSON**: All test data must be valid JSON
4. **Consistent error_code**: Must match the filename

#### Naming Conventions

- **File names**: `ERROR_CODE.json` (uppercase, underscores)
- **Test names**: `error-code-specific-scenario` (lowercase, hyphens)
- **Error codes**: Match official HED specification

#### AI Metadata

For AI training and code generation, include:

- `explanation`: Why this error occurs
- `common_causes`: Typical mistakes
- `correction_strategy`: How to fix
- `correction_examples`: Concrete before/after examples

### Example Test File

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

______________________________________________________________________

## Test Coverage Report

### Summary Statistics

- **Total error codes covered**: 33
- **Total test cases**: 136
- **Error codes with AI metadata**: 33 (100.0%)

### Test Type Coverage

- **combo_tests**: 23 error codes
- **event_tests**: 23 error codes
- **schema_tests**: 9 error codes
- **sidecar_tests**: 23 error codes
- **string_tests**: 24 error codes

### Coverage by Error Code

| Error Code                     | Test Cases | Test Types                                            | AI Metadata | Schema Versions                |
| ------------------------------ | ---------- | ----------------------------------------------------- | ----------- | ------------------------------ |
| CHARACTER_INVALID              | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.2.0, 8.4.0                   |
| COMMA_MISSING                  | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| DEFINITION_INVALID             | 10         | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| DEF_EXPAND_INVALID             | 6          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| DEF_INVALID                    | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| ELEMENT_DEPRECATED             | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.2.0                          |
| PARENTHESES_MISMATCH           | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| PLACEHOLDER_INVALID            | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| SCHEMA_ATTRIBUTE_INVALID       | 1          | schema_tests                                          | ✓           |                                |
| SCHEMA_ATTRIBUTE_VALUE_INVALID | 12         | schema_tests                                          | ✓           |                                |
| SCHEMA_CHARACTER_INVALID       | 6          | schema_tests                                          | ✓           |                                |
| SCHEMA_DEPRECATION_ERROR       | 8          | schema_tests                                          | ✓           |                                |
| SCHEMA_DUPLICATE_NODE          | 2          | schema_tests                                          | ✓           |                                |
| SCHEMA_HEADER_INVALID          | 2          | schema_tests                                          | ✓           |                                |
| SCHEMA_LIBRARY_INVALID         | 8          | schema_tests                                          | ✓           |                                |
| SCHEMA_LOAD_FAILED             | 3          | string_tests                                          | ✓           | 8.1.0, 8.2.0, lang_1.1.0, sc:8 |
| SCHEMA_SECTION_MISSING         | 1          | schema_tests                                          | ✓           |                                |
| SIDECAR_BRACES_INVALID         | 5          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| SIDECAR_INVALID                | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| SIDECAR_KEY_MISSING            | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EMPTY                      | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EXPRESSION_REPEATED        | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EXTENDED                   | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_EXTENSION_INVALID          | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_GROUP_ERROR                | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_INVALID                    | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_NAMESPACE_PREFIX_INVALID   | 3          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.3.0, sc:score_1.0.0, ts:8.3. |
| TAG_NOT_UNIQUE                 | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TAG_REQUIRES_CHILD             | 1          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| TEMPORAL_TAG_ERROR             | 24         | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.3.0, 8.4.0                   |
| UNITS_INVALID                  | 2          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.4.0                          |
| VALUE_INVALID                  | 4          | combo_tests, event_tests, sidecar_tests, string_tests | ✓           | 8.3.0, 8.4.0                   |
| WIKI_DELIMITERS_INVALID        | 1          | schema_tests                                          | ✓           |                                |

### Files by Error Code

#### CHARACTER_INVALID

- `CHARACTER_INVALID.json`

#### COMMA_MISSING

- `COMMA_MISSING.json`

#### DEFINITION_INVALID

- `DEFINITION_INVALID.json`

#### DEF_EXPAND_INVALID

- `DEF_EXPAND_INVALID.json`

#### DEF_INVALID

- `DEF_INVALID.json`

#### ELEMENT_DEPRECATED

- `ELEMENT_DEPRECATED.json`

#### PARENTHESES_MISMATCH

- `PARENTHESES_MISMATCH.json`

#### PLACEHOLDER_INVALID

- `PLACEHOLDER_INVALID.json`

#### SCHEMA_ATTRIBUTE_INVALID

- `SCHEMA_ATTRIBUTE_INVALID.json`

#### SCHEMA_ATTRIBUTE_VALUE_INVALID

- `SCHEMA_ATTRIBUTE_VALUE_INVALID_ALLOWED_CHARACTER.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_DEFAULT_UNIT.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_HED_ID.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_IN_LIBRARY.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_NON_PLACEHOLDER_HAS_CLASS.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_RELATED_TAG.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_SUGGESTED_TAG.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_UNIT_CLASS.json`
- `SCHEMA_ATTRIBUTE_VALUE_INVALID_VALUE_CLASS.json`

#### SCHEMA_CHARACTER_INVALID

- `SCHEMA_CHARACTER_INVALID.json`

#### SCHEMA_DEPRECATION_ERROR

- `SCHEMA_DEPRECATION_ERROR.json`

#### SCHEMA_DUPLICATE_NODE

- `SCHEMA_DUPLICATE_NODE.json`

#### SCHEMA_HEADER_INVALID

- `SCHEMA_HEADER_INVALID.json`

#### SCHEMA_LIBRARY_INVALID

- `SCHEMA_LIBRARY_INVALID.json`

#### SCHEMA_LOAD_FAILED

- `SCHEMA_LOAD_FAILED.json`

#### SCHEMA_SECTION_MISSING

- `SCHEMA_SECTION_MISSING.json`

#### SIDECAR_BRACES_INVALID

- `SIDECAR_BRACES_INVALID.json`

#### SIDECAR_INVALID

- `SIDECAR_INVALID.json`

#### SIDECAR_KEY_MISSING

- `SIDECAR_KEY_MISSING.json`

#### TAG_EMPTY

- `TAG_EMPTY.json`

#### TAG_EXPRESSION_REPEATED

- `TAG_EXPRESSION_REPEATED.json`

#### TAG_EXTENDED

- `TAG_EXTENDED.json`

#### TAG_EXTENSION_INVALID

- `TAG_EXTENSION_INVALID.json`

#### TAG_GROUP_ERROR

- `TAG_GROUP_ERROR.json`

#### TAG_INVALID

- `TAG_INVALID.json`

#### TAG_NAMESPACE_PREFIX_INVALID

- `SCHEMA_LOAD_FAILED.json`
- `TAG_NAMESPACE_PREFIX_INVALID.json`

#### TAG_NOT_UNIQUE

- `TAG_NOT_UNIQUE.json`

#### TAG_REQUIRES_CHILD

- `TAG_REQUIRES_CHILD.json`

#### TEMPORAL_TAG_ERROR

- `TEMPORAL_TAG_ERROR.json`
- `TEMPORAL_TAG_ERROR_DELAY.json`

#### UNITS_INVALID

- `UNITS_INVALID.json`

#### VALUE_INVALID

- `VALUE_INVALID.json`

#### WIKI_DELIMITERS_INVALID

- `SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

______________________________________________________________________

## Validator Integration Guide

### Integration Overview

The HED Test Suite provides standardized JSON test cases that all HED validators should pass. By integrating these tests, you ensure your validator:

- **Matches the specification**: Validates HED according to the official rules
- **Maintains consistency**: Produces the same results as other validators
- **Prevents regressions**: Catches changes in validation behavior
- **Documents behavior**: Tests serve as executable specifications

### Getting the Tests

#### Method 1: Git clone (Recommended)

Clone the repository to access all tests:

```bash
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
```

Update periodically to get new tests:

```bash
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
git submodule add https://github.com/hed-standard/hed-tests.git tests/hed-tests
git submodule update --init --recursive
```

### Test File Structure Integration

Tests are organized in two directories:

```
json_test_data/
├── validation_test_data/  # Validation error tests
│   ├── TAG_INVALID.json
│   ├── UNITS_INVALID.json
│   └── ...
└── schema_test_data/      # Schema validation tests
    ├── SCHEMA_ATTRIBUTE_INVALID.json
    └── ...
```

#### Consolidated files

For convenience, consolidated test files and lookup dictionaries are provided:

**Test files:**

- `json_test_data/validation_tests.json` - All validation tests in one file
- `json_test_data/schema_tests.json` - All schema tests in one file

**Lookup dictionaries:**

- `json_test_data/validation_code_dict.json` - Maps error codes to test names
- `json_test_data/validation_testname_dict.json` - Maps test names to error codes
- `json_test_data/schema_code_dict.json` - Maps error codes to test names (schema tests)
- `json_test_data/schema_testname_dict.json` - Maps test names to error codes (schema tests)

Generate these files using:

```bash
python src/scripts/consolidate_tests.py
```

### JSON Format

Each test file contains an array of test case objects:

```json
[
    {
        "error_code": "TAG_INVALID",
        "name": "tag-invalid-basic",
        "description": "Basic test for tags not in the schema",
        "schema": "8.4.0",
        "tests": {
            "string_tests": {
                "fails": ["Invalidtag"],
                "passes": ["Event"]
            }
        }
    }
]
```

### Integration Approaches

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
                            any(issue.code == error_code for issue in issues),
                            f"Expected {error_code} for: {hed_string}"
                        )
                    
                    # Test passing strings
                    for hed_string in test_case["tests"]["string_tests"].get("passes", []):
                        issues = validate_hed_string(hed_string, schema)
                        self.assertFalse(
                            any(issue.code == error_code for issue in issues),
                            f"Unexpected {error_code} for: {hed_string}"
                        )

if __name__ == '__main__':
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

#### Approach 2: Generate Test Cases

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
    
    test_code = f'''
import unittest
from hed_validator import validate_hed_string, load_schema

class Test{error_code}(unittest.TestCase):
'''
    
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
    
    with open(output_path, 'w') as f:
        f.write(test_code)
```

#### Approach 3: Test Report Comparison

Run tests and compare your results against a reference implementation.

```python
def compare_validation_results(test_case, reference_issues, your_issues):
    """Compare validation results against reference implementation."""
    error_code = test_case["error_code"]
    
    # Check if both found (or didn't find) the error
    ref_found = any(i.code == error_code for i in reference_issues)
    your_found = any(i.code == error_code for i in your_issues)
    
    if ref_found != your_found:
        return {
            "test": test_case["name"],
            "expected": ref_found,
            "actual": your_found,
            "status": "MISMATCH"
        }
    
    return {"status": "MATCH"}
```

### Test Types Implementation

#### String Tests

Simplest test type - raw HED strings.

```python
def run_string_tests(test_case, schema):
    """Execute string_tests from a test case."""
    error_code = test_case["error_code"]
    string_tests = test_case["tests"].get("string_tests", {})
    
    # Test strings that should fail
    for hed_string in string_tests.get("fails", []):
        issues = validate_hed_string(hed_string, schema)
        assert any(i.code == error_code for i in issues), \
            f"Expected {error_code} for: {hed_string}"
    
    # Test strings that should pass
    for hed_string in string_tests.get("passes", []):
        issues = validate_hed_string(hed_string, schema)
        assert not any(i.code == error_code for i in issues), \
            f"Unexpected {error_code} for: {hed_string}"
```

#### Sidecar Tests

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

#### Event Tests

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

#### Combo Tests

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

### Handling Definitions

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
        issues = validate_hed_string(
            hed_string, 
            schema, 
            definitions=definition_dict
        )
        # ... assertions
```

### Error Code Mapping

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

### CI/CD Integration

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

### Reporting Issues

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

### Integration Best Practices

1. **Run all tests**: Don't cherry-pick - run the entire suite
2. **Automate execution**: Integrate tests into CI/CD
3. **Track coverage**: Monitor which tests pass/fail over time
4. **Update regularly**: Pull latest tests periodically
5. **Report discrepancies**: Help improve the test suite
6. **Use schema versions**: Respect the schema version in each test
7. **Handle all test types**: Support string, sidecar, event, and combo tests

______________________________________________________________________

## Complete Test Index

### Quick Navigation Index

Complete index of 136 test cases in the HED test suite.

- [CHARACTER_INVALID](#character-invalid-1) (4 tests)
- [COMMA_MISSING](#comma-missing-1) (2 tests)
- [DEFINITION_INVALID](#definition-invalid-1) (10 tests)
- [DEF_EXPAND_INVALID](#def-expand-invalid-1) (6 tests)
- [DEF_INVALID](#def-invalid-1) (3 tests)
- [ELEMENT_DEPRECATED](#element-deprecated-1) (1 tests)
- [PARENTHESES_MISMATCH](#parentheses-mismatch-1) (2 tests)
- [PLACEHOLDER_INVALID](#placeholder-invalid-1) (4 tests)
- [SCHEMA_ATTRIBUTE_INVALID](#schema-attribute-invalid-1) (1 tests)
- [SCHEMA_ATTRIBUTE_VALUE_INVALID](#schema-attribute-value-invalid-1) (12 tests)
- [SCHEMA_CHARACTER_INVALID](#schema-character-invalid-1) (6 tests)
- [SCHEMA_DEPRECATION_ERROR](#schema-deprecation-error-1) (8 tests)
- [SCHEMA_DUPLICATE_NODE](#schema-duplicate-node-1) (2 tests)
- [SCHEMA_HEADER_INVALID](#schema-header-invalid-1) (2 tests)
- [SCHEMA_LIBRARY_INVALID](#schema-library-invalid-1) (8 tests)
- [SCHEMA_LOAD_FAILED](#schema-load-failed-1) (3 tests)
- [SCHEMA_SECTION_MISSING](#schema-section-missing-1) (1 tests)
- [SIDECAR_BRACES_INVALID](#sidecar-braces-invalid-1) (5 tests)
- [SIDECAR_INVALID](#sidecar-invalid-1) (2 tests)
- [SIDECAR_KEY_MISSING](#sidecar-key-missing-1) (2 tests)
- [TAG_EMPTY](#tag-empty-1) (3 tests)
- [TAG_EXPRESSION_REPEATED](#tag-expression-repeated-1) (3 tests)
- [TAG_EXTENDED](#tag-extended-1) (1 tests)
- [TAG_EXTENSION_INVALID](#tag-extension-invalid-1) (2 tests)
- [TAG_GROUP_ERROR](#tag-group-error-1) (4 tests)
- [TAG_INVALID](#tag-invalid-1) (3 tests)
- [TAG_NAMESPACE_PREFIX_INVALID](#tag-namespace-prefix-invalid-1) (3 tests)
- [TAG_NOT_UNIQUE](#tag-not-unique-1) (1 tests)
- [TAG_REQUIRES_CHILD](#tag-requires-child-1) (1 tests)
- [TEMPORAL_TAG_ERROR](#temporal-tag-error-1) (24 tests)
- [UNITS_INVALID](#units-invalid-1) (2 tests)
- [VALUE_INVALID](#value-invalid-1) (4 tests)
- [WIKI_DELIMITERS_INVALID](#wiki-delimiters-invalid-1) (1 tests)

### Detailed Test Listings

## CHARACTER_INVALID

**File**: `json_test_data/validation_test_data/CHARACTER_INVALID.json`

### character-invalid-non-printing-appears 🤖 AI 📝 Examples

**Description**: The HED string contains a UTF-8 character.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### curly-braces-not-in-sidecar 🤖 AI 📝 Examples

**Description**: The curly brace notation is used outside a sidecar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 1 fail, 1 pass

### invalid-character-name-value-class 🤖 AI 📝 Examples

**Description**: An invalid character was used in an 8.3.0 or greater style name value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 5 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 3 fail, 1 pass
- `combo_tests`: 1 fail, 0 pass

### invalid-character-name-value-class-early-schema 🤖 AI 📝 Examples

**Description**: An invalid character was as a value in a placeholder or as a tag extension.

**Schema**: 8.2.0 **Category**: validation

**Tests**:

- `string_tests`: 4 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 3 fail, 1 pass

## COMMA_MISSING

**File**: `json_test_data/validation_test_data/COMMA_MISSING.json`

### comma-missing-tag-and-group 🤖 AI 📝 Examples

**Description**: A tag and a tag group are not separated by commas: A(B,D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### comma-missing-tag-groups 🤖 AI 📝 Examples

**Description**: Two tag groups are not separated by commas: (A, B)(C, D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEFINITION_INVALID

**File**: `json_test_data/validation_test_data/DEFINITION_INVALID.json`

### definition-invalid-bad-number-of-placeholders 🤖 AI 📝 Examples

**Description**: A definition that includes a placeholder (`#`) does not have exactly two `#` characters.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-content-has-top-level-tag 🤖 AI 📝 Examples

**Description**: A tag with a required or unique attribute appears in a definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-empty-inner-group 🤖 AI 📝 Examples

**Description**: A definition's enclosing tag group has an empty inner group (i.e., the definition's contents).

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-inner-group-defs 🤖 AI 📝 Examples

**Description**: A definition's inner tag group contains `Definition`, `Def` or `Def-expand` tags.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 0 pass
- `event_tests`: 0 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-multiple-definition-tags 🤖 AI 📝 Examples

**Description**: A definition's enclosing tag group contains more than a `Definition` tag and an inner group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-multiple-definitions 🤖 AI 📝 Examples

**Description**: Multiple `Definition` tags with same name are encountered.

**Schema**: 8.4.0 **Category**: uniqueness

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-placeholder-conflict 🤖 AI 📝 Examples

**Description**: Definitions of the same name appear with and without a `#`.

**Schema**: 8.4.0 **Category**: consistency

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-placeholder-incorrect-of-positions 🤖 AI 📝 Examples

**Description**: A definition has placeholders (`#`) in incorrect positions.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-tag-group 🤖 AI 📝 Examples

**Description**: A Definition tag does not appear in a tag group at the top level in an annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 0 pass
- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-not-allowed-here 🤖 AI 📝 Examples

**Description**: A definition appears in an unexpected place such as an events file or sidecar.

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEF_EXPAND_INVALID

**File**: `json_test_data/validation_test_data/DEF_EXPAND_INVALID.json`

### def-expand-has-extras 🤖 AI 📝 Examples

**Description**: A Def-expand has extra tags or groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-bad-placeholder-value-or-units 🤖 AI 📝 Examples

**Description**: A `Def-expand` has an incorrect type of placeholder value.

**Schema**: 8.4.0 **Category**: value

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-missing-placeholder 🤖 AI 📝 Examples

**Description**: A `Def-expand` is missing an expected placeholder value or has an unexpected placeholder value.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-name-not-definition 🤖 AI 📝 Examples

**Description**: A `Def-expand` tag's name does not correspond to a definition.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-tags-not-in-definition 🤖 AI 📝 Examples

**Description**: The tags within a Def-expand do not match the corresponding definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-missing-inner-group 🤖 AI 📝 Examples

**Description**: A Def-expand is missing its inner group containing the definition.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEF_INVALID

**File**: `json_test_data/validation_test_data/DEF_INVALID.json`

### def-invalid-bad-placeholder-value 🤖 AI 📝 Examples

**Description**: A `Def` has a placeholder value of incorrect format or units for definition.

**Schema**: 8.4.0 **Category**: value

**Tests**:

- `string_tests`: 4 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-invalid-missing-placeholder 🤖 AI 📝 Examples

**Description**: A `Def` tag is missing an expected placeholder value or has an unexpected placeholder value.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-invalid-name 🤖 AI 📝 Examples

**Description**: A `Def` tag's name does not correspond to a definition.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## ELEMENT_DEPRECATED

**File**: `json_test_data/validation_test_data/ELEMENT_DEPRECATED.json`

### tag-deprecated ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A tag is deprecated

**Schema**: 8.2.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PARENTHESES_MISMATCH

**File**: `json_test_data/validation_test_data/PARENTHESES_MISMATCH.json`

### parentheses-mismatch-incorrect-nesting 🤖 AI 📝 Examples

**Description**: The open and closed parentheses are not correctly nested in the HED string.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### parentheses-mismatch-unmatched-parentheses 🤖 AI 📝 Examples

**Description**: A HED string does not have the same number of open and closed parentheses.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PLACEHOLDER_INVALID

**File**: `json_test_data/validation_test_data/PLACEHOLDER_INVALID.json`

### placeholder-invalid-#-in-categorical-column 🤖 AI 📝 Examples

**Description**: A JSON sidecar has a placeholder (`#`) in the HED dictionary for a categorical column.

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-#-misplaced 🤖 AI 📝 Examples

**Description**: A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child.

**Schema**: 8.4.0 **Category**: schema

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-value-column 🤖 AI 📝 Examples

**Description**: A JSON sidecar does not have exactly one placeholder (`#`) in each HED string representing a value column.

**Schema**: 8.4.0 **Category**: count

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-misplaced 🤖 AI 📝 Examples

**Description**: A `#` appears in a place that it should not (such as in the `HED` column of an event file outside a definition).

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 0 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## SCHEMA_ATTRIBUTE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_INVALID.json`

### attribute-invalid-unknown ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

## SCHEMA_ATTRIBUTE_VALUE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-factor-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit has an invalid conversion factor

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 4 fail, 1 pass

### attribute-default-unit-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit class has an invalid default value

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-allowed-character ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit has an invalid conversion factor

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### attribute-invalid-hed-id-changed ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema value class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-hed-id-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema value class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-hed-id-out-range ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema value class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-in-library ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit has an invalid in library attribute(most other library errors are SCHEMA_LIBRARY_INVALID

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-unit-class ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-value-class ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema value class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-on-nonplaceholder-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A non placeholder tag has takes value, unit class, or value class

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

### attribute-relatedTag-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A related tag points to an unknown tag

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 2 pass

### attribute-suggestedTag-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A suggested tag points to an unknown tag

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 2 pass

## SCHEMA_CHARACTER_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_CHARACTER_INVALID.json`

### schema-character-allowed-character-unit ⚠️ Warning

**Description**: Allowed character properly works on units.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### schema-character-invalid-description ⚠️ Warning

**Description**: Description does not contain banned characters.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-other-term ⚠️ Warning

**Description**: Invalid character in a tag term.

**Schema**: any

**Tests**:

- `schema_tests`: 6 fail, 1 pass

### schema-character-invalid-prologue ⚠️ Warning 🤖 AI 📝 Examples

**Description**: Invalid character in prologue or epilogue.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-tag ⚠️ Warning

**Description**: Invalid character in a tag term.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-utf8-other-term ⚠️ Warning

**Description**: UTF8 characters (valid) in term.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

## SCHEMA_DEPRECATION_ERROR

**File**: `json_test_data/schema_test_data/SCHEMA_DEPRECATION_ERROR.json`

### schema-deprecated-attribute-invalid ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is an unhandled deprecated attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-deprecated-default-unit ⚠️ Warning

**Description**: A schema deprecation issue, deprecated default units

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### schema-deprecated-deprecated-attribute ⚠️ Warning

**Description**: A schema deprecation issue, an attribute of an element is deprecated

**Schema**: any

**Tests**:

- `schema_tests`: 5 fail, 5 pass

### schema-deprecated-deprecated-property ⚠️ Warning

**Description**: A schema deprecation issue, a property of an attribute is is deprecated

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-deprecated-invalid-child ⚠️ Warning

**Description**: A schema deprecation issue, saying there is an invalid child of a deprecated node

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-deprecated-invalid-suggested-related-tag ⚠️ Warning

**Description**: A schema deprecation issue, saying a related or suggested tag points to a deprecated tag

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 4 pass

### schema-deprecated-unit-class ⚠️ Warning

**Description**: A schema deprecation issue, deprecated value or unit class

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-deprecated-value-class ⚠️ Warning

**Description**: A schema deprecation issue, deprecated value or unit class

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_DUPLICATE_NODE

**File**: `json_test_data/schema_test_data/SCHEMA_DUPLICATE_NODE.json`

### attribute-duplicate-node ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is a duplicate node.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 6 fail, 1 pass

### attribute-duplicate-node-unit ⚠️ Warning

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_HEADER_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_HEADER_INVALID.json`

### schema-header-malformed-attribute ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-header-unknown-attribute ⚠️ Warning

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_LIBRARY_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_LIBRARY_INVALID.json`

### library-invalid-bad-name ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema library issue, indicating the name is invalid.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

### library-invalid-bad_with-standard ⚠️ Warning

**Description**: A schema library issue, the with-standard attribute is present without the library attribute.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-bad_with-standard-version ⚠️ Warning

**Description**: A schema library issue, indicating it references a version of the standard that can't be found.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-rooted-in-duplicate-other ⚠️ Warning

**Description**: A schema library issue, indicating the InLibrary attribute appears when it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-in-library-present ⚠️ Warning

**Description**: A schema library issue, indicating the InLibrary attribute appears when it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-not-in-base ⚠️ Warning

**Description**: A schema library issue, rooted tag does not exist.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-rooted-not-top-level ⚠️ Warning

**Description**: A schema library issue, indicating a node is being rooted that is not a top level node.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-present ⚠️ Warning

**Description**: A schema library issue, indicating the rooted property appears in a file it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

## SCHEMA_LOAD_FAILED

**File**: `json_test_data/validation_test_data/SCHEMA_LOAD_FAILED.json`

### different-standard-schemas-in-same-merge-group 🤖 AI 📝 Examples

**Description**: Schemas in a merge group must be associated with the same standard schema.

**Schema**: 8.1.0, testlib_2.0.0 **Category**: schema_development

**Tests**:

- `string_tests`: 2 fail, 0 pass

### extra-standard-schemas-in-same-merge-group

**Description**: Standard schema in same group as its partners is okay.

**Schema**: 8.2.0, testlib_2.0.0, testlib_3.0.0, sc:8.1.0

**Tests**:

- `string_tests`: 0 fail, 2 pass

### incompatible-merge-schemas

**Description**: Schemas in a merge group must be associated with the same standard schema.

**Schema**: score_2.0.0, lang_1.1.0

**Tests**:

- `string_tests`: 2 fail, 0 pass

## SCHEMA_SECTION_MISSING

**File**: `json_test_data/schema_test_data/SCHEMA_SECTION_MISSING.json`

### schema-section-missing ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 9 fail, 1 pass

## SIDECAR_BRACES_INVALID

**File**: `json_test_data/validation_test_data/SIDECAR_BRACES_INVALID.json`

### sidecar-braces-appear-as-value-rather-than-tag 🤖 AI 📝 Examples

**Description**: The curly braces are in a value rather than as a separate tag substitute.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### sidecar-braces-circular-reference 🤖 AI 📝 Examples

**Description**: The item in curly braces has a HED annotation that contains curly braces.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 2 fail, 2 pass
- `combo_tests`: 0 fail, 1 pass

### sidecar-braces-contents-invalid 🤖 AI 📝 Examples

**Description**: The item in curly braces is not the word HED or a column name with HED annotations in the sidecar.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 2 pass
- `combo_tests`: 0 fail, 1 pass

### sidecar-braces-invalid-spot 🤖 AI 📝 Examples

**Description**: A curly brace reference must only appear where a tag could.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass

### sidecar-braces-self-reference 🤖 AI 📝 Examples

**Description**: The item in curly braces has a HED annotation that contains itself.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 1 fail, 3 pass
- `combo_tests`: 1 fail, 2 pass

## SIDECAR_INVALID

**File**: `json_test_data/validation_test_data/SIDECAR_INVALID.json`

### sidecar-invalid-key-at-wrong-level 🤖 AI 📝 Examples

**Description**: The HED key is not a second-level dictionary key.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### sidecar-invalid-na-annotated 🤖 AI 📝 Examples

**Description**: An annotation entry is provided for `n/a`.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## SIDECAR_KEY_MISSING

**File**: `json_test_data/validation_test_data/SIDECAR_KEY_MISSING.json`

### sidecar-key-missing ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A value in a categorical column does not have an expected entry in a sidecar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `combo_tests`: 1 fail, 1 pass

### sidecar-refers-to-missing-tsv-hed-column ⚠️ Warning 🤖 AI 📝 Examples

**Description**: (Warning) A sidecar uses a `{HED}` column which does not appear in the corresponding tsv file.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 0 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EMPTY

**File**: `json_test_data/validation_test_data/TAG_EMPTY.json`

### tag-empty-begin-end-comma 🤖 AI 📝 Examples

**Description**: A HED string begins or ends with a comma (ignoring white space).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-empty-empty-parentheses 🤖 AI 📝 Examples

**Description**: A tag group is empty (i.e., empty parentheses are not allowed).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-empty-extra-commas-or-parentheses 🤖 AI 📝 Examples

**Description**: A HED string has extra commas or parentheses separated by only white space.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 5 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXPRESSION_REPEATED

**File**: `json_test_data/validation_test_data/TAG_EXPRESSION_REPEATED.json`

### tag-expression-repeated-same-level 🤖 AI 📝 Examples

**Description**: A tag is repeated in the same tag group or level.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tags-duplicated-across-multiple-rows 🤖 AI 📝 Examples

**Description**: Tags are repeated because two rows have the same onset value.

**Schema**: 8.4.0 **Category**: duplication

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tags-with-duplicated-onsets-across-multiple-rows 🤖 AI 📝 Examples

**Description**: Tags are repeated because two rows have the same onset value.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENDED

**File**: `json_test_data/validation_test_data/TAG_EXTENDED.json`

### tag-extended-extension ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A tag represents an extension from the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 7 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENSION_INVALID

**File**: `json_test_data/validation_test_data/TAG_EXTENSION_INVALID.json`

### tag-extension-invalid-bad-node-name 🤖 AI 📝 Examples

**Description**: A tag extension term does not comply with rules for schema nodes.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-extension-invalid-duplicate 🤖 AI 📝 Examples

**Description**: A tag extension term is already in the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_GROUP_ERROR

**File**: `json_test_data/validation_test_data/TAG_GROUP_ERROR.json`

### multiple-top-level-tags-in-same-group 🤖 AI 📝 Examples

**Description**: Multiple tags with the topLevelTagGroup attribute appear in the same top-level tag group. (Delay and Duration are allowed to be in the same topLevelTagGroup).

**Schema**: 8.4.0 **Category**: cardinality

**Tests**:

- `string_tests`: 4 fail, 2 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-deferred-in-splice 🤖 AI 📝 Examples

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-missing 🤖 AI 📝 Examples

**Description**: A tag has tagGroup or topLevelTagGroup attribute, but is not enclosed in parentheses.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 5 fail, 4 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-not-top-level 🤖 AI 📝 Examples

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_INVALID

**File**: `json_test_data/validation_test_data/TAG_INVALID.json`

### tag-has-extra-white space 🤖 AI 📝 Examples

**Description**: A HED tag has extra internal whitespace, including directly before or after slashes.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 4 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-has-leading-trailing-or-consecutive-slashes 🤖 AI 📝 Examples

**Description**: A HED tag has leading, trailing or consecutive slashes.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 8 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-invalid-in-schema 🤖 AI 📝 Examples

**Description**: The tag is not valid in the schema it is associated with.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_NAMESPACE_PREFIX_INVALID

**File**: `json_test_data/validation_test_data/TAG_NAMESPACE_PREFIX_INVALID.json`

### tag-namespace_prefix-invalid-characters 🤖 AI 📝 Examples

**Description**: A tag prefix has invalid characters.

**Schema**: 8.3.0, sc:score_1.0.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-namespace_prefix-with-colon-values 🤖 AI 📝 Examples

**Description**: A tag prefix has invalid characters.

**Schema**: ts:8.3.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-with-namespace-has-no-schema

**Description**: A tag starting with name: does not have an associated schema.

**Schema**: 8.3.0, sc:score_1.0.0

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_NOT_UNIQUE

**File**: `json_test_data/validation_test_data/TAG_NOT_UNIQUE.json`

### tag-not-unique 🤖 AI 📝 Examples

**Description**: A tag with unique attribute appears more than once in an event-level HED string.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_REQUIRES_CHILD

**File**: `json_test_data/validation_test_data/TAG_REQUIRES_CHILD.json`

### tag-requires-child-missing 🤖 AI 📝 Examples

**Description**: A tag has the requireChild schema attribute but does not have a child.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TEMPORAL_TAG_ERROR

**File**: `json_test_data/validation_test_data/TEMPORAL_TAG_ERROR.json`

### na-in-onset column 🤖 AI 📝 Examples

**Description**: n/a is in the onset column.

**Schema**: 8.4.0 **Category**: data_format

**Tests**:

- `combo_tests`: 2 fail, 2 pass

### temporal-tag-error-duplicated-onset-or-offset 🤖 AI 📝 Examples

**Description**: An Onset or an Offset with a given Def or Def-expand anchor appears in the same event marker with another Onset or Offset that uses the same anchor.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-duplicated-onset-or-offset-delay 🤖 AI 📝 Examples

**Description**: An Onset or an Offset with a given Def or Def-expand anchor appears in the same event marker with another Onset or Offset that uses the same anchor.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-duration-group 🤖 AI 📝 Examples

**Description**: A Duration or Delay has extra tags or groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 3 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 0 fail, 1 pass

### temporal-tag-error-extra tags 🤖 AI 📝 Examples

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-extra tags-delay 🤖 AI 📝 Examples

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras 🤖 AI 📝 Examples

**Description**: An Inset group has tags or groups in addition to its defining Def or Def-expand.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras-delay 🤖 AI 📝 Examples

**Description**: An Inset group has tags or groups in addition to its defining Def or Def-expand.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-outside-its-event 🤖 AI 📝 Examples

**Description**: An Inset tag is not grouped with a Def or Def-expand of an ongoing Onset.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-outside-its-event-delay 🤖 AI 📝 Examples

**Description**: An Inset tag is not grouped with a Def or Def-expand of an ongoing Onset.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-mismatch-delay 🤖 AI 📝 Examples

**Description**: An Offset tag associated with a given definition appears after a previous Offset tag without the appearance of an intervening Onset of the same name.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group 🤖 AI 📝 Examples

**Description**: An Onset or Offset tag appears in a nested tag group (not a top-level tag group).

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group-delay 🤖 AI 📝 Examples

**Description**: A delay appears in a group not in the top level.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group 🤖 AI 📝 Examples

**Description**: An Onset or Offset tag does not appear in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group-delay 🤖 AI 📝 Examples

**Description**: A Delay is not in the tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-offset-has-groups 🤖 AI 📝 Examples

**Description**: An Offset appears with one or more tags or additional tag groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-offset-has-groups-delay 🤖 AI 📝 Examples

**Description**: An Offset appears with one or more tags or additional tag groups.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-offset-with-no-onset 🤖 AI 📝 Examples

**Description**: An Offset tag associated with a given definition appears after a previous Offset tag without the appearance of an intervening Onset of the same name.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups 🤖 AI 📝 Examples

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups-delay 🤖 AI 📝 Examples

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-tag-appears-where-not-allowed 🤖 AI 📝 Examples

**Description**: A temporal tag appears appears in a tsv with no onset column

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-tag-appears-where-not-allowed-delay 🤖 AI 📝 Examples

**Description**: An Inset, Offset, or Onset tag appears in a tsv with no onset column

**Schema**: 8.3.0 **Category**: context

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs 🤖 AI 📝 Examples

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 1 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs-delay 🤖 AI 📝 Examples

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 1 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## UNITS_INVALID

**File**: `json_test_data/validation_test_data/UNITS_INVALID.json`

### units-invalid-for-unit-class 🤖 AI 📝 Examples

**Description**: A tag has a value with units that are invalid or not of the correct unit class for the tag.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### units-invalid-si-units 🤖 AI 📝 Examples

**Description**: A unit modifier is applied to units that are not SI units.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## VALUE_INVALID

**File**: `json_test_data/validation_test_data/VALUE_INVALID.json`

### invalid-character-numeric-class 🤖 AI 📝 Examples

**Description**: An invalid character was used in an 8.3.0 or greater style numeric value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 8 fail, 10 pass
- `sidecar_tests`: 1 fail, 1 pass

### value-invalid-#-substitution 🤖 AI 📝 Examples

**Description**: The value substituted for a placeholder (`#`) is not valid.

**Schema**: 8.3.0 **Category**: validation

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### value-invalid-blank-missing-before-units 🤖 AI 📝 Examples

**Description**: The units are not separated from the value by a single blank.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### value-invalid-incompatible-value-class 🤖 AI 📝 Examples

**Description**: A tag placeholder value is incompatible with the specified value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## WIKI_DELIMITERS_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-format ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit has an invalid conversion factor due to bad formatting

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 0 pass

______________________________________________________________________

## Support and Resources

### Documentation

- **[HED Homepage](https://www.hedtags.org)**: Project overview
- **[HED Specification](https://www.hedtags.org/hed-specification)**: Formal validation rules
- **[HED Schemas](https://github.com/hed-standard/hed-schemas)**: Vocabulary definitions
- **[HED Python Validator](https://github.com/hed-standard/hed-python)**: Python implementation
- **[HED JavaScript Validator](https://github.com/hed-standard/hed-javascript)**: JavaScript implementation

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/hed-standard/hed-tests/issues)
- **Discussions**: [GitHub Discussions](https://github.com/hed-standard/hed-tests/discussions)
- **Email**: [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)

### Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on adding new tests or improving existing ones.

______________________________________________________________________

**End of User Guide**
