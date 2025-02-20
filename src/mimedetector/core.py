from typing import Union, Optional, Dict
import pathlib
import requests
import mimetypes
from urllib.parse import urlparse


class MIMEDetector:
    """
    A class for detecting MIME types of local files and URLs.

    This class provides methods to determine the MIME type of both local
    files and remote URLs using various detection techniques.
    """

    def __init__(self, headers: Optional[Dict[str, str]] = None):
        """
        Initialize the MIMEDetector.

        Args:
            headers (Optional[Dict[str, str]]): Custom headers for HTTP requests
        """
        self.headers = headers or {}

    def check_file_location(self, path: Union[str, pathlib.Path]) -> str:
        """
        Determine if the given path is a local file or remote URL.

        Args:
            path (Union[str, pathlib.Path]): The path to check

        Returns:
            str: 'local' for local files, 'remote' for URLs, None for invalid paths
        """
        if isinstance(path, pathlib.Path):
            path = str(path)

        parsed = urlparse(path)
        if parsed.scheme and parsed.netloc:
            return "remote"
        elif pathlib.Path(path).exists():
            return "local"
        return None

    def _get_url_MIME(self, source_path: Union[str, pathlib.Path], show_debug: bool = False) -> Optional[str]:
        """
        Get the MIME type of a remote URL.

        Args:
            source_path (Union[str, pathlib.Path]): The URL to check
            show_debug (bool): If True, print debug messages

        Returns:
            Optional[str]: The MIME type or None in case of error
        """
        try:
            response = requests.head(source_path, headers=self.headers, allow_redirects=True)
            if response.status_code == 200:
                mime_type = response.headers.get('Content-Type')
                return mime_type
            else:
                if show_debug:
                    print(f"URL error: Status code {response.status_code}")
                return None
        except requests.RequestException as e:
            if show_debug:
                print(f"Request error: {str(e)}")
            return None

    def _get_file_MIME(self, source_path: Union[str, pathlib.Path]) -> Optional[str]:
        """
        Get the MIME type of a local file.

        Args:
            source_path (Union[str, pathlib.Path]): The path to the local file

        Returns:
            Optional[str]: The MIME type or None in case of error
        """
        if isinstance(source_path, pathlib.Path):
            source_path = str(source_path)
        return mimetypes.guess_type(source_path)[0]

    def get_MIME(self, source_path: Union[str, pathlib.Path]) -> Optional[str]:
        """
        Determine the MIME type of a file or URL.

        This method automatically determines if the given path is a local file
        or remote URL and uses the appropriate method to get the MIME type.

        Args:
            source_path (Union[str, pathlib.Path]): The file path or URL

        Returns:
            Optional[str]: The MIME type or None in case of error
        """
        content_location = self.check_file_location(source_path)
        if "remote" == content_location:
            return self._get_url_MIME(source_path)
        elif "local" == content_location:
            return self._get_file_MIME(source_path)
        return None
