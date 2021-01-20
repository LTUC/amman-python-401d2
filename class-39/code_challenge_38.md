

                    source
            /                   \
        s1                       s2
    /         \               /      \


(1,,)

(35, (41, (33,,), (52,,) ), (59, (30, ,), (44, ,)))

function waterUsage(source)
    if source is None:
        return 0
    return source[0] + waterUsage(source[1]) + waterUsage(source[2])

function waterUsage(source)
    sum = source[0]
    function calcSum(t):
        if not t:
            return
        sum1 = t[0] + calcSum(t[1]) + calcSum(t[2])
        sum += sum1
    calcSum(source[1])
    calcSum(source[2])
