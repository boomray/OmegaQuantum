# test_omegaquantum.py
"""
Tests for OmegaQuantum module.
"""

import unittest
from omegaquantum import OmegaQuantum

class TestOmegaQuantum(unittest.TestCase):
    """Test cases for OmegaQuantum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OmegaQuantum()
        self.assertIsInstance(instance, OmegaQuantum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OmegaQuantum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
