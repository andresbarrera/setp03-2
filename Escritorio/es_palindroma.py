def es_palindroma(string):
    string_lista=list(string)
    string_inverso=string_lista
    string_inverso=string_inverso[-1::-1]
    if string_lista == string_inverso:
        return True
    else:
        return False
