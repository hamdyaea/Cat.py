# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import io
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
import cat

class CatTests(unittest.TestCase):
    def test_binary_files(self):
        with TemporaryDirectory() as folder:
            first = Path(folder) / "first"
            second = Path(folder) / "second"
            first.write_bytes(b"abc\x00")
            second.write_bytes(b"\xff\n")
            out = io.BytesIO()
            self.assertEqual(cat.cat([str(first), str(second)], output=out), 0)
            self.assertEqual(out.getvalue(), b"abc\x00\xff\n")
    def test_stdin(self):
        out = io.BytesIO()
        self.assertEqual(cat.cat(["-"], output=out, input_stream=io.BytesIO(b"hello")), 0)
        self.assertEqual(out.getvalue(), b"hello")
    def test_missing_file_continues(self):
        with TemporaryDirectory() as folder:
            good = Path(folder) / "good"
            good.write_bytes(b"ok")
            out = io.BytesIO()
            self.assertEqual(cat.cat([str(good)+"missing", str(good)], output=out), 1)
            self.assertEqual(out.getvalue(), b"ok")

if __name__ == "__main__":
    unittest.main()
