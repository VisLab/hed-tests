# HED test suite index

Complete index of 136 test cases in the HED test suite.

## Quick navigation

- [CHARACTER_INVALID](#character-invalid) (4 tests)
- [COMMA_MISSING](#comma-missing) (2 tests)
- [DEFINITION_INVALID](#definition-invalid) (10 tests)
- [DEF_EXPAND_INVALID](#def-expand-invalid) (6 tests)
- [DEF_INVALID](#def-invalid) (3 tests)
- [ELEMENT_DEPRECATED](#element-deprecated) (1 tests)
- [PARENTHESES_MISMATCH](#parentheses-mismatch) (2 tests)
- [PLACEHOLDER_INVALID](#placeholder-invalid) (4 tests)
- [SCHEMA_ATTRIBUTE_INVALID](#schema-attribute-invalid) (1 tests)
- [SCHEMA_ATTRIBUTE_VALUE_INVALID](#schema-attribute-value-invalid) (12 tests)
- [SCHEMA_CHARACTER_INVALID](#schema-character-invalid) (6 tests)
- [SCHEMA_DEPRECATION_ERROR](#schema-deprecation-error) (8 tests)
- [SCHEMA_DUPLICATE_NODE](#schema-duplicate-node) (2 tests)
- [SCHEMA_HEADER_INVALID](#schema-header-invalid) (2 tests)
- [SCHEMA_LIBRARY_INVALID](#schema-library-invalid) (8 tests)
- [SCHEMA_LOAD_FAILED](#schema-load-failed) (3 tests)
- [SCHEMA_SECTION_MISSING](#schema-section-missing) (1 tests)
- [SIDECAR_BRACES_INVALID](#sidecar-braces-invalid) (5 tests)
- [SIDECAR_INVALID](#sidecar-invalid) (2 tests)
- [SIDECAR_KEY_MISSING](#sidecar-key-missing) (2 tests)
- [TAG_EMPTY](#tag-empty) (3 tests)
- [TAG_EXPRESSION_REPEATED](#tag-expression-repeated) (3 tests)
- [TAG_EXTENDED](#tag-extended) (1 tests)
- [TAG_EXTENSION_INVALID](#tag-extension-invalid) (2 tests)
- [TAG_GROUP_ERROR](#tag-group-error) (4 tests)
- [TAG_INVALID](#tag-invalid) (3 tests)
- [TAG_NAMESPACE_PREFIX_INVALID](#tag-namespace-prefix-invalid) (3 tests)
- [TAG_NOT_UNIQUE](#tag-not-unique) (1 tests)
- [TAG_REQUIRES_CHILD](#tag-requires-child) (1 tests)
- [TEMPORAL_TAG_ERROR](#temporal-tag-error) (24 tests)
- [UNITS_INVALID](#units-invalid) (2 tests)
- [VALUE_INVALID](#value-invalid) (4 tests)
- [WIKI_DELIMITERS_INVALID](#wiki-delimiters-invalid) (1 tests)

## CHARACTER_INVALID

**File**: `json_test_data/validation_tests/CHARACTER_INVALID.json`

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

**File**: `json_test_data/validation_tests/COMMA_MISSING.json`

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

**File**: `json_test_data/validation_tests/DEFINITION_INVALID.json`

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

**File**: `json_test_data/validation_tests/DEF_EXPAND_INVALID.json`

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

**File**: `json_test_data/validation_tests/DEF_INVALID.json`

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

**File**: `json_test_data/validation_tests/ELEMENT_DEPRECATED.json`

### tag-deprecated ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A tag is deprecated

**Schema**: 8.2.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PARENTHESES_MISMATCH

**File**: `json_test_data/validation_tests/PARENTHESES_MISMATCH.json`

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

**File**: `json_test_data/validation_tests/PLACEHOLDER_INVALID.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_ATTRIBUTE_INVALID.json`

### attribute-invalid-unknown ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

## SCHEMA_ATTRIBUTE_VALUE_INVALID

**File**: `json_test_data/schema_tests/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_CHARACTER_INVALID.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_DEPRECATION_ERROR.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_DUPLICATE_NODE.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_HEADER_INVALID.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_LIBRARY_INVALID.json`

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

**File**: `json_test_data/validation_tests/SCHEMA_LOAD_FAILED.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_SECTION_MISSING.json`

### schema-section-missing ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 9 fail, 1 pass

## SIDECAR_BRACES_INVALID

**File**: `json_test_data/validation_tests/SIDECAR_BRACES_INVALID.json`

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

**File**: `json_test_data/validation_tests/SIDECAR_INVALID.json`

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

**File**: `json_test_data/validation_tests/SIDECAR_KEY_MISSING.json`

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

**File**: `json_test_data/validation_tests/TAG_EMPTY.json`

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

**File**: `json_test_data/validation_tests/TAG_EXPRESSION_REPEATED.json`

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

**File**: `json_test_data/validation_tests/TAG_EXTENDED.json`

### tag-extended-extension ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A tag represents an extension from the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 7 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENSION_INVALID

**File**: `json_test_data/validation_tests/TAG_EXTENSION_INVALID.json`

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

**File**: `json_test_data/validation_tests/TAG_GROUP_ERROR.json`

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

**File**: `json_test_data/validation_tests/TAG_INVALID.json`

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

**File**: `json_test_data/validation_tests/TAG_NAMESPACE_PREFIX_INVALID.json`

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

**File**: `json_test_data/validation_tests/TAG_NOT_UNIQUE.json`

### tag-not-unique 🤖 AI 📝 Examples

**Description**: A tag with unique attribute appears more than once in an event-level HED string.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_REQUIRES_CHILD

**File**: `json_test_data/validation_tests/TAG_REQUIRES_CHILD.json`

### tag-requires-child-missing 🤖 AI 📝 Examples

**Description**: A tag has the requireChild schema attribute but does not have a child.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TEMPORAL_TAG_ERROR

**File**: `json_test_data/validation_tests/TEMPORAL_TAG_ERROR.json`

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

**File**: `json_test_data/validation_tests/UNITS_INVALID.json`

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

**File**: `json_test_data/validation_tests/VALUE_INVALID.json`

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

**File**: `json_test_data/schema_tests/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-format ⚠️ Warning 🤖 AI 📝 Examples

**Description**: A schema unit has an invalid conversion factor due to bad formatting

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 0 pass
