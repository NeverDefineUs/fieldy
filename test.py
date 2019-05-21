from fieldy import SchemaManager, Encoder
sm = SchemaManager('samples/')
sm.load('composed')
b = {'simple':{'name':'arthur', 'dt': '2019-05-21'}}
v = Encoder(sm)
print(v.to_object(b, 'composed').__dict__)
print(v.to_object(b, 'composed').simple.__dict__)
