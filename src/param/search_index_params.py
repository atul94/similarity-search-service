"""Default parameter values for Search Engine"""
from param.search_index_type import SearchIndexType


class SearchEngineParams:
    DEFAULT_SIMILARITY_METRIC = 'euclidean'
    DEFAULT_NUM_TREES = 5
    DEFAULT_SEARCH_DEPTH = 4
    DEFAULT_SEARCH_ENGINE_TYPE = SearchIndexType.ANNOY
    DEFAULT_VECTOR_DIM = 100
    DEFAULT_VECTOR_LIST_JSON_PATH = '/app/resources/current_list.json'
