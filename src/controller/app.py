from flask_restplus import Resource, Api
from src import SSS_APP
from engine.search_engine import SearchEngineSingleton
from param.search_index_state import SearchIndexState
from param.search_index_params import SearchEngineParams
from util.io_util import IOUtil
from biz.similarity_search_service_biz import SimilaritySearchServiceBiz
from flask_restplus import reqparse
from src import ROOT_MAIN_DIR

api = Api(SSS_APP,
          version='1.0 - Similarity Search Service with Annoy Search Index',
          title='Similarity Search Service API',
          description='API to render the response for Query Vector From Indexed Vector Data',
          default='Prod', default_label='In A/B Testing Stage')

vec_dim, index2label, vec_list = IOUtil.read_index_vector_json(
    ROOT_MAIN_DIR + '/test/resources/index_vectors_swap.json')
search_engine = SearchEngineSingleton(vector_dim=vec_dim, index_vectors=vec_list)


@api.route('/api/search')
class SearchService(Resource):
    """
    SearchService: To get response for similar query vector
    """
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('vec_rep', type=float, action='append', help='vector representation of the object')
    post_parser.add_argument('cacheable', type=str)
    post_parser.add_argument('numVec', type=int)

    @api.expect(post_parser)
    @api.response(200, 'Success')
    @api.response(400, 'Error in POST Request')
    def post(self):
        args = self.post_parser.parse_args()
        similarity_service_biz = SimilaritySearchServiceBiz()
        return similarity_service_biz.dump_similar_search_service_response(query_vec=args['vec_rep'],
                                                                           top_k=args['numVec'],
                                                                           index2label=index2label)


@api.route('/api/updateIndex')
class SearchEngineIO(Resource):
    """
    SearchEngineIO: To update Search ENgine with new index
    """
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('toggleIndexType', type=str)

    @api.expect(post_parser)
    @api.response(200, 'Success')
    @api.response(400, 'Error in POST Request')
    def post(self):
        global index2label, vec_dim, vec_list, search_engine
        index2label, vec_dim, vec_list = IOUtil.read_index_vector_json(SearchEngineParams.DEFAULT_VECTOR_LIST_JSON_PATH)
        similarity_service_biz = SimilaritySearchServiceBiz()
        similarity_service_biz.refresh_vec_list(vec_list)


@api.route('/api/health_check')
class SearchServiceHealthCheck(Resource):
    """
    Health Check: Returning 200 when the Search Index is build
    """

    def get(self):
        return ("{Error}", 500) if search_engine.live_index_build_status is SearchIndexState.UN_BUILD else (
            "{Success}", 200)


# This will not be called when uwsgi server will be up
if __name__ == "__main__":
    try:
        SSS_APP.run(host='localhost', debug=True, port=8080)
    except BaseException:
        SSS_APP.logger.error(" Unable to start the App")
