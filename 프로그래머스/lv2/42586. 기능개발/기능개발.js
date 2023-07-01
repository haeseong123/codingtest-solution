// <문제 설명>
// 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
// 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

// 아래 매개변수가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 반환해 주세요.
// progresses: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 
// speeds: 각 작업의 개발 속도가 적힌 정수 배열 

// <제한사항>
// 작업의 개수 progresses, speeds 배열의 길이는 100개 이하입니다.
// 작업 진도는 100 미만의 자연수입니다.
// 작업 속도는 100 이하의 자연수입니다.
// 배포는 하루에 한 번만 할 수 있으며,
// 하루의 끝에 이루어진다고 가정합니다.
// 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

// <문제 풀이>
// 진도를 더한다.
// 진도가 100% 이상이라면 해당 작업을 배포할 수 있다.

// 각 progresses의 맨 앞의 작업을 완료하기 위해 필요한 일 수를 저장하는 require_days를 선언합니다.
// 완료하는 데 필요한 x는
// x = Math.ceil((100 - 작업 진도) / 작업 속도) 
// 이때 작업 진도는 아래와 같이 초기화 하고 위 식을 적용해야 합니다.
// 작업 진도 += 작업 속도 * require_days
function solution(progresses, speeds) {
    var answer = [];
    let days = 0;
    let count = 0;
    let i = 0;
    
    while (i < progresses.length) {
        const progress = progresses[i] + (speeds[i] * days)
        if (progress >= 100) {
            count += 1;
            i += 1;
        } else {
            if (count) {
                answer.push(count);                
                count = 0;
            }
            days += Math.ceil((100 - progress) / speeds[i]);
        }
    }
    
    answer.push(count);
    return answer;
}