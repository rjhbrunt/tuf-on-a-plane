from securesystemslib.util import load_json_file

from .models.common import (
    Filepath,
    Rolename,
)
from .models.metadata import Metadata
from .parsers.json import JSONParser


class ReaderMixIn:
    """A mixin to separate TUF metadata details such as filename extension and
    file format."""

    def role_filename(self, rolename: Rolename) -> Filepath:
        """Return the expected filename based on the rolename."""
        raise NotImplementedError

    def read_from_file(self, path: Filepath) -> Metadata:
        """Read, parse, and return the Metadata from the file."""
        raise NotImplementedError


class JSONReaderMixIn(ReaderMixIn):
    """Use this mixin to handle the JSON filename extension and file format."""

    def role_filename(self, rolename: Rolename) -> Filepath:
        """Return the expected filename based on the rolename."""
        return f"{rolename}.json"

    def read_from_file(self, path: Filepath) -> Metadata:
        """Return the expected filename based on the rolename."""
        return JSONParser.parse(load_json_file(path))
