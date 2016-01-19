from unittest import TestCase

import json


class TestPSLJson(TestCase):
    def test_to_json(self):
        # complex types need a to_json method
        dict_json = json.dumps({"field_1": "value_1",
                                "field_2": "value_2"})
        assert dict_json.get("field_1") == "value_1"
        assert dict_json.get("field_2") == "value_2"
