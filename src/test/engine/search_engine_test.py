"""Test Class For Search Engine"""

import unittest
from test import ROOT_TEST_DIR
from util.io_util import IOUtil
from engine.search_engine import SearchEngine, SearchEngineSingleton


class SearchEngineTest(unittest.TestCase):
    def setUp(self):
        self.vec_dim, self.index2label, self.vec_list = IOUtil.read_index_vector_json(
            ROOT_TEST_DIR + '/resources/index_vectors.json')

    def search_engine_constructor_test(self):
        search_engine = SearchEngine(vector_dim=self.vec_dim, index_vectors=self.vec_list)
        self.assertEqual(2, search_engine.vec_dim)
        self.assertEqual(0, search_engine.shadow_index_size())
        self.assertEqual(([4, 3, 5], [0.0, 0.1414213478565216, 0.1414213925600052]),
                         search_engine.search([0.5, 0.5], 3))
        self.vec_dim, self.index2label, self.vec_list = IOUtil.read_index_vector_json(
            ROOT_TEST_DIR + '/resources/index_vectors_swap.json')
        search_engine.refresh_data_in_engine(self.vec_list)
        response = search_engine.search([0.5, 0.5], 5)
        self.assertEqual(7, response[0][0])
