import subprocess
import unittest


class CliScriptTests(unittest.TestCase):
    def test_uv_run_cli_prints_greeting(self) -> None:
        result = subprocess.run(
            ["uv", "run", "cli"],
            capture_output=True,
            text=True,
            cwd="/Users/piersonlim/hoocl",
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Hello from hoocl")


if __name__ == "__main__":
    unittest.main()