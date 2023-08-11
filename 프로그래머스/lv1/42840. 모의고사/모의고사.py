def solution(answers):
    corrects = [0, 0, 0]
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i, answer in enumerate(answers):
        if answer == supo1[i % len(supo1)]:
            corrects[0] += 1
        if answer == supo2[i % len(supo2)]:
            corrects[1] += 1
        if answer == supo3[i % len(supo3)]:
            corrects[2] += 1
    
    maxScore = max(corrects)
    return [i + 1 for i, c in enumerate(corrects) if c == maxScore]