# HED test suite index

Complete index of 137 test cases in the HED test suite.

## Quick navigation

- [CHARACTER_INVALID](#character-invalid) (4 tests)
- [COMMA_MISSING](#comma-missing) (2 tests)
- [DEFINITION_INVALID](#definition-invalid) (10 tests)
- [DEF_EXPAND_INVALID](#def-expand-invalid) (6 tests)
- [DEF_INVALID](#def-invalid) (3 tests)
- [ELEMENT_DEPRECATED](#element-deprecated) (1 test)
- [PARENTHESES_MISMATCH](#parentheses-mismatch) (2 tests)
- [PLACEHOLDER_INVALID](#placeholder-invalid) (4 tests)
- [SCHEMA_ATTRIBUTE_INVALID](#schema-attribute-invalid) (1 test)
- [SCHEMA_ATTRIBUTE_VALUE_INVALID](#schema-attribute-value-invalid) (12 tests)
- [SCHEMA_CHARACTER_INVALID](#schema-character-invalid) (6 tests)
- [SCHEMA_DEPRECATION_ERROR](#schema-deprecation-error) (8 tests)
- [SCHEMA_DUPLICATE_NODE](#schema-duplicate-node) (2 tests)
- [SCHEMA_HEADER_INVALID](#schema-header-invalid) (2 tests)
- [SCHEMA_LIBRARY_INVALID](#schema-library-invalid) (8 tests)
- [SCHEMA_LOAD_FAILED](#schema-load-failed) (3 tests)
- [SCHEMA_MISSING_EXTRA_VALUE](#schema-missing-extra-value) (1 test)
- [SCHEMA_SECTION_MISSING](#schema-section-missing) (1 test)
- [SIDECAR_BRACES_INVALID](#sidecar-braces-invalid) (5 tests)
- [SIDECAR_INVALID](#sidecar-invalid) (2 tests)
- [SIDECAR_KEY_MISSING](#sidecar-key-missing) (2 tests)
- [TAG_EMPTY](#tag-empty) (3 tests)
- [TAG_EXPRESSION_REPEATED](#tag-expression-repeated) (3 tests)
- [TAG_EXTENDED](#tag-extended) (1 test)
- [TAG_EXTENSION_INVALID](#tag-extension-invalid) (2 tests)
- [TAG_GROUP_ERROR](#tag-group-error) (4 tests)
- [TAG_INVALID](#tag-invalid) (3 tests)
- [TAG_NAMESPACE_PREFIX_INVALID](#tag-namespace-prefix-invalid) (3 tests)
- [TAG_NOT_UNIQUE](#tag-not-unique) (1 test)
- [TAG_REQUIRES_CHILD](#tag-requires-child) (1 test)
- [TEMPORAL_TAG_ERROR](#temporal-tag-error) (24 tests)
- [UNITS_INVALID](#units-invalid) (2 tests)
- [VALUE_INVALID](#value-invalid) (4 tests)
- [WIKI_DELIMITERS_INVALID](#wiki-delimiters-invalid) (1 test)

## CHARACTER_INVALID

**File**: `json_test_data/validation_test_data/CHARACTER_INVALID.json`

### character-invalid-non-printing-appears (AI metadata) (examples)

**Description**: The HED string contains a UTF-8 character.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### curly-braces-not-in-sidecar (AI metadata) (examples)

**Description**: The curly brace notation is used outside a sidecar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 1 fail, 1 pass

### invalid-character-name-value-class (AI metadata) (examples)

**Description**: An invalid character was used in an 8.3.0 or greater style name value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 5 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 3 fail, 1 pass
- `combo_tests`: 1 fail, 0 pass

### invalid-character-name-value-class-early-schema (AI metadata) (examples)

**Description**: An invalid character was as a value in a placeholder or as a tag extension.

**Schema**: 8.2.0 **Category**: validation

**Tests**:

- `string_tests`: 4 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 3 fail, 1 pass

## COMMA_MISSING

**File**: `json_test_data/validation_test_data/COMMA_MISSING.json`

### comma-missing-tag-and-group (AI metadata) (examples)

**Description**: A tag and a tag group are not separated by commas: A(B,D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### comma-missing-tag-groups (AI metadata) (examples)

**Description**: Two tag groups are not separated by commas: (A, B)(C, D).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEFINITION_INVALID

**File**: `json_test_data/validation_test_data/DEFINITION_INVALID.json`

### definition-invalid-bad-number-of-placeholders (AI metadata) (examples)

**Description**: A definition that includes a placeholder (`#`) does not have exactly two `#` characters.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-content-has-top-level-tag (AI metadata) (examples)

**Description**: A tag with a required or unique attribute appears in a definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-empty-inner-group (AI metadata) (examples)

**Description**: A definition's enclosing tag group has an empty inner group (i.e., the definition's contents).

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-inner-group-defs (AI metadata) (examples)

**Description**: A definition's inner tag group contains `Definition`, `Def` or `Def-expand` tags.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 0 pass
- `event_tests`: 0 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-multiple-definition-tags (AI metadata) (examples)

**Description**: A definition's enclosing tag group contains more than a `Definition` tag and an inner group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-multiple-definitions (AI metadata) (examples)

**Description**: Multiple `Definition` tags with same name are encountered.

**Schema**: 8.4.0 **Category**: uniqueness

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-placeholder-conflict (AI metadata) (examples)

**Description**: Definitions of the same name appear with and without a `#`.

**Schema**: 8.4.0 **Category**: consistency

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-placeholder-incorrect-of-positions (AI metadata) (examples)

**Description**: A definition has placeholders (`#`) in incorrect positions.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-invalid-tag-group (AI metadata) (examples)

**Description**: A Definition tag does not appear in a tag group at the top level in an annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 0 pass
- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### definition-not-allowed-here (AI metadata) (examples)

**Description**: A definition appears in an unexpected place such as an events file or sidecar.

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEF_EXPAND_INVALID

**File**: `json_test_data/validation_test_data/DEF_EXPAND_INVALID.json`

### def-expand-has-extras (AI metadata) (examples)

**Description**: A Def-expand has extra tags or groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-bad-placeholder-value-or-units (AI metadata) (examples)

**Description**: A `Def-expand` has an incorrect type of placeholder value.

**Schema**: 8.4.0 **Category**: value

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-missing-placeholder (AI metadata) (examples)

**Description**: A `Def-expand` is missing an expected placeholder value or has an unexpected placeholder value.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-name-not-definition (AI metadata) (examples)

**Description**: A `Def-expand` tag's name does not correspond to a definition.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-invalid-tags-not-in-definition (AI metadata) (examples)

**Description**: The tags within a Def-expand do not match the corresponding definition.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-expand-missing-inner-group (AI metadata) (examples)

**Description**: A Def-expand is missing its inner group containing the definition.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## DEF_INVALID

**File**: `json_test_data/validation_test_data/DEF_INVALID.json`

### def-invalid-bad-placeholder-value (AI metadata) (examples)

**Description**: A `Def` has a placeholder value of incorrect format or units for definition.

**Schema**: 8.4.0 **Category**: value

**Tests**:

- `string_tests`: 4 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-invalid-missing-placeholder (AI metadata) (examples)

**Description**: A `Def` tag is missing an expected placeholder value or has an unexpected placeholder value.

**Schema**: 8.4.0 **Category**: placeholder

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### def-invalid-name (AI metadata) (examples)

**Description**: A `Def` tag's name does not correspond to a definition.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## ELEMENT_DEPRECATED

**File**: `json_test_data/validation_test_data/ELEMENT_DEPRECATED.json`

### tag-deprecated (warning) (AI metadata) (examples)

**Description**: A tag is deprecated

**Schema**: 8.2.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PARENTHESES_MISMATCH

**File**: `json_test_data/validation_test_data/PARENTHESES_MISMATCH.json`

### parentheses-mismatch-incorrect-nesting (AI metadata) (examples)

**Description**: The open and closed parentheses are not correctly nested in the HED string.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### parentheses-mismatch-unmatched-parentheses (AI metadata) (examples)

**Description**: A HED string does not have the same number of open and closed parentheses.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## PLACEHOLDER_INVALID

**File**: `json_test_data/validation_test_data/PLACEHOLDER_INVALID.json`

### placeholder-invalid-#-in-categorical-column (AI metadata) (examples)

**Description**: A JSON sidecar has a placeholder (`#`) in the HED dictionary for a categorical column.

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-#-misplaced (AI metadata) (examples)

**Description**: A placeholder (`#`) is used in JSON sidecar or definition, but its parent in the schema does not have a placeholder child.

**Schema**: 8.4.0 **Category**: schema

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-json-value-column (AI metadata) (examples)

**Description**: A JSON sidecar does not have exactly one placeholder (`#`) in each HED string representing a value column.

**Schema**: 8.4.0 **Category**: count

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### placeholder-invalid-misplaced (AI metadata) (examples)

**Description**: A `#` appears in a place that it should not (such as in the `HED` column of an event file outside a definition).

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 0 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## SCHEMA_ATTRIBUTE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_INVALID.json`

### attribute-invalid-unknown (warning) (AI metadata) (examples)

**Description**: A schema attribute issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

## SCHEMA_ATTRIBUTE_VALUE_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-factor-invalid (warning) (AI metadata) (examples)

**Description**: A schema unit has an invalid conversion factor

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 4 fail, 1 pass

### attribute-default-unit-invalid (warning) (AI metadata) (examples)

**Description**: A schema unit class has an invalid default value

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-allowed-character (warning) (AI metadata) (examples)

**Description**: A schema value class has an invalid allowedCharacter attribute value

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### attribute-invalid-hed-id-changed (warning) (AI metadata) (examples)

**Description**: A schema element has a hedId that changed from its previously assigned value.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-hed-id-invalid (warning) (AI metadata) (examples)

**Description**: A schema element has a hedId with an invalid format (non-numeric or malformed).

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-hed-id-out-range (warning) (AI metadata) (examples)

**Description**: A schema element has a hedId that is outside the valid allocated range for its section.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-in-library (warning) (AI metadata) (examples)

**Description**: A schema element has an invalid inLibrary attribute (most other library errors are SCHEMA_LIBRARY_INVALID)

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-unit-class (warning) (AI metadata) (examples)

**Description**: A schema unit class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-invalid-value-class (warning) (AI metadata) (examples)

**Description**: A schema value class issue, saying there is an unknown one.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### attribute-on-nonplaceholder-invalid (warning) (AI metadata) (examples)

**Description**: A non placeholder tag has takes value, unit class, or value class

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

### attribute-relatedTag-invalid (warning) (AI metadata) (examples)

**Description**: A related tag points to an unknown tag

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 2 pass

### attribute-suggestedTag-invalid (warning) (AI metadata) (examples)

**Description**: A suggested tag points to an unknown tag

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 2 pass

## SCHEMA_CHARACTER_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_CHARACTER_INVALID.json`

### schema-character-allowed-character-unit (warning)

**Description**: Allowed character properly works on units.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### schema-character-invalid-description (warning)

**Description**: Description does not contain banned characters.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-other-term (warning)

**Description**: Invalid character in a non-tag schema element name (unit, unit class, modifier, value class, attribute, or property).

**Schema**: any

**Tests**:

- `schema_tests`: 6 fail, 1 pass

### schema-character-invalid-prologue (warning) (AI metadata) (examples)

**Description**: Invalid character in prologue or epilogue.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-tag (warning)

**Description**: Invalid character in a tag term.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-character-invalid-utf8-other-term (warning)

**Description**: UTF8 characters (valid) in term.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

## SCHEMA_DEPRECATION_ERROR

**File**: `json_test_data/schema_test_data/SCHEMA_DEPRECATION_ERROR.json`

### schema-deprecated-attribute-invalid (warning) (AI metadata) (examples)

**Description**: A schema attribute issue, saying there is an unhandled deprecated attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-deprecated-default-unit (warning)

**Description**: A schema deprecation issue, deprecated default units

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 2 pass

### schema-deprecated-deprecated-attribute (warning)

**Description**: A schema deprecation issue, an attribute of an element is deprecated

**Schema**: any

**Tests**:

- `schema_tests`: 5 fail, 5 pass

### schema-deprecated-deprecated-property (warning)

**Description**: A schema deprecation issue, a property of an attribute is is deprecated

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-deprecated-invalid-child (warning)

**Description**: A schema deprecation issue, saying there is an invalid child of a deprecated node

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### schema-deprecated-invalid-suggested-related-tag (warning)

**Description**: A schema deprecation issue, saying a related or suggested tag points to a deprecated tag

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 4 pass

### schema-deprecated-unit-class (warning)

**Description**: A schema deprecation issue, deprecated value or unit class

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-deprecated-value-class (warning)

**Description**: A schema deprecation issue, deprecated value or unit class

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_DUPLICATE_NODE

**File**: `json_test_data/schema_test_data/SCHEMA_DUPLICATE_NODE.json`

### attribute-duplicate-node (warning) (AI metadata) (examples)

**Description**: A schema attribute issue, saying there is a duplicate node.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 6 fail, 1 pass

### attribute-duplicate-node-unit (warning)

**Description**: A schema has duplicate unit entries with case-insensitive name collision.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_HEADER_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_HEADER_INVALID.json`

### schema-header-malformed-attribute (warning) (AI metadata) (examples)

**Description**: A schema header contains a malformed or unknown attribute.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### schema-header-unknown-attribute (warning)

**Description**: An unknown attribute was found in the schema header.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

## SCHEMA_LIBRARY_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_LIBRARY_INVALID.json`

### library-invalid-bad-name (warning) (AI metadata) (examples)

**Description**: A schema library issue, indicating the name is invalid.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

### library-invalid-bad_with-standard (warning)

**Description**: A schema library issue, the with-standard attribute is present without the library attribute.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-bad_with-standard-version (warning)

**Description**: A schema library issue, indicating it references a version of the standard that can't be found.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-rooted-in-duplicate-other (warning)

**Description**: A library schema defines elements that duplicate entries already in the base standard schema.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-in-library-present (warning)

**Description**: A schema library issue, indicating the InLibrary attribute appears when it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-not-in-base (warning)

**Description**: A schema library issue, rooted tag does not exist.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

### library-invalid-rooted-not-top-level (warning)

**Description**: A schema library issue, indicating a node is being rooted that is not a top level node.

**Schema**: any

**Tests**:

- `schema_tests`: 1 fail, 1 pass

### library-invalid-rooted-present (warning)

**Description**: A schema library issue, indicating the rooted property appears in a file it shouldn't.

**Schema**: any

**Tests**:

- `schema_tests`: 2 fail, 1 pass

## SCHEMA_LOAD_FAILED

**File**: `json_test_data/validation_test_data/SCHEMA_LOAD_FAILED.json`

### different-standard-schemas-in-same-merge-group (AI metadata) (examples)

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

## SCHEMA_MISSING_EXTRA_VALUE

**File**: `json_test_data/schema_test_data/SCHEMA_MISSING_EXTRA_VALUE.json`

### schema-missing-extra-value (warning) (AI metadata) (examples)

**Description**: An extras section (Sources, Prefixes, or ExternalAnnotations) has an empty value in a required column.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 3 fail, 1 pass

## SCHEMA_SECTION_MISSING

**File**: `json_test_data/schema_test_data/SCHEMA_SECTION_MISSING.json`

### schema-section-missing (warning) (AI metadata) (examples)

**Description**: A required schema section is missing from the schema file.

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 9 fail, 1 pass

## SIDECAR_BRACES_INVALID

**File**: `json_test_data/validation_test_data/SIDECAR_BRACES_INVALID.json`

### sidecar-braces-appear-as-value-rather-than-tag (AI metadata) (examples)

**Description**: The curly braces are in a value rather than as a separate tag substitute.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### sidecar-braces-circular-reference (AI metadata) (examples)

**Description**: The item in curly braces has a HED annotation that contains curly braces.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 2 fail, 2 pass
- `combo_tests`: 0 fail, 1 pass

### sidecar-braces-contents-invalid (AI metadata) (examples)

**Description**: The item in curly braces is not the word HED or a column name with HED annotations in the sidecar.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 2 pass
- `combo_tests`: 0 fail, 1 pass

### sidecar-braces-invalid-spot (AI metadata) (examples)

**Description**: A curly brace reference must only appear where a tag could.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass

### sidecar-braces-self-reference (AI metadata) (examples)

**Description**: The item in curly braces has a HED annotation that contains itself.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 1 fail, 3 pass
- `combo_tests`: 1 fail, 2 pass

## SIDECAR_INVALID

**File**: `json_test_data/validation_test_data/SIDECAR_INVALID.json`

### sidecar-invalid-key-at-wrong-level (AI metadata) (examples)

**Description**: The HED key is not a second-level dictionary key.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### sidecar-invalid-na-annotated (AI metadata) (examples)

**Description**: An annotation entry is provided for `n/a`.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## SIDECAR_KEY_MISSING

**File**: `json_test_data/validation_test_data/SIDECAR_KEY_MISSING.json`

### sidecar-key-missing (warning) (AI metadata) (examples)

**Description**: A value in a categorical column does not have an expected entry in a sidecar.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `combo_tests`: 1 fail, 1 pass

### sidecar-refers-to-missing-tsv-hed-column (warning) (AI metadata) (examples)

**Description**: (Warning) A sidecar uses a \{HED} column which does not appear in the corresponding tsv file.

**Schema**: 8.4.0 **Category**: reference

**Tests**:

- `sidecar_tests`: 0 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EMPTY

**File**: `json_test_data/validation_test_data/TAG_EMPTY.json`

### tag-empty-begin-end-comma (AI metadata) (examples)

**Description**: A HED string begins or ends with a comma (ignoring white space).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-empty-empty-parentheses (AI metadata) (examples)

**Description**: A tag group is empty (i.e., empty parentheses are not allowed).

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-empty-extra-commas-or-parentheses (AI metadata) (examples)

**Description**: A HED string has extra commas or parentheses separated by only white space.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 5 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXPRESSION_REPEATED

**File**: `json_test_data/validation_test_data/TAG_EXPRESSION_REPEATED.json`

### tag-expression-repeated-same-level (AI metadata) (examples)

**Description**: A tag is repeated in the same tag group or level.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tags-duplicated-across-multiple-rows (AI metadata) (examples)

**Description**: Tags are repeated because two rows have the same onset value.

**Schema**: 8.4.0 **Category**: duplication

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tags-with-duplicated-onsets-across-multiple-rows (AI metadata) (examples)

**Description**: Tags are repeated because two rows have the same onset value.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENDED

**File**: `json_test_data/validation_test_data/TAG_EXTENDED.json`

### tag-extended-extension (warning) (AI metadata) (examples)

**Description**: A tag represents an extension from the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 7 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_EXTENSION_INVALID

**File**: `json_test_data/validation_test_data/TAG_EXTENSION_INVALID.json`

### tag-extension-invalid-bad-node-name (AI metadata) (examples)

**Description**: A tag extension term does not comply with rules for schema nodes.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 3 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-extension-invalid-duplicate (AI metadata) (examples)

**Description**: A tag extension term is already in the schema.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_GROUP_ERROR

**File**: `json_test_data/validation_test_data/TAG_GROUP_ERROR.json`

### multiple-top-level-tags-in-same-group (AI metadata) (examples)

**Description**: Multiple tags with the topLevelTagGroup attribute appear in the same top-level tag group. (Delay and Duration are allowed to be in the same topLevelTagGroup).

**Schema**: 8.4.0 **Category**: cardinality

**Tests**:

- `string_tests`: 4 fail, 2 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-deferred-in-splice (AI metadata) (examples)

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-missing (AI metadata) (examples)

**Description**: A tag has tagGroup or topLevelTagGroup attribute, but is not enclosed in parentheses.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 5 fail, 4 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-group-error-not-top-level (AI metadata) (examples)

**Description**: A tag with the topLevelTagGroup does not appear at a HED tag group at the top level in an assembled HED annotation.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_INVALID

**File**: `json_test_data/validation_test_data/TAG_INVALID.json`

### tag-has-extra-whitespace (AI metadata) (examples)

**Description**: A HED tag has extra internal whitespace, including directly before or after slashes.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 4 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-has-leading-trailing-or-consecutive-slashes (AI metadata) (examples)

**Description**: A HED tag has leading, trailing or consecutive slashes.

**Schema**: 8.4.0 **Category**: syntax

**Tests**:

- `string_tests`: 8 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-invalid-in-schema (AI metadata) (examples)

**Description**: The tag is not valid in the schema it is associated with.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_NAMESPACE_PREFIX_INVALID

**File**: `json_test_data/validation_test_data/TAG_NAMESPACE_PREFIX_INVALID.json`

### tag-namespace_prefix-invalid-characters (AI metadata) (examples)

**Description**: A tag prefix has invalid characters.

**Schema**: 8.3.0, sc:score_1.0.0 **Category**: syntax

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### tag-namespace_prefix-with-colon-values (AI metadata) (examples)

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

### tag-not-unique (AI metadata) (examples)

**Description**: A tag with unique attribute appears more than once in an event-level HED string.

**Schema**: 8.4.0 **Category**: semantic

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TAG_REQUIRES_CHILD

**File**: `json_test_data/validation_test_data/TAG_REQUIRES_CHILD.json`

### tag-requires-child-missing (AI metadata) (examples)

**Description**: A tag has the requireChild schema attribute but does not have a child.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## TEMPORAL_TAG_ERROR

**File**: `json_test_data/validation_test_data/TEMPORAL_TAG_ERROR.json`

### na-in-onset column (AI metadata) (examples)

**Description**: n/a is in the onset column.

**Schema**: 8.4.0 **Category**: data_format

**Tests**:

- `combo_tests`: 2 fail, 2 pass

### temporal-tag-error-duplicated-onset-or-offset (AI metadata) (examples)

**Description**: An Onset or an Offset with a given Def or Def-expand anchor appears in the same event marker with another Onset or Offset that uses the same anchor.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-duplicated-onset-or-offset-delay (AI metadata) (examples)

**Description**: An Onset or an Offset with a given Def or Def-expand anchor appears in the same event marker with another Onset or Offset that uses the same anchor.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-duration-group (AI metadata) (examples)

**Description**: A Duration or Delay has extra tags or groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 3 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 0 fail, 1 pass

### temporal-tag-error-extra tags (AI metadata) (examples)

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-extra tags-delay (AI metadata) (examples)

**Description**: An Onset tag group with has tags besides the anchor Def or Def-expand that are not in a tag group.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras (AI metadata) (examples)

**Description**: An Inset group has tags or groups in addition to its defining Def or Def-expand.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-group-has-extras-delay (AI metadata) (examples)

**Description**: An Inset group has tags or groups in addition to its defining Def or Def-expand.

**Schema**: 8.3.0 **Category**: temporal

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-outside-its-event (AI metadata) (examples)

**Description**: An Inset tag is not grouped with a Def or Def-expand of an ongoing Onset.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-inset-outside-its-event-delay (AI metadata) (examples)

**Description**: An Inset tag is not grouped with a Def or Def-expand of an ongoing Onset.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-mismatch-delay (AI metadata) (examples)

**Description**: An Offset tag associated with a given definition appears after a previous Offset tag without the appearance of an intervening Onset of the same name.

**Schema**: 8.3.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group (AI metadata) (examples)

**Description**: An Onset or Offset tag appears in a nested tag group (not a top-level tag group).

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-nested-group-delay (AI metadata) (examples)

**Description**: A delay appears in a group not in the top level.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group (AI metadata) (examples)

**Description**: An Onset or Offset tag does not appear in a tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 0 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-not-tag-group-delay (AI metadata) (examples)

**Description**: A Delay is not in the tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 3 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-offset-has-groups (AI metadata) (examples)

**Description**: An Offset appears with one or more tags or additional tag groups.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-offset-has-groups-delay (AI metadata) (examples)

**Description**: An Offset appears with one or more tags or additional tag groups.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-offset-with-no-onset (AI metadata) (examples)

**Description**: An Offset tag associated with a given definition appears after a previous Offset tag without the appearance of an intervening Onset of the same name.

**Schema**: 8.4.0 **Category**: temporal_logic

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups (AI metadata) (examples)

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: structure

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-onset-has-more-groups-delay (AI metadata) (examples)

**Description**: An Onset group has more than one additional tag group.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 2 fail, 2 pass
- `sidecar_tests`: 2 fail, 1 pass
- `event_tests`: 2 fail, 1 pass
- `combo_tests`: 3 fail, 1 pass

### temporal-tag-error-tag-appears-where-not-allowed (AI metadata) (examples)

**Description**: A temporal tag appears appears in a tsv with no onset column

**Schema**: 8.4.0 **Category**: context

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-tag-appears-where-not-allowed-delay (AI metadata) (examples)

**Description**: An Inset, Offset, or Onset tag appears in a tsv with no onset column

**Schema**: 8.3.0 **Category**: context

**Tests**:

- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 2 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs (AI metadata) (examples)

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: content

**Tests**:

- `string_tests`: 1 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### temporal-tag-error-wrong-number-of-defs-delay (AI metadata) (examples)

**Description**: An Onset or Offset tag is not grouped with exactly one Def-expand tag group or a Def tag.

**Schema**: 8.4.0 **Category**: temporal

**Tests**:

- `string_tests`: 1 fail, 2 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## UNITS_INVALID

**File**: `json_test_data/validation_test_data/UNITS_INVALID.json`

### units-invalid-for-unit-class (AI metadata) (examples)

**Description**: A tag has a value with units that are invalid or not of the correct unit class for the tag.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### units-invalid-si-units (AI metadata) (examples)

**Description**: A unit modifier is applied to units that are not SI units.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 2 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## VALUE_INVALID

**File**: `json_test_data/validation_test_data/VALUE_INVALID.json`

### invalid-character-numeric-class (AI metadata) (examples)

**Description**: An invalid character was used in an 8.3.0 or greater style numeric value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 8 fail, 10 pass
- `sidecar_tests`: 1 fail, 1 pass

### value-invalid-#-substitution (AI metadata) (examples)

**Description**: The value substituted for a placeholder (`#`) is not valid.

**Schema**: 8.3.0 **Category**: validation

**Tests**:

- `sidecar_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### value-invalid-blank-missing-before-units (AI metadata) (examples)

**Description**: The units are not separated from the value by a single blank.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

### value-invalid-incompatible-value-class (AI metadata) (examples)

**Description**: A tag placeholder value is incompatible with the specified value class.

**Schema**: 8.4.0 **Category**: validation

**Tests**:

- `string_tests`: 1 fail, 1 pass
- `sidecar_tests`: 1 fail, 1 pass
- `event_tests`: 1 fail, 1 pass
- `combo_tests`: 1 fail, 1 pass

## WIKI_DELIMITERS_INVALID

**File**: `json_test_data/schema_test_data/SCHEMA_ATTRIBUTE_VALUE_INVALID_CONVERSION_FACTOR.json`

### attribute-conversion-format (warning) (AI metadata) (examples)

**Description**: A schema unit has an invalid conversion factor due to bad formatting

**Schema**: any **Category**: schema_development

**Tests**:

- `schema_tests`: 1 fail, 0 pass
