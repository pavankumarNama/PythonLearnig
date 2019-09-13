# re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
VOWELS = "aeiouy"


def translate(phrase):
    # re.sub(r'(([^aeiouy\s][aeiouy]|[aeiouy]{3}))', lambda s: s[0][0], phrase)
    # lambda s:s and s[0]+translate(s[1+int(s[0]!=' ')+int('aeiouy'.find(s[0])>=0):])
    # t=lambda s:s and s[0]+t(s[2+int('aeiouy'.find(s[0])>=0):])
    # translate=lambda s:' '.join(map(t,s.split()))
    # translate=lambda s:s and s[0]+translate(s[1+(s[0]!=' ')+(s[0]in'aeiouy'):])
    # pattern = re.compile('(([aeiouy])[aeiouy]{2})|(([^aeiouy])[aeiouy])')
    # return ' '.join([''.join([i.group(2) or i.group(4) for i in pattern.finditer(word)]) for word in phrase.split(' ')])
    # prune = lambda exp, phr: sub(exp.format(VOWELS), r'\1', phr)
    #     return prune(r'([{0}])\1\1', prune(r'([^ {0}])[{0}]', phrase))
    # return re.sub(r'(\w)\1?.', r'\1', phrase)
    # PATTERN = re.compile(r'([a-z])\1?[' + VOWELS + ']')
    # return PATTERN.sub(r'\1', phrase)
    # phrase = re.sub(r'([^aeiouy ])\w', r'\1', phrase)
    #     phrase = re.sub(r'([aeiouy]){3}', r'\1', phrase)
    #     return phrase

    result = []
    human_phrase = []
    i = 0
    for j in range(len(phrase)):
        if phrase[j] == ' ':
            result.append(phrase[j])
        elif phrase[j] not in VOWELS:
            if phrase[j + 1] in VOWELS:
                result.append(phrase[j])
        elif phrase[j] in VOWELS and phrase[j - 1] not in VOWELS and phrase[j - 1] != ' ':
            pass
        else:
            result.append(phrase[j])

    result = ''.join(result)
    output = ''
    x = 0

    while x < len(result):
        if result[x] in VOWELS:
            output += result[x]
            x += 3
        else:
            output += result[x]
            x += 1

    # print(output)
    return output
    # while i < len(phrase):
    #     human_phrase.append(phrase[i])
    #     if phrase[i] in VOWELS:
    #         i += 3
    #     elif phrase[i] == ' ':
    #         i += 1
    #     else:
    #         i += 2
    # return ''.join(human_phrase)


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
