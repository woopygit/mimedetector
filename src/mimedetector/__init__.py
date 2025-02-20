"""
MIMEDetector - A Python package for detecting MIME types of local files and URLs.

This package provides a simple interface to detect MIME types of both local files
and remote URLs using various detection techniques.
"""

from .core import MIMEDetector

__version__ = "0.2.1"
__author__ = "woopygit"
__email__ = "woopygit@icloud.com"

__all__ = ["MIMEDetector"]