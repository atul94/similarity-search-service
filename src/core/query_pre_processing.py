"""Define the abstract class for Query Pre-Processing."""


class QueryPreProcessing:
    """" Query Pre-Processing Module handles Query Vector Pre-Processing like Padding, Differential Weighting etc."""

    def __init__(self):
        pass

    def pad_query_vector(self, query_vector, pad_len):
        pass

    def weight_query_vector(self, query_vector, weight_schema):
        pass
