#Name: Juan Gonzalez
#ID: 1808943

def selection_sort_descend_trace(list):
    for i in range(len(list) - 1):
        nums = i
        for j in range(i + 1, len(list)):
            if list[j] > list[nums]:
                nums = j
        list[i], list[nums] = list[nums], list[i]
        print(' '.join([str(x) for x in list]), '')
    return list


if __name__ == '__main__':
    num_list = [int(x) for x in input().split()]
    selection_sort_descend_trace(num_list)