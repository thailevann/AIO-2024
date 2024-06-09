# Calculate F1-score
def exercise(tp, fp, fn):
    if not isinstance(tp, int):
        raise TypeError("tp must be an integer")
    if not isinstance(fp, int):
        raise TypeError("fp must be an integer")
    if not isinstance(fn, int):
        raise TypeError("fn must be an integer")
    if tp <= 0 or fp <= 0 or fn <= 0:
        raise ValueError("tp, fp, and fn must be greater than zero")

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * (precision * recall / (precision + recall))
    return precision, recall, f1

if __name__ == "__main__":
    try:
        tp = 0
        fp = 1
        fn = 4
        precision, recall, f1 = exercise(tp, fp, fn)
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1-score: {f1}")
    except (TypeError, ValueError) as e:
        print(e)
