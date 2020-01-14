"""Utility Class for reading and writing input output"""
import json


class IOUtil:

    @staticmethod
    def read_index_vector_json(file_path):
        with open(file_path, 'r') as json_file:
            input_file = json.load(json_file)
            label_list = [entry['label'] for entry in input_file['keys']]
            vector_list = [entry['embedding'] for entry in input_file['keys']]
            index2label = {index: label for index, label in enumerate(label_list)}
            vec_dim = len(vector_list[0])
        return vec_dim, index2label, vector_list
