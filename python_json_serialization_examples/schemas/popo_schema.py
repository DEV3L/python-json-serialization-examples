from marshmallow import Schema, fields, post_load

from python_json_serialization_examples.domain.popo import Popo


class PopoSchema(Schema):
    num = fields.Number()
    fooVar = fields.Str(attribute='foo_var')
    fooList = fields.List(fields.String, attribute='foo_list')
    fooDict = fields.Dict(attribute='foo_dict')

    @post_load
    def make_popo_domain_object(self, data):
        _popo = Popo()
        _popo.foo_dict = data.get('foo_dict')
        _popo.foo_list = data.get('foo_list')
        _popo.foo_var = data.get('foo_var')
        _popo.num = int(data.get('num'))
        return _popo
