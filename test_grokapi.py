# test_grokapi.py
"""
Tests for GrokAPI module.
"""

import unittest
from grokapi import GrokAPI

class TestGrokAPI(unittest.TestCase):
    """Test cases for GrokAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GrokAPI()
        self.assertIsInstance(instance, GrokAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GrokAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
