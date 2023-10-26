def solution(x, y):
    if len(x) > len(y):
        for i in range(len(x)):
            try:
                y.index(x[i])
            except ValueError:
                return x[i]

    else:
        for i in range(len(y)):
            try:
                x.index(y[i])
            except ValueError:
                return y[i]