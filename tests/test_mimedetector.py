import unittest
from pathlib import Path
from mimedetector import MIMEDetector

class TestMIMEDetector(unittest.TestCase):
    def setUp(self):
        self.detector = MIMEDetector()

    def test_check_file_location_url(self):
        path = "https://example.com/file.pdf"
        self.assertEqual(self.detector.check_file_location(path), "remote")

    def test_get_mime_invalid_path(self):
        path = "nonexistent/file.pdf"
        self.assertIsNone(self.detector.get_MIME(path))

if __name__ == '__main__':
    unittest.main()