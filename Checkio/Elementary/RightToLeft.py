def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    # short answer
    temp = ','.join(phrases).replace('right', 'left')
    # result = []
    # for phrase in phrases:
    #     if phrase.__contains__('right'):
    #         result.append(phrase.replace('right', 'left'))
    #     else:
    #         result.append(phrase)
    # temp = result.__str__().replace('[', '').replace(']', '').replace("'", '').replace(', ', ',')
    return temp


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
