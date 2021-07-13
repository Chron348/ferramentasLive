
import unittest

from ..src.services import remoteConnection

class testServiceManager(unittest.TestCase):
    def connectionTest(self):
        conn = remoteConnection.RemoteConnection()
        conn.connectToRemoteWindowsHost()
        

if __name__ =='__pytest__':
    unittest.main()