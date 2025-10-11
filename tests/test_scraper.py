"""Comprehensive tests for GPlay Scraper."""

import unittest
from unittest.mock import patch, MagicMock
from gplay_scraper import GPlayScraper
from gplay_scraper.core.aso_analyzer import AsoAnalyzer


class TestGPlayScraper(unittest.TestCase):
    """Test cases for GPlayScraper main functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.scraper = GPlayScraper()

    def test_invalid_app_id_empty(self):
        """Test that empty app_id raises ValueError."""
        with self.assertRaises(ValueError):
            self.scraper.analyze("")

    def test_invalid_app_id_none(self):
        """Test that None app_id raises ValueError."""
        with self.assertRaises(ValueError):
            self.scraper.analyze(None)

    def test_invalid_app_id_format(self):
        """Test that invalid app_id format raises ValueError."""
        with self.assertRaises(ValueError):
            self.scraper.analyze("invalid@app#id")

    @patch('gplay_scraper.core.scraper.curl_requests.get')
    def test_network_timeout(self, mock_get):
        """Test network timeout handling."""
        mock_get.side_effect = Exception("Timeout")
        
        with self.assertRaises(Exception):
            self.scraper.analyze("com.invalid.test.app")

    def test_get_field_validation(self):
        """Test get_field input validation."""
        with self.assertRaises(ValueError):
            self.scraper.get_field("", "title")

    def test_get_fields_validation(self):
        """Test get_fields input validation."""
        with self.assertRaises(ValueError):
            self.scraper.get_fields("", ["title"])


class TestAsoAnalyzer(unittest.TestCase):
    """Test cases for ASO analysis functionality."""

    def setUp(self):
        """Set up test fixtures."""
        self.analyzer = AsoAnalyzer()

    def test_tokenize_text(self):
        """Test text tokenization."""
        text = "This is a test app for gaming!"
        tokens = self.analyzer.tokenize_text(text)
        self.assertIn("test", tokens)
        self.assertNotIn("is", tokens)  # Stop word removed

    def test_extract_ngrams(self):
        """Test n-gram extraction."""
        words = ["test", "mobile", "app"]
        bigrams = self.analyzer.extract_ngrams(words, 2)
        self.assertEqual(bigrams, ["test mobile", "mobile app"])

    def test_keyword_frequency(self):
        """Test keyword frequency calculation."""
        words = ["test", "app", "test", "mobile"]
        freq = self.analyzer.keyword_frequency(words, 10)
        self.assertEqual(freq["test"], 2)
        self.assertEqual(freq["app"], 1)

    def test_competitive_keywords(self):
        """Test competitive keyword detection."""
        text = "Buy premium features and share with friends"
        keywords = self.analyzer.analyze_competitive_keywords(text)
        self.assertIn("monetization", keywords)
        self.assertIn("social", keywords)


if __name__ == '__main__':
    unittest.main(verbosity=2)
