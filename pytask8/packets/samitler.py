def samit(env):
    samitler = set()
    for letter in env:
        if letter.isalpha():
            samitler.add(letter.lower())
    return samitler