"""Business logic implementation for Retrieving information, modifying index from and in Search Engine"""
from engine.search_engine import SearchEngineSingleton
from biz.similarity_service_dto import SearchServiceResponseDTOSchema, SearchItemDTO, SearchServiceResponseDTO, \
    SearchItemDTOSchema


class SimilaritySearchServiceBiz:

    def __init__(self):
        self.__search_engine = SearchEngineSingleton()
        self.__vec_dim = self.__search_engine.vec_dim

    def refresh_vec_list(self, vector_list):
        self.__search_engine.refresh_data_in_engine(vector_list)

    def get_similar_vector(self, query_vec, top_k):
        return self.__search_engine.search(self.pad_query_vector(query_vec), top_k)

    def pad_query_vector(self, query_vec):
        assert len(query_vec) <= self.__vec_dim, "Query Vector larger than acceptable dimensions passed"
        if len(query_vec) == self.__vec_dim:
            return query_vec
        else:
            query_vec += [0] * (self.__vec_dim - len(query_vec))
            return query_vec

    def pad_query_vec_list(self, vec_list):
        mod_vec_list = [self.pad_query_vector(vec) for vec in vec_list]
        return mod_vec_list

    @staticmethod
    def map_search_response_to_dto(engine_response, index2label: dict):
        schema = SearchItemDTOSchema()
        dto_list = [SearchItemDTO(index2label[index], similarity_score)for index, similarity_score in zip(*engine_response)]
        return [schema.dump(x) for x in dto_list]

    def get_similar_search_response(self, query_vec: list, top_k: int, index2label: dict):
        return SearchServiceResponseDTO(self.__vec_dim,
                                        self.map_search_response_to_dto(self.get_similar_vector(query_vec, top_k),
                                                                        index2label))

    def dump_similar_search_service_response(self, query_vec: list, top_k: int, index2label: dict):
        schema = SearchServiceResponseDTOSchema()
        return schema.dump(self.get_similar_search_response(query_vec, top_k, index2label))
