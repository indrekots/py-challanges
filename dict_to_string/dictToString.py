def dictToString(dict):
    result = ''
    for i in dict:
        if dict.get(i) is not None:
            result += str(i) + '=' + str(dict.get(i)) + ';'
    return result