from . import Util

class Validator:
  def __init__(self, schema, schema_manager):
    self.schema = schema
    self.schema_manager = schema_manager

  def validate(self, entry):
    for field_name in entry.keys():
      field = entry[field_name]
      if field_name not in self.schema['fields'].keys():
        raise Exception('Field {} not defined in schema'.format(field_name))
    for field_name in  self.schema['fields'].keys():
      field = self.schema['fields'][field_name]
      if field_name not in entry.keys():
        if field["required"]:
          raise Exception('Missing required field: {}'.field_name)
        continue
      field_type = field["type"]
      if field_type in Util.get_base_types():
        if field_type == "string":
          if type(entry[field_name]) != str:
            raise Exception('Field {} should be a str'.format(field_name))
        if field_type == "integer":
          if type(entry[field_name]) != int:
            raise Exception('Field {} should be a inr'.format(field_name))
        if field_type == "float":
          if type(entry[field_name]) != float:
            raise Exception('Field {} should be a float'.format(field_name))
        if field_type == "boolean":
          if type(entry[field_name]) != bool:
            raise Exception('Field {} should be a bool'.format(field_name))
      else:
        continue