""" Implementation of search Index of Spotify: Annoy"""
from core.search_index import SearchIndex
from annoy import AnnoyIndex
from param.search_index_params import SearchEngineParams
from param.search_index_state import SearchIndexState


class AnnoySearchIndex(SearchIndex):

    def __init__(self, vector_dim=SearchEngineParams.DEFAULT_VECTOR_DIM,
                 similarity_metric=SearchEngineParams.DEFAULT_SIMILARITY_METRIC,
                 num_trees=SearchEngineParams.DEFAULT_NUM_TREES,
                 search_k=SearchEngineParams.DEFAULT_SEARCH_DEPTH, load=False, load_path=None):
        self.__similarity_metric = similarity_metric
        self.__num_tree = num_trees
        self.__search_k = search_k
        self.__vector_dim = vector_dim
        self.__live_search_index = self.get_new_annoy_index()
        self.__shadow_search_index = self.get_new_annoy_index()
        self.__index_build_status = SearchIndexState.UN_BUILD
        self.__vec_count = 0
        if load:
            self.load_index(path=load_path)
        else:
            self.__search_index = self.create_search_index()

    def get_new_annoy_index(self):
        return AnnoyIndex(self.__vector_dim, self.__similarity_metric)

    def create_search_index(self):
        search_index = self.get_new_annoy_index()
        return search_index

    def build_search_index(self):
        self.__search_index.build(self.__num_tree)
        self.__index_build_status = SearchIndexState.BUILD

    def clear_search_index(self):
        self.__search_index.unload()
        self.__index_build_status = SearchIndexState.UN_BUILD
        self.__vec_count = 0

    def add_vec_to_index(self, additional_vec):
        self.__search_index.add_item(self.__vec_count, additional_vec)
        self.__vec_count = self.__vec_count + 1

    def get_similar_vectors(self, query_vec, top_k):
        return self.__search_index.get_nns_by_vector(query_vec, top_k, search_k=self.__search_k, include_distances=True)

    def save_index(self, path):
        self.__search_index.save(path)

    def load_index(self, path):
        search_index = self.get_new_annoy_index()
        search_index.load(path)
        self.__search_index = search_index

    @property
    def index_size(self):
        return self.__vec_count

    @property
    def index_build_status(self) -> SearchIndexState:
        return self.__index_build_status
