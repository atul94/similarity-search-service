"""Define the abstract class for Information Retrieval From Index"""


class InformationRetrieval:
    """ Information retrieval handles getting list of closest indexed vectors for the query vector"""

    def __init__(self):
        pass

    def get(self, query_vector):
        pass

    def refresh_index(self, search_index):
        pass

    def custom_get(self, query_vector, similarity_metric):
        pass
