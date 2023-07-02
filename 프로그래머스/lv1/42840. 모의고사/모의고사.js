function solution(answers) {
    const one = [1,2,3,4,5],
          two = [2,1,2,3,2,4,2,5],
          three = [3,3,1,1,2,2,4,4,5,5];
    const corrects = [0, 0, 0];
    
    for (let i = 0; i < answers.length; i++) {
        corrects[0] += one[i % 5] === answers[i] ? 1 : 0;
        corrects[1] += two[i % 8] === answers[i] ? 1 : 0;
        corrects[2] += three[i % 10] === answers[i] ? 1 : 0;
    }
    
    const answer = []
    const first = Math.max(...corrects);
    for (let i = 0; i < 3; i++) {
        if (corrects[i] === first) {
            answer.push(i + 1);
        }
    }
    return answer;
}