"""Enum for index status in the search Engine"""

from enum import Enum, auto


class SearchIndexState(Enum):
    """Status when the index is in build state"""
    BUILD = auto()
    """Status when index is not in build state"""
    UN_BUILD = auto()
