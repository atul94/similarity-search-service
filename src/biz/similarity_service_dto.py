"""DTOs for responses of APIs"""

from marshmallow import Schema, fields, post_dump


class SearchItemDTO:
    def __init__(self, identifier_key, similarity_score):
        self.__identifier_key = identifier_key
        self.__similarity_score = similarity_score

    @property
    def identifier_key(self):
        return self.__identifier_key

    @property
    def similarity_score(self):
        return self.__similarity_score


class SearchItemDTOSchema(Schema):
    identifier_key = fields.Str()
    similarity_score = fields.Float()


class SearchServiceResponseDTO:
    def __init__(self, query_vec_dim, response_item_list):
        self.__query_vec_dim = query_vec_dim
        self.__response_item_list = response_item_list

    @property
    def query_vec_dim(self):
        return self.__query_vec_dim

    @property
    def response_item_list(self):
        return self.__response_item_list


class SearchServiceResponseDTOSchema(Schema):
    query_vec_dim = fields.Integer()
    response_item_list = fields.List(fields.Nested(SearchItemDTOSchema))
