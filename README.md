# MIMEDetector

A Python package for detecting MIME types of local files and URLs. This package provides a simple and efficient way to determine the MIME type of both local files and remote URLs using various detection techniques.

## Features

- Detect MIME types of local files
- Detect MIME types of remote URLs
- Support for custom HTTP headers
- Simple and intuitive API
- Type hints for better development experience
- Python 3.7+ support

## Installation

You can install MIMEDetector using pip:

```bash
pip install mimedetector
```

## Quick Start

```python
from mimedetector import MIMEDetector

# Initialize the detector
detector = MIMEDetector()

# Check a local file
mime_type = detector.get_MIME("path/to/your/file.pdf")
print(f"Local file MIME type: {mime_type}")

# Check a remote URL
mime_type = detector.get_MIME("https://example.com/file.jpg")
print(f"Remote file MIME type: {mime_type}")

# Using custom headers for HTTP requests
headers = {
    "User-Agent": "Custom User Agent",
    "Accept": "*/*"
}
detector = MIMEDetector(headers=headers)
mime_type = detector.get_MIME("https://example.com/file.jpg")
```

## API Reference

### MIMEDetector

#### `__init__(headers: Optional[Dict[str, str]] = None)`

Initialize a new MIMEDetector instance.

- `headers`: Optional dictionary of HTTP headers to use for remote requests

#### `get_MIME(source_path: Union[str, pathlib.Path]) -> Optional[str]`

Get the MIME type of a file or URL.

- `source_path`: Path to local file or URL
- Returns: MIME type string or None if unable to determine

#### `check_file_location(path: Union[str, pathlib.Path]) -> str`

Determine if the given path is a local file or remote URL.

- `path`: Path to check
- Returns: 'local' for local files, 'remote' for URLs, None for invalid paths

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **woopygit** - [GitHub](https://github.com/woopygit)
- Email: woopygit@icloud.com

## Version History

- 0.2.1
  - Added support for custom HTTP headers
  - Improved error handling
  - Updated documentation

## Acknowledgments

- Thanks to all contributors who have helped shape this project
- Built with Python's excellent `mimetypes` and `requests` libraries