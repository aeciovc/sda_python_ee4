import pytest

from unittest.mock import MagicMock, patch
from unittest import mock

from files import FileText


class TestInstanciateFileText:

    def test_when_empty_file_path(self):

        with pytest.raises(ValueError):
            filetext = FileText('')

    def test_when_none_file_path(self):

        with pytest.raises(ValueError):
            filetext = FileText(None)

    def test_when_file_path_ok(self):

        filetext = FileText('/tmp/myfile.txt')

        assert isinstance(filetext, FileText)
        assert filetext.path == '/tmp/myfile.txt'


class TestReadFileText:

    def test_read_when_file_is_empty(self):

        filetext = FileText('/tmp/my_file.txt')

        with patch('builtins.open', new_callable=mock.mock_open, read_data=''):
            content = filetext.read()

        assert content == ''

    def test_read_when_file_not_exists(self):
        pass

    def test_read_when_file_has_content(self):
        pass


class TestWriteFileText:
    pass


class TestRemoveFileText:
    pass


class TestChecksFileText:
    pass
