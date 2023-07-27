def bool2bit(_bool):
    return 1 if _bool else 0
    
def solution(ineq, eq, n, m):
    comparison_operator = ineq + eq
    
    if comparison_operator == ">=":
        return bool2bit(n >= m)
    elif comparison_operator == "<=":
        return bool2bit(n <= m)
    elif comparison_operator == ">!":
        return bool2bit(n > m)
    elif comparison_operator == "<!":
        return bool2bit(n < m)
    else:
        return -1