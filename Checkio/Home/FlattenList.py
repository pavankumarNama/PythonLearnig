output = []


def remove_list(inner_list):
    for val in inner_list:
        if isinstance(val, list):
            remove_list(val)
        else:
            output.append(val)
    return output


def flat_list(array):
    print(eval('['+str(array).replace('[', '').replace(']', '')+']'))
    return eval('['+str(array).replace('[', '').replace(']', '')+']')
    # f = lambda x: [val for val in array]
    # print([ if isinstance(val, list) else val for val in array])

    # print(type(array.__iter__().__next__()))
    # s_array = str(array)
    # output = []
    # for val in s_array:
    #     if val.isalnum():
    #         output.append(int(val))
    #
    # print(output)
    # for val in array:
    #     if isinstance(val, list):
    #         remove_list(val)
    #     else:
    #         output.append(val)
    #
    # result = []
    # result.extend(output)
    # # print(result)
    # output.clear()
    # return result


if __name__ == '__main__':
    print(remove_list([1, [2, 2, 2], 4]))
    # assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    # assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    # assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    # assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
