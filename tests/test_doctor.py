import unittest
from unittest.mock import patch
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

import doctor

class TestDoctor(unittest.TestCase):
    def test_check_optional_tools_when_wt_missing(self):
        with patch("shutil.which", return_value=None):
            optional = doctor.check_optional_tools()
            self.assertIn("worktrunk (wt)", optional)
            self.assertFalse(optional["worktrunk (wt)"]["installed"])
            self.assertIsNone(optional["worktrunk (wt)"]["path"])
            self.assertIn("brew install", optional["worktrunk (wt)"]["install_hint"])

    def test_check_optional_tools_when_wt_present(self):
        with patch("shutil.which", return_value="/usr/local/bin/wt"):
            optional = doctor.check_optional_tools()
            self.assertIn("worktrunk (wt)", optional)
            self.assertTrue(optional["worktrunk (wt)"]["installed"])
            self.assertEqual(optional["worktrunk (wt)"]["path"], "/usr/local/bin/wt")

if __name__ == "__main__":
    unittest.main()
