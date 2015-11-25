def charswap(input):
    s = str(input)
    if len(str(s)) > 1:
        return s[len(s)-1] + s[1:len(s)-1] + s[0]
    else:
        return s