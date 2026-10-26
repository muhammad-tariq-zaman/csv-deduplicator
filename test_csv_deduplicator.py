import csv
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestDedupe(unittest.TestCase):
    def test_keep_first_report_removed(self):
        with tempfile.TemporaryDirectory() as d:
            inp, out = os.path.join(d, "in.csv"), os.path.join(d, "out.csv")
            with open(inp, "w", newline="") as fh:
                w = csv.writer(fh)
                w.writerow(["id", "name"])
                w.writerow(["1", "first"])
                w.writerow(["1", "duplicate"])
                w.writerow(["2", "second"])
            r = main.dedupe(inp, out, "id")
            self.assertEqual((r["kept"], r["removed"]), (2, 1))
            rows = list(csv.DictReader(open(out)))
            self.assertEqual(rows[0]["name"], "first")

    def test_missing_key_raises(self):
        with tempfile.TemporaryDirectory() as d:
            inp = os.path.join(d, "in.csv")
            open(inp, "w").write("id,name\n1,x\n")
            with self.assertRaises(ValueError):
                main.dedupe(inp, os.path.join(d, "o.csv"), "nope")


if __name__ == "__main__":
    unittest.main()
