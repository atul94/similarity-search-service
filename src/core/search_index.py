""" Define the abstract class for Search Index"""


class SearchIndex:
    """Search Index handles creation of various search index, getting values, destroying search index"""

    def create_search_index(self):
        pass

    def clear_search_index(self):
        pass

    def get_similar_vectors(self, query_vec, top_k):
        pass
