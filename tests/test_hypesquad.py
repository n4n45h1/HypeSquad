import unittest
from unittest.mock import Mock, patch

import requests

import hypesquad


class HouseRequestTests(unittest.TestCase):
    @patch("hypesquad.requests.request")
    def test_join_sends_expected_method_payload_and_timeout(self, request):
        request.return_value = Mock(ok=True)
        ok, message = hypesquad.request_house("fake-token", "balance")
        self.assertTrue(ok)
        self.assertIn("Balance", message)
        request.assert_called_once_with(
            "POST", hypesquad.API_URL, headers={"Authorization": "fake-token"},
            json={"house_id": 3}, timeout=(5, 15)
        )

    @patch("hypesquad.requests.request")
    def test_leave_uses_delete_without_payload(self, request):
        request.return_value = Mock(ok=True)
        self.assertTrue(hypesquad.request_house("fake-token", "leave")[0])
        self.assertEqual(request.call_args.kwargs["json"], None)
        self.assertEqual(request.call_args.args[0], "DELETE")

    @patch("hypesquad.requests.request")
    def test_error_body_is_not_echoed(self, request):
        request.return_value = Mock(ok=False, status_code=400, text="secret fake-token")
        ok, message = hypesquad.request_house("fake-token", "bravery")
        self.assertFalse(ok)
        self.assertIn("400", message)
        self.assertNotIn("fake-token", message)

    @patch("hypesquad.requests.request", side_effect=requests.Timeout)
    def test_timeout_does_not_retry(self, request):
        self.assertFalse(hypesquad.request_house("fake-token", "bravery")[0])
        request.assert_called_once()

    @patch.dict("hypesquad.os.environ", {"DISCORD_TOKEN": " env-token "})
    def test_environment_token(self):
        self.assertEqual(hypesquad.read_token(None), "env-token")


if __name__ == "__main__":
    unittest.main()
