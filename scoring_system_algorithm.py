def calculate_scores(txt):
    return [txt.count("A"), txt.count("B"), txt.count("C")]


print(calculate_scores("ABBCCC"))