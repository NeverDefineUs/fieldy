import python.SchemaManager as Schema
from python.Encoder import Encoder
sm = Schema.SchemaManager('samples/')
sm.load('composed')
b = {'simple':{'name':'arthur'}}
v = Encoder(sm)
print(v.to_object(b, 'composed').__dict__)
print(v.to_object(b, 'composed').simple.__dict__)
