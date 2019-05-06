from pprint import pprint

s = 'str'

magic_methods = [
    method for method in dir(s)
    if method.startswith('__') and method.endswith('__')
]

pprint(magic_methods)
