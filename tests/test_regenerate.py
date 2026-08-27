"""
Unit tests for regenerate.py's staleness detection.

The detection is exercised in a throwaway git repository under a temp
directory, never against the real working tree.
"""

import subprocess
import tempfile
import unittest
from pathlib import Path

from src.scripts.regenerate import DERIVED_PATHS, find_stale


def git(repo: Path, *args: str) -> None:
    """Run a git command in the temp repository, raising on failure."""
    subprocess.run(["git", *args], cwd=repo, check=True, capture_output=True)


class TestFindStale(unittest.TestCase):
    """find_stale reports files whose content differs from the index."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.email", "test@example.com")
        git(self.repo, "config", "user.name", "Test")
        (self.repo / "docs").mkdir()
        (self.repo / "json_test_data").mkdir()
        (self.repo / "docs" / "test_coverage.md").write_text("# Coverage\n\ntotal 10\n", encoding="utf-8")
        (self.repo / "json_test_data" / "validation_tests.json").write_text("[]\n", encoding="utf-8")
        git(self.repo, "add", ".")
        git(self.repo, "commit", "-q", "-m", "initial")

    def tearDown(self):
        self.tmp.cleanup()

    def test_clean_tree_reports_nothing(self):
        self.assertEqual(find_stale(self.repo, DERIVED_PATHS), [])

    def test_modified_derived_file_is_reported(self):
        (self.repo / "docs" / "test_coverage.md").write_text("# Coverage\n\ntotal 11\n", encoding="utf-8")
        self.assertEqual(find_stale(self.repo, DERIVED_PATHS), ["docs/test_coverage.md"])

    def test_untracked_derived_file_is_reported(self):
        (self.repo / "docs" / "test_index.md").write_text("# Index\n", encoding="utf-8")
        self.assertEqual(find_stale(self.repo, DERIVED_PATHS), ["docs/test_index.md"])

    def test_change_outside_derived_paths_is_ignored(self):
        (self.repo / "docs" / "user_guide.md").write_text("# Guide\n", encoding="utf-8")
        self.assertEqual(find_stale(self.repo, DERIVED_PATHS), [])

    def test_staged_change_is_not_stale(self):
        (self.repo / "docs" / "test_coverage.md").write_text("# Coverage\n\ntotal 12\n", encoding="utf-8")
        git(self.repo, "add", "docs/test_coverage.md")
        self.assertEqual(find_stale(self.repo, DERIVED_PATHS), [])


if __name__ == "__main__":
    unittest.main()
