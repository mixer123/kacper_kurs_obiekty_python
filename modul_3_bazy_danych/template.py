from string import Template
message =Template('$name zjadł $count nalesników ')

info =[
    ('mirek', 20),
    ('ela', 30)
]

for name1, count1 in info:
    text = message.substitute(name=name1, count=count1)
    print(text)