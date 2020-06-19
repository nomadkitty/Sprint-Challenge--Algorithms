'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case: when there's no th
    count = 0
    if word.find("th") == -1:
        return count

    # recursion: find and then slice the list
    if word.find("th") >= 0:
        count += 1
        word = word[word.find("th")+1:]

    return count + count_th(word)
