import unittest
from test import ROOT_TEST_DIR
from util.io_util import IOUtil


class IOUtilTest(unittest.TestCase):

    def test_read_index_vector_json(self):
        print(ROOT_TEST_DIR)
        a, b, c = IOUtil.read_index_vector_json(ROOT_TEST_DIR + '/resources/index_vectors.json')
        self.assertEqual(a, 2)
        self.assertEqual('a', b[0])
        self.assertEqual(6, len(b))
        self.assertEqual([0.1, 0.1], c[0])
