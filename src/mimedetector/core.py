from typing import Union, Optional
import pathlib
import requests
import mimetypes
from urllib.parse import urlparse
from .i18n import en, it


class MIMEDetector:
    """
    A class for detecting MIME types of local files and URLs.

    This class provides methods to determine the MIME type of both local
    files and remote URLs using various detection techniques.

    Una classe per rilevare il tipo MIME di file locali e URL.

    Questa classe fornisce metodi per determinare il tipo MIME di file sia locali
    che remoti (URL) utilizzando varie tecniche di rilevamento.
    """

    def __init__(self, language: str = "en"):
        """
        Initialize the MIMEDetector.

        Args:
            language (str): Language for debug messages ("en" or "it")
        """
        self.language = language
        self.messages = en.DEBUG_MESSAGES if language == "en" else it.DEBUG_MESSAGES

    def check_file_location(self, path: Union[str, pathlib.Path]) -> str:
        """
        Determine if the given path is a local file or remote URL.

        Determina se il percorso fornito è un file locale o un URL remoto.

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

    def _get_url_MIME(self, SourcePath: Union[str, pathlib.Path], ShowDebug: Optional[bool] = False) -> Optional[str]:
        """
        Get the MIME type of a remote URL.

        Ottiene il tipo MIME di un URL remoto.

        Args:
            SourcePath (Union[str, pathlib.Path]): The URL to check
            ShowDebug (Optional[bool]): If True, print debug messages

        Returns:
            Optional[str]: The MIME type or None in case of error
        """
        try:
            response = requests.head(SourcePath, allow_redirects=True)
            if response.status_code == 200:
                mime_type = response.headers.get('Content-Type')
                return mime_type
            else:
                if ShowDebug:
                    print(self.messages["url_error"].format(status_code=response.status_code))
                return None
        except requests.RequestException as e:
            if ShowDebug:
                print(self.messages["request_error"].format(error=str(e)))
            return None

    def _get_file_MIME(self, SourcePath: Union[str, pathlib.Path]) -> Optional[str]:
        """
        Get the MIME type of a local file.

        Ottiene il tipo MIME di un file locale.

        Args:
            SourcePath (Union[str, pathlib.Path]): The path to the local file

        Returns:
            Optional[str]: The MIME type or None in case of error
        """
        if isinstance(SourcePath, pathlib.Path):
            SourcePath = str(SourcePath)
        return mimetypes.guess_type(SourcePath)[0]

    def get_MIME(self, SourcePath: Union[str, pathlib.Path]) -> Optional[str]:
        """
        Determine the MIME type of a file or URL.

        This method automatically determines if the given path is a local file
        or remote URL and uses the appropriate method to get the MIME type.

        Determina il tipo MIME di un file o URL.

        Questo metodo determina automaticamente se il percorso fornito è un file locale
        o un URL remoto e utilizza il metodo appropriato per ottenere il tipo MIME.

        Args:
            SourcePath (Union[str, pathlib.Path]): The file path or URL

        Returns:
            Optional[str]: The MIME type or None in case of error
        """
        ContentLocation = self.check_file_location(SourcePath)
        if "remote" == ContentLocation:
            return self._get_url_MIME(SourcePath)
        elif "local" == ContentLocation:
            return self._get_file_MIME(SourcePath)
        return None