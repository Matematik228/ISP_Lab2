def to_json(obj):
    ret = ''
    if obj is True:
        return 'true'
    elif obj is False:
        return 'false'
    elif obj is None:
        return 'null'
    elif isinstance(obj, dict):
        ret += '{'
        for key in obj:
            if len(ret) > 1:
                ret += ', '
            ret += to_json(str(key)) + ': ' + to_json(obj[key])
        return ret + '}'
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, (tuple, list)):
        ret += '['
        for x in obj:
            if len(ret) > 1:
                ret += ', '
            ret += to_json(x)
        return ret + ']'
    elif isinstance(obj, str):
        special_symbols = {
            '\b': '\\b',
            '\f': '\\f',
            '\n': '\\n',
            '\r': '\\r',
            '\t': '\\t',
            '\"': '\\\"',
            '\\': '\\\\'
        }
        ret = '\"'
        for ch in obj:
            if ch in special_symbols:
                ret += special_symbols[ch]
            else:
                ret += ch
        return ret + '\"'
    else:
        return to_json(obj.__dict__)


class X:
    def __init__(self):
        self.a = 2
        self.d = 'Some text \t \f \n \' \" /'
        self.dict = {1: 2, 10: "228"}
        self.array = [2392, "Text", True, False, None, (1, 2, {8: 3, 5: "Deep"})]


if __name__ == '__main__':
    print(to_json(X()))
