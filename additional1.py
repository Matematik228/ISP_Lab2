def from_json(text):
    def pos(ind):
        is_str = False
        balance = 0
        punctuation = {',', ':'}
        while ind < len(text):
            if text[ind] == '\"':
                is_str = not is_str
            elif not is_str:
                if text[ind] == '{' or text[ind] == '[':
                    balance += 1
                elif text[ind] == '}' or text[ind] == ']':
                    balance -= 1
            if not is_str and balance == 0 and text[ind] in punctuation:
                return ind
            ind += 1
        return len(text) - 1

    if text == 'true':
        return True
    if text == 'false':
        return False
    if text == 'null':
        return None
    if text[0] == '\"':
        string = ''
        special_symbols = {
            'b': '\b',
            'f': '\f',
            'n': '\n',
            'r': '\r',
            't': '\t',
            '\"': '\"',
            '\\': '\\'
        }
        i = 1
        while i < len(text) - 1:
            if text[i] == '\\' and text[i + 1] in special_symbols:
                string += special_symbols[text[i + 1]]
                i += 1
            else:
                string += text[i]
            i += 1
        return string
    if text[0] == '{':
        dictionary = dict()
        start = 1
        while start < len(text) - 1:
            end = pos(start)
            key = from_json(text[start:end])
            start = end + 2
            end = pos(start)
            dictionary[key] = from_json(text[start:end])
            start = end + 2
        return dictionary
    if text[0] == '[':
        arr = []
        start = 1
        while start < len(text) - 1:
            end = pos(start)
            arr.append(from_json(text[start:end]))
            start = end + 2
        return arr
    try:
        return int(text)
    except ValueError:
        return float(text)


print(from_json('{"a": 2, "d": "Some text \\t \\n", "dict": {"1": 2, "10": "228"}, "array": [2392, "Text", ' +
                'true, false, null, [1, 2, {"8": 3, "5": "Deep"}]]}'))
