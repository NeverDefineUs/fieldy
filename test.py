from fieldy import SchemaManager, Encoder
sm = SchemaManager('../samples/')
sm.load('composed')
b = {'simple':{'name':'arthur'}}
v = Encoder(sm)
print(v.to_object(b, 'composed').__dict__)
print(v.to_object(b, 'composed').simple.__dict__)
