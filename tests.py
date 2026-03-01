import logic_kit
import unittest

class LogicKitTest(unittest.TestCase):
  def test_fmt(self):
    self.assertEqual(logic_kit.format_logic("ab"), "a & b")

if __name__ == "__main__":
  unittest.main()