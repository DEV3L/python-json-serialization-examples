from unittest import TestCase

from python_json_serialization_examples.domain.popo import Popo
from python_json_serialization_examples.schemas.popo_schema import PopoSchema


class TestPopoSchema(TestCase):
    def setUp(self):
        self.popo = Popo()

        self.popo.foo_dict['field_1'] = 'value1'
        self.popo.foo_list.append('value2')
        self.popo.foo_list.append('value3')
        self.popo.foo_var = 'value4'
        self.popo.num = 5

        self.schema = PopoSchema()
        self.schema_many = PopoSchema(many=True)

    def test_to_json(self):
        popo_json = self.schema.dump(self.popo).data
        assert popo_json.get("fooDict") == self.popo.foo_dict
        assert popo_json.get("fooList") == self.popo.foo_list
        assert popo_json.get("fooVar") == self.popo.foo_var
        assert popo_json.get("num") == self.popo.num

    def test_to_json_many(self):
        popo_json_list = self.schema_many.dump([self.popo]).data
        assert len(popo_json_list) == 1

        popo_json_list = self.schema_many.dump([self.popo, self.popo]).data
        assert len(popo_json_list) == 2

        popo_json = popo_json_list[0]

        assert popo_json.get("fooDict") == self.popo.foo_dict
        assert popo_json.get("fooList") == self.popo.foo_list
        assert popo_json.get("fooVar") == self.popo.foo_var
        assert popo_json.get("num") == self.popo.num

    def test_from_json(self):
        popo_json = self.schema.dump(self.popo).data
        _popo = self.schema.load(popo_json).data

        assert _popo.foo_dict == self.popo.foo_dict
        assert _popo.foo_list == self.popo.foo_list
        assert _popo.foo_var == self.popo.foo_var
        assert _popo.num == self.popo.num

    def test_from_json_many(self):
        popo_json = self.schema_many.dump([self.popo]).data
        _popo = self.schema_many.load(popo_json).data[0]

        assert _popo.foo_dict == self.popo.foo_dict
        assert _popo.foo_list == self.popo.foo_list
        assert _popo.foo_var == self.popo.foo_var
        assert _popo.num == self.popo.num

    def test_from_json_string(self):
        popo_json = self.schema.dumps(self.popo).data
        _popo = self.schema.loads(popo_json).data

        assert _popo.foo_dict == self.popo.foo_dict
        assert _popo.foo_list == self.popo.foo_list
        assert _popo.foo_var == self.popo.foo_var
        assert _popo.num == self.popo.num

    def test_from_json_string_many(self):
        popo_json = self.schema_many.dumps([self.popo]).data
        _popo = self.schema_many.loads(popo_json).data[0]

        assert _popo.foo_dict == self.popo.foo_dict
        assert _popo.foo_list == self.popo.foo_list
        assert _popo.foo_var == self.popo.foo_var
        assert _popo.num == self.popo.num
