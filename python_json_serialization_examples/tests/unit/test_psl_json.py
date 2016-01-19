from unittest import TestCase

import json


class TestPSLJson(TestCase):
    def test_to_json(self):
        # complex types need a to_json method
        json_dict = json.dumps({'field_1': 'value_1',
                                'field_2': 'value_2'})
        assert 'value_1' in json_dict
        assert 'value_2' in json_dict
