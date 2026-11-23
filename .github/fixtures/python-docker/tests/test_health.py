import threading
import unittest
from http.server import HTTPServer
from urllib.error import HTTPError
from urllib.request import urlopen

from health_server import HealthHandler


class HealthHandlerTests(unittest.TestCase):
    def setUp(self):
        self.server = HTTPServer(("127.0.0.1", 0), HealthHandler)
        self.thread = threading.Thread(target=self.server.serve_forever)
        self.thread.start()
        self.base_url = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    def test_health_endpoint_returns_ok(self):
        with urlopen(f"{self.base_url}/health") as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.read(), b"ok")

    def test_unknown_path_returns_not_found(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(f"{self.base_url}/unknown")

        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
