"""
Unit test for Python HTTP server configuration and static directory discovery.
"""
import unittest
import os
import sys

class TestServerConfiguration(unittest.TestCase):
    def setUp(self):
        self.root_dir = os.path.dirname(os.path.dirname(__file__))

    def test_site_directory_exists(self):
        site_dir = os.path.join(self.root_dir, "accessmap-site")
        self.assertTrue(os.path.isdir(site_dir), "accessmap-site folder must exist")

    def test_index_file_exists(self):
        index_file = os.path.join(self.root_dir, "accessmap-site", "index.html")
        self.assertTrue(os.path.isfile(index_file), "index.html must exist in accessmap-site")

    def test_styles_file_exists(self):
        css_file = os.path.join(self.root_dir, "accessmap-site", "styles.css")
        self.assertTrue(os.path.isfile(css_file), "styles.css must exist in accessmap-site")

    def test_app_js_file_exists(self):
        js_file = os.path.join(self.root_dir, "accessmap-site", "app.js")
        self.assertTrue(os.path.isfile(js_file), "app.js must exist in accessmap-site")

if __name__ == "__main__":
    unittest.main()
