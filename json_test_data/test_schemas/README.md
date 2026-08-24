# Test schemas

Test-only HED schema libraries used by the JSON test suite, primarily by the
schema-loading tests in
`validation_test_data/SCHEMA_LOAD_FAILED.json` and
`validation_test_data/TAG_NAMESPACE_PREFIX_INVALID.json`. These libraries are
not released through hed-schemas and must never be published to the HED
schema repositories; they exist so the suite can exercise every
schema-combination rule with fully controlled vocabularies.

## Loading convention (for validator implementers)

Test cases keep plain version strings in their `schema` fields (for example
`"8.5.0, testconflict_1.0.0"`, prefixed forms included) because the tests are
about version-string and merge-group semantics. Runners resolve those version
strings against the flat folder `json_test_data/test_schemas/hedxml/` as a
local schema directory instead of the released-schema repositories. The
folder contains every merged library version plus the vendored standard
schemas, under the standard cache-convention file names
(`HED_<library>_<version>.xml`, `HED<version>.xml`), so a whole merge group
resolves against this single directory and no network access is needed.

In hed-python this is exactly:

```python
from hed.schema import load_schema_version

schema = load_schema_version(versions, xml_folder="json_test_data/test_schemas/hedxml")
```

Validators that bundle their schemas (for example hed-javascript) implement
the same rule: resolve every version string in a test's `schema` list against
this folder by cache-convention file name.

## Layout

- `hedxml/` - flat, load-ready: all merged library XML plus the vendored
  standard schemas. This is the only folder runners need.
- `<library>/hedwiki/` - hand-edited unmerged `.mediawiki` sources, the
  source of truth for each library.
- `<library>/hedxml_unmerged/` - generated unmerged XML.
- `manifest.json` - machine-readable inventory: libraries, versions, each
  version's `withStandard` partner, and the hed-schemas commit each vendored
  standard snapshot came from.

## The libraries

- **testconflict** - the primary, semver-clean library: every
  version-to-version change follows the semantic versioning rules in the HED
  specification (section 3.1.3). Unpartnered 1.x versions and 2.x versions
  partnered with standard schema 8.5.0.
- **testclash** - the conflict companion: each version carries the constant
  `Clash-tag` scaffold plus at most one probe element shared with
  testconflict 2.x, identical except for one controlled difference
  (attribute value, description, ancestor path, placeholder child, rooted
  anchor, or a shared-hierarchy variation). One conflict per version, so
  each load test isolates a single rule.
- **testminimal** - a third library name with an unchanging vocabulary:
  unpartnered 1.0.0, 2.0.0 partnered with 8.4.0, and 2.1.0 partnered with
  8.5.0, for the mismatched-partner and multi-library cases.

Each version's prologue states its role and the semver level of its change
from the predecessor.

## Vendored standard schemas

`hedxml/HED8.5.0.xml` (prerelease snapshot) and `hedxml/HED8.4.0.xml`
(released) are vendored copies from hed-standard/hed-schemas so schema
loading is fully hermetic; their source commits are recorded in
`manifest.json`. The vendored copies stay after 8.5.0 is released.

## Regeneration

The `.mediawiki` sources are the editable source of truth. After editing
one, regenerate and commit the XML (as with `consolidate_tests.py`, CI reruns
the script but staleness of committed copies is on the committer):

```bash
python src/scripts/convert_test_schemas.py
```

To update the vendored standard snapshots from a local hed-schemas checkout
(for example when the 8.5.0 prerelease changes):

```bash
python src/scripts/convert_test_schemas.py --refresh --hed-schemas <path-to-hed-schemas>
```

The script also verifies that no library tag name exists in that library's
standard schema partner (spec SCHEMA_LIBRARY_INVALID reason i), so edits
cannot introduce a partner collision silently.
