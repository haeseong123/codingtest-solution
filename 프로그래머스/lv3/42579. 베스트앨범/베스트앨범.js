// <문제 설명>
// 스트리밍 사이트에서 장르 별로 
// 가장 많이 재생된 노래를 두 개씩 모아 
// 베스트 앨범을 출시하려 합니다. 
// 노래는 고유 번호로 구분하며, 
// 노래를 수록하는 기준은 다음과 같습니다.

// 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
// 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
// 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

// 아래 매개변수가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 반환해 주세요.
// genres: 노래의 장르를 나타내는 문자열 배열
// plays: 노래별 재생 횟수를 나타내는 정수 배열

// <제한사항>
// genres[i]는 고유번호가 i인 노래의 장르입니다.
// plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
// genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
// 장르 종류는 100개 미만입니다.

// "classic": 500, 150, 800 = 1450
// "pop": 600, 2500 = 3100

// map<장르 이름: [(재생 횟수, 인덱스), ...]>
// map을 list로 변환
//      => [[(재생 횟수, 인덱스), ...], ...]
// list를 재생횟수 오름차순으로 저장
// list의 길이가 0 초과일때 동안 
//      list pop해가며 아래 수행
//          해당 원소를 오름차순으로 저장
//          맨 뒤, 맨 뒤 - 1의 인덱스를 answer에 append
// answer 반환


function solution(genres, plays) {
    // 1.
    const map = new Map();
    for (let i = 0; i < genres.length; i++) {
        const g = genres[i], 
              p = plays[i];
        const value = map.get(g) || [0, []];
        value[0] += p;
        value[1].push([p, i]);
        map.set(g, value);
    }
    
    // 2.
    const list = [...map.values()]
    list.sort((a, b) => {
        if (a[0] < b[0]) return -1;
        else if (a[0] === b[0]) return 0;
        else return 1;
    })
    
    // 3.
    const answer = [];
    while (list.length) {
        const [_, value] = list.pop();
        value.sort((a, b) => {
            if (a[0] < b[0]) return -1;
            else if (a[0] === b[0]) {
                if (a[1] <= b[1]) return 1;
                else return -1;
            }
            else return 1;
        });
        
        const repeat = Math.min(2, value.length);
        for (let i=0; i < repeat; i++) {
            answer.push(value.pop()[1]);            
        }
    }
    
    return answer;
}