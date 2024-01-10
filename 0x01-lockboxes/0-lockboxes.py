"""Module containing solution for lockboxes"""


def canUnlockAll(boxes):
    """Solution function"""
    # create a truth List for
    truth_list = [True if _ == 0 else False for _ in range(len(boxes))]
    opened_list = [False for _ in boxes]

    def check():
        for i in range(len(boxes)):
            if (opened_list[i] != truth_list[i]):
                return False
        return True
    while not check():
        for j in range(len(boxes)):
            if truth_list[j]:
                opened_list[j] = True
                for i in boxes[j]:
                    try:
                        truth_list[i] = True
                    except Exception as e:
                        pass
    return all([True if _ else False for _ in truth_list])
