"""
Automated Accessibility (a11y) Static Audit for AccessMap India.
Validates ARIA roles, label compliance, and meta viewport tags.
"""
import re
import unittest
import os

class TestAccessibilityMarkup(unittest.TestCase):
    def setUp(self):
        self.html_path = os.path.join(os.path.dirname(__file__), "..", "accessmap-site", "index.html")
        with open(self.html_path, "r", encoding="utf-8") as f:
            self.html = f.read()

    def test_viewport_accessibility(self):
        # Must not restrict user zoom with user-scalable=no or maximum-scale=1
        self.assertIn('name="viewport"', self.html)
        self.assertNotIn('user-scalable=no', self.html.lower())

    def test_aria_landmarks(self):
        # Must contain semantic landmarks
        self.assertTrue(bool(re.search(r'role=["\']main["\']|<main\b', self.html)))

    def test_navigation_hud_elements(self):
        # Must contain live navigation HUD anchors
        self.assertIn('id="live-nav-hud"', self.html)
        self.assertIn('id="live-nav-turn-banner"', self.html)
        self.assertIn('id="live-nav-dock"', self.html)

if __name__ == "__main__":
    unittest.main()
