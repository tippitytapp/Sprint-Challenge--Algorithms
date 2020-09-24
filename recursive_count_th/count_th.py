'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, count = 0):
    # initialize a count variable to keep track of how many times _th_ is found
    # start count at 0

    # BASE CASE:
    # if the _word_ is an empty string
    # return 0
    if word == '':
        return count
    
    # if there are more than 2 letters in the _word_
    # compare each letter and letter + 1 to see if they are _th_
    # SECOND BASE CASE:
    # letter 1 and letter + 1 = _th_ remove and increase count
    if len(word) >= 2 and (word[0] + word[1] == 'th'):
        # then recurse through the word and compare it again
        return 0 + count_th(word[2:], count + 1)
    else:
        # and letter and letter + 1 != _th_ remove the first letter and then recurse through it again
        return count_th(word[1:], count)


