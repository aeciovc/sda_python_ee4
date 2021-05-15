import world_time

from unittest.mock import patch, MagicMock

class TestWorldTimeConnections:

    def test_when_service_not_available(self):

        mock = MagicMock()
        mock.return_value = {'msg': '503 Unavailable'}

        with patch('requests.get', mock):

            result = world_time.get_time_by_ip('...')

            assert result == None

