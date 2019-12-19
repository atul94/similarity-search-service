"""Define the abstract class for similarity search service controllers"""


class SearchService:
    """Search Service handles all controllers in the search service"""

    def __init__(self):
        pass

    def load_index(self):
        pass

    def load_labels(self):
        pass

    def similar_search_vectors(self):
        pass

    def refresh_index(self):
        pass

    def health_check(self):
        pass
