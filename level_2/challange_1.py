def solution(total_lambs):
    _sum = 1
    gen_count = 0
    while _sum + _sum <= total_lambs+1:
        _sum += _sum
        gen_count += 1
    
    _sum = 1
    last_num = 1
    last_sum = 0
    str_count = 0
    while _sum + last_num <= total_lambs+1:
        last_sum = _sum
        _sum = _sum + last_num
        last_num = last_sum
        str_count += 1
    
    return str_count - gen_count