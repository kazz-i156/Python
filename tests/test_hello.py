import os
import sys
import unittest

# テスト実行時にプロジェクトのルートをインポートパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hello import sum_1_to_100


class TestHelloSum(unittest.TestCase):
    def test_sum_1_to_100(self):
        self.assertEqual(sum_1_to_100(), 5050)


if __name__ == "__main__":
    unittest.main()
