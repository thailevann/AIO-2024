#caculate f1-score
def exercise(tp, fp, fn):
    if not type(tp) is int:
        raise TypeError("tp must be int")
    if not type(fp) is int:
        raise TypeError("fp must be int")
    if not type(fn) is int:
        raise TypeError("fn must be int")
    if tp == 0 or fp == 0 or fn == 0:
        raise TypeError("tp and fp and fn must be greater than zero")
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*(precision*recall/(precision+recall))
    return precision, recall, f1
if __name__== "__main__":

    try:
        tp = 0
        fp = 1
        fn = 4
        precision, recall, f1 = exercise(tp, fp, fn)
        print(f"precision is {precision}")
        print(f'recall is {recall}')
        print(f'f1-score is {f1}')
    except (TypeError, ValueError) as e:
        print(e)


