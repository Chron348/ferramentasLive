import unittest

from livetools.services.remoteConnection import RemoteConnection


class ServiceTest(unittest.TestCase):

    def test_connect_to_remote_windows_machine(self):
        conn = RemoteConnection()
        print(conn.list_folder_server_live_remote_windows_host())
        self.assertEqual(0, 0)

if __name__ == '__pytest__':
    unittest.main()
