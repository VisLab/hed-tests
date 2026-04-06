# HED test suite

[![CI](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml/badge.svg)](https://github.com/hed-standard/hed-tests/actions/workflows/ci.yaml) [![Docs](https://img.shields.io/badge/docs-hed--tests-blue.svg)](https://www.hedtags.org/hed-tests) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Official JSON test suite for HED (Hierarchical Event Descriptors) validation**

This repository provides comprehensive, machine-readable test cases for validating HED validator implementations across all platforms (Python, JavaScript, and future implementations). Tests ensure consistent validation behavior and serve as AI-readable specifications for HED validation rules.

## Quick start

```powershell
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
├── json_test_data/
│   ├── validation_test_data/    # One JSON file per validation error code
│   ├── schema_test_data/        # One JSON file per schema error code
│   ├── validation_tests.json    # Consolidated validation tests
│   ├── schema_tests.json        # Consolidated schema tests
│   └── *_dict.json              # Error code ↔ test name lookup dictionaries
├── src/scripts/                 # consolidate_tests.py and validation scripts
├── tests/                       # Test analysis utilities
└── docs/                        # Documentation source
```

## Test statistics

- **Validation tests**: 25 error codes
- **Schema tests**: 18 error codes
- **Total test cases**: 500+ individual tests
- **Test types**: string, sidecar, event, and combo

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
