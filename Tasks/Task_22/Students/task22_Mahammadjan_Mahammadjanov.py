def hypen_sorter(text):
    text = text.split("-")
    text.sort()
    connector = "-"
    newtext = connector.join(text)
    return newtext

print(hypen_sorter(input()))