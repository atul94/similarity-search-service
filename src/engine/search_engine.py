"""Search Engine Implementation"""
from param.search_index_params import SearchEngineParams
from param.search_index_state import SearchIndexState
from index.annoy_search_index import AnnoySearchIndex


class SearchEngine:

    def __init__(self, vector_dim=SearchEngineParams.DEFAULT_VECTOR_DIM,
                 similarity_metric=SearchEngineParams.DEFAULT_SIMILARITY_METRIC,
                 num_trees=SearchEngineParams.DEFAULT_NUM_TREES,
                 search_depth=SearchEngineParams.DEFAULT_SEARCH_DEPTH,
                 search_index_type=SearchEngineParams.DEFAULT_SEARCH_ENGINE_TYPE, index_vectors=None, load=False,
                 load_path=None):
        self.__vector_dim = vector_dim
        self.__similarity_metric = similarity_metric
        self.__num_trees = num_trees
        self.__search_depth = search_depth
        self.__search_index_type = search_index_type
        if load:
            self.__live_search_index = AnnoySearchIndex(vector_dim, similarity_metric, num_trees, search_depth, load,
                                                        load_path)
        else:
            self.__live_search_index = AnnoySearchIndex(vector_dim=vector_dim, similarity_metric=similarity_metric,
                                                        num_trees=num_trees, search_k=search_depth)
            self.put_vector_list_in_index(self.__live_search_index, index_vectors)
        self.__shadow_search_index = AnnoySearchIndex(vector_dim=vector_dim, similarity_metric=similarity_metric,
                                                      num_trees=num_trees, search_k=search_depth)
        self.build_index(self.__live_search_index)

    def put_vector_list_in_index(self, search_index, vector_list):
        for vec in vector_list:
            self.put_vector_in_index(search_index, vec)

    def put_vector_in_index(self, search_index, vec):
        assert len(vec) == self.__vector_dim, "Vector dimension and acceptable vector_dim unequal"
        assert search_index.index_build_status is SearchIndexState.UN_BUILD, "Cannot add a vector in an built index"
        search_index.add_vec_to_index(vec)

    def add_vector_list(self, vector_list):
        assert self.__shadow_search_index.index_build_status is SearchIndexState.UN_BUILD, \
            "Cannot add vector in shadow index. Is in build state."
        for vec in vector_list:
            self.put_vector_in_index(self.__shadow_search_index, vec)

    def swap_search_index(self):
        self.__live_search_index, self.__shadow_search_index = self.__shadow_search_index, self.__live_search_index
        self.__shadow_search_index.clear_search_index()

    def refresh_data_in_engine(self, vec_list):
        self.add_vector_list(vec_list)
        self.build_index(self.__shadow_search_index)
        self.swap_search_index()

    @staticmethod
    def build_index(search_index):
        search_index.build_search_index()
