"""Define the abstract class for results Post-Processing"""


class ResultsPostProcessing:
    """Result Post-Processing handles labels, re-ranking, re-scoring"""

    def __init__(self):
        pass

    def add_labels(self, result_vector, labels):
        pass

    def re_rank_results(self):
        pass
