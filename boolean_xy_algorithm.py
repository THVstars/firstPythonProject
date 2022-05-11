def xo(txt):
    return txt.casefold().count("x") == txt.casefold().count("o")


print(xo("xoXOxoXoxO"))
