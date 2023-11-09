def solution(data, col, row_begin, row_end):
    answer = 0
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))

    for (i, row) in enumerate(sorted_data[row_begin - 1 : row_end]):
        row_num = i + row_begin
        answer ^= sum(n % row_num for n in row)

    return answer
