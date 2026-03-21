# HED test suite developer instructions

If `.status/local-environment.md` exists, read it first for local OS, shell, and virtual environment details.

Use Google format for docstrings (`Parameters:` not `Args:`).
When you create summaries of what you did, always put them in a `.status/` directory at the repository root.

## Markdown style

- Use **sentence case** for all headings: capitalize only the first word (and proper nouns/acronyms like HED, JSON, BIDS, AI).
- Correct: `## Test file format`
- Incorrect: `## Test File Format`

## Project overview

This repository (`hed-tests`) hosts the **official JSON test suite** for HED (Hierarchical Event Descriptors) validation. It ensures consistent validation behavior across all HED validator implementations and provides AI-readable validation specifications.

**Purpose**: Provide a centralized, version-controlled test suite that:
- Validates HED validators (Python, JavaScript, and future implementations)
- Serves as machine-readable specification documentation
- Enables AI systems to understand HED validation rules
- Ensures cross-platform validation consistency

### Related repositories
- **[hed-python](https://github.com/hed-standard/hed-python)**: Python validator implementation (primary consumer)
- **[hed-javascript](https://github.com/hed-standard/hed-javascript)**: JavaScript validator implementation (primary consumer)
- **[hed-specification](https://github.com/hed-standard/hed-specification)**: Formal specification defining HED rules (source of truth)
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)**: HED schema vocabulary definitions (referenced in tests)

## Repository structure

```
hed-tests/
├── json_test_data/                     # All test data (primary content)
│   ├── validation_test_data/           # Individual error code test files
│   │   ├── TAG_INVALID.json           # Tests for TAG_INVALID error
│   │   └── ...                        # One file per error code
│   ├── schema_test_data/               # Schema validation test files
│   │   ├── SCHEMA_ATTRIBUTE_INVALID.json
│   │   └── ...                        # Schema-level validation tests
│   ├── validation_tests.json           # Consolidated validation tests
│   ├── schema_tests.json               # Consolidated schema tests
│   ├── *_code_dict.json                # Error code → test name lookups
│   └── *_testname_dict.json            # Test name → error code lookups
├── src/scripts/
│   └── consolidate_tests.py            # Combines individual tests
├── tests/                              # Test analysis utilities (unittest)
├── docs/                               # Documentation
├── .github/workflows/                  # CI/CD pipelines
└── pyproject.toml                      # All dependencies managed here
```

## Build and validation commands

Always activate the virtual environment before running any command. The working sequence is:

```bash
# 1. Install (first time or after dependency changes)
pip install -e ".[dev,docs]"

# 2. Run tests
python -m unittest tests.test_summarize_testdata -v

# 3. Consolidate test files and regenerate dictionaries
python src/scripts/consolidate_tests.py

# 4. Validate JSON structure (if script exists)
python src/scripts/validate_test_structure.py json_test_data/validation_test_data/
python src/scripts/validate_test_structure.py json_test_data/schema_test_data/
```

After editing any test JSON file, always run step 3 to regenerate consolidated files. After running commands, verify there are no errors before considering the task done.

## Test file format

Each JSON file in `validation_test_data/` or `schema_test_data/` contains an array of test case objects:

```json
[
    {
        "error_code": "TAG_INVALID",
        "alt_codes": ["PLACEHOLDER_INVALID"],
        "name": "tag-invalid-in-schema",
        "description": "Human-readable description",
        "warning": false,
        "schema": "8.4.0",
        "error_category": "semantic",
        "common_causes": ["List of common causes"],
        "explanation": "Detailed explanation for AI/developers",
        "correction_strategy": "How to fix the issue",
        "correction_examples": [
            {"wrong": "...", "correct": "...", "explanation": "..."}
        ],
        "definitions": [],
        "tests": {
            "string_tests":  { "fails": [...], "passes": [...] },
            "sidecar_tests": { "fails": [...], "passes": [...] },
            "event_tests":   { "fails": [...], "passes": [...] },
            "combo_tests":   { "fails": [...], "passes": [...] }
        }
    }
]
```

### Test types
1. **string_tests**: Raw HED strings
2. **sidecar_tests**: JSON sidecar files (BIDS metadata)
3. **event_tests**: Tabular event data with HED columns
4. **combo_tests**: Combined sidecar + event data (realistic BIDS scenarios)

## Adding or editing tests

1. Edit the corresponding file in `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/` (one error code per file)
2. Include both failing and passing test cases
3. Always include AI metadata: `explanation`, `common_causes`, `correction_strategy`, `correction_examples`
4. Validate JSON syntax
5. Run consolidation to update consolidated files and dictionaries

## Error code categories

- **Syntax**: `CHARACTER_INVALID`, `COMMA_MISSING`, `PARENTHESES_MISMATCH`, `TAG_EMPTY`
- **Semantic**: `TAG_INVALID`, `TAG_EXTENDED`, `TAG_EXTENSION_INVALID`, `VALUE_INVALID`, `UNITS_INVALID`
- **Definition**: `DEFINITION_INVALID`, `DEF_INVALID`, `DEF_EXPAND_INVALID`
- **Sidecar**: `SIDECAR_INVALID`, `SIDECAR_BRACES_INVALID`, `SIDECAR_KEY_MISSING`
- **Schema**: `SCHEMA_ATTRIBUTE_INVALID`, `SCHEMA_DUPLICATE_NODE`, `SCHEMA_HEADER_INVALID`
- **Temporal**: `TEMPORAL_TAG_ERROR`, `TEMPORAL_TAG_ERROR_DELAY`

## CI/CD pipeline

GitHub Actions in `.github/workflows/`:
- `ci.yaml`: Validate JSON structure and format
- `black.yaml`: Python code formatting
- `codespell.yaml`: Spell checking
- `links.yaml`: Broken link checking

Replicate CI checks locally before pushing: run tests, consolidation, and JSON validation.

## Naming conventions

- Test files: `ERROR_CODE.json` (uppercase, underscores)
- Test names: `error-code-specific-scenario` (lowercase, hyphens)
- JSON formatting: 4-space indentation

## Common pitfalls

- Don't hardcode file paths — use relative paths
- Validate JSON syntax before committing
- Don't duplicate test cases across files
- Keep test files focused on single error codes
- Always run consolidation after editing test files

Trust these instructions. Only search for additional information if something here is incomplete or found to be incorrect.
