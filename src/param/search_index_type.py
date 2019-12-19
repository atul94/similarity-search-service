"""Enum for index type in the search Engine"""

from enum import Enum, auto


class SearchIndexType(Enum):
    ANNOY = auto()
    FAISS = auto()
