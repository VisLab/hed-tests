# HED test suite

[![CI](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml/badge.svg)](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml) [![Docs](https://img.shields.io/badge/docs-hed--tests-blue.svg)](https://www.hedtags.org/hed-tests) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Official JSON test suite for HED (Hierarchical Event Descriptors) validation**

This repository provides comprehensive, machine-readable test cases for validating HED validator implementations across all platforms (Python, JavaScript, and future implementations). Tests ensure consistent validation behavior and serve as AI-readable specifications for HED validation rules.

## Quick start

```bash
# Linux/macOS
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,docs]"
```

```powershell
# Windows PowerShell
git clone https://github.com/hed-standard/hed-tests.git
cd hed-tests
python -m venv .venv
.venv/Scripts/activate.ps1
pip install -e ".[dev,docs]"
```

See the **[user guide](https://www.hedtags.org/hed-tests)** for complete documentation, including:

- Test file format and test types
- Integrating the test suite into your validator
- Error code categories and coverage
- Contributing new tests

## Repository structure

```
hed-tests/
|-- json_test_data/
|   |-- validation_test_data/    # One JSON file per validation error code
|   |-- schema_test_data/        # One JSON file per schema error code
|   |-- validation_tests.json    # Consolidated validation tests (generated)
|   |-- schema_tests.json        # Consolidated schema tests (generated)
|   `-- *_dict.json              # Error code <-> test name lookups (generated)
|-- src/scripts/                 # Maintenance scripts (see below)
|-- src/schemas/                 # JSON schema the test files must conform to
|-- tests/                       # Unit tests for the maintenance scripts
`-- docs/                        # Documentation source
```

See [json_test_data/README.md](json_test_data/README.md) for what each JSON file represents and how validators consume them.

## Maintenance scripts

Four scripts in `src/scripts/` maintain the test suite. All run from the repository root; CI runs all four on every push.

### validate_test_structure.py

Checks that test files conform to the official JSON schema in `src/schemas/test_schema.json`: JSON syntax, required fields, field types, and test structure. After editing any test file under `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/`, run it with no arguments to check everything, or narrow it to just the directory or file you edited:

```bash
# Validate all test directories
python src/scripts/validate_test_structure.py

# Validate one directory
python src/scripts/validate_test_structure.py json_test_data/schema_test_data

# Validate a single file
python src/scripts/validate_test_structure.py --file json_test_data/validation_test_data/TAG_INVALID.json
```

Options: `--schema <path>` to validate against a different schema, `--verbose` for per-file detail.

### consolidate_tests.py

Combines the individual per-error-code files into the six generated files at the top of `json_test_data/` (the two consolidated test files plus four lookup dictionaries) that validators actually consume:

```bash
# Regenerate all six consolidated files
python src/scripts/consolidate_tests.py

# Preview what would be regenerated without writing anything
python src/scripts/consolidate_tests.py --dry-run
```

**Run this after every test edit and commit the regenerated files together with the edit.** CI runs the script but does not fail when the committed copies are stale, so an uncommitted regeneration leaves validators consuming outdated tests.

### check_coverage.py

Reports which error codes have tests, how many test cases each has, which test types (string/sidecar/event/combo) are covered, and whether the AI metadata fields are complete. Use it to find coverage gaps before adding tests:

```bash
# Print the coverage report to the console
python src/scripts/check_coverage.py

# Write the coverage report to a markdown file instead
python src/scripts/check_coverage.py --markdown report.md
```

For current test statistics, run this script rather than trusting any count written in documentation.

### generate_test_index.py

Regenerates `docs/test_index.md`, the searchable index of every test case organized by error code:

```bash
# Regenerate docs/test_index.md (the default output)
python src/scripts/generate_test_index.py

# Write the index to a different file
python src/scripts/generate_test_index.py --output some_other_file.md

# Produce the index as JSON instead of markdown
python src/scripts/generate_test_index.py --format json
```

`docs/test_index.md` is generated - edit tests, not the index.

### Typical maintenance workflow

1. Edit or add a test file in `json_test_data/validation_test_data/` or `json_test_data/schema_test_data/` (one error code per file).
2. Validate: `python src/scripts/validate_test_structure.py` (or narrow it to the directory you edited).
3. Regenerate: `python src/scripts/consolidate_tests.py`.
4. Check the result: `python src/scripts/check_coverage.py` and `python -m unittest discover tests`.
5. Commit the edited file **and** the regenerated consolidated files together.

## Related repositories

- **[hed-python](https://github.com/hed-standard/hed-python)**: Python validator implementation
- **[hed-javascript](https://github.com/hed-standard/hed-javascript)**: JavaScript validator implementation
- **[hed-specification](https://github.com/hed-standard/hed-specification)**: Formal HED specification
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)**: HED vocabulary schemas

## Versioning

Semantic versioning: major = breaking format change, minor = new tests/error codes, patch = bug fixes. Current version: **1.0.0**

## License

MIT License — see [LICENSE](LICENSE) for details.

## Citation

If you use HED in your research, please cite:

```
Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2022).
Building FAIR functionality: Annotating events in time series data using
Hierarchical Event Descriptors (HED). Neuroinformatics, 1-17.
```

## Support

- **Documentation**: https://www.hedtags.org/hed-tests
- **Issues**: https://github.com/hed-standard/hed-tests/issues
- **Discussions**: https://github.com/orgs/hed-standard/discussions
- **Email**: hed.maintainers@gmail.com
