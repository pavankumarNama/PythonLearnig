# def between_markers(text: str, begin: str, end: str) -> str:
#     """
#         returns substring between two given markers
#     """
#     # your code here
#     start = text.index(begin)
#     end = text.index(end)
#     return text[start+1:end]
#
#
# if __name__ == '__main__':
#     print('Example:')
#     print(between_markers('What is >apple<', '>', '<'))
#
#     # These "asserts" are used for self-checking and not for testing
#     assert between_markers('What is >apple<', '>', '<') == "apple"
#     assert between_markers('What is [apple]', '[', ']') == "apple"
#     assert between_markers('What is ><', '>', '<') == ""
#     assert between_markers('>apple<', '>', '<') == "apple"
#     print('Wow, you are doing pretty good. Time to check it!')


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    if text.find(begin) == -1 and text.find(end) != -1:
        return text[0:text.find(end)]
    elif text.find(begin) != -1 and text.find(end) == -1:
        return text[text.find(begin)+len(begin):]
    elif text.find(begin) == -1 and text.find(end) == -1:
        return text
    elif text.find(begin) > text.find(end):
        return ''
    else:
        return text[text.index(begin)+len(begin):text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
