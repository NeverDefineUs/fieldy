import json

class SchemaManager:
  def __init__(self, base_path = None):
    self.base_path = base_path
    self.schemas = {}
    self.base_types = ["string", "integer", "float", "boolean"]
  
  def load(self, name):
    file = open(self.base_path + name + '.json', 'r')
    txt = file.read()
    file.close()
    schema = json.loads(txt)
    if name != schema['typename']:
      raise Exception('File {} doesn\'t match typename {}'.format(name, schema['typename']))
    self.schemas[name] = schema
    for field_name in schema['fields']:
      field = schema['fields'][field_name]
      field_type = field["type"]
      if field_type in self.base_types:
        continue
      if field_type not in self.schemas.keys():
        self.load(field_type)