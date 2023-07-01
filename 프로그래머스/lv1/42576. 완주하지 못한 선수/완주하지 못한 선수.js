// <문제 설명>
// 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
// 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
// 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
// 완주하지 못한 선수의 이름을 return 하도록 solition 함수를 작성해주세요.

// participant: 마라톤에 참여한 선수들의 이름이 담긴 배열
// compeltion: 완주한 선수들의 이름이 담긴 배열
// return: 완주하지 못한 선수의 이름

// <제한사항>
// 1 <= len(participant) <= 100,000
// len(participant) == len(completion) - 1
// 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
// 참가자 중에는 동명이 있을 수 있습니다.

// <문제 풀이 방법>
// 1. participant를 순회하며 map<선수 이름: 명 수>을 채운다.
// 2. completion을 순회하며 map<선수 이름: 명 수>에서 "명 수"를 -1 한다.
//      -1을 한 뒤 "명 수"가 0이 되면 해당 요소를 map에서 삭제한다.
// 3. map을 순회하며 가장 처음 잡힌 요소를 반환한다.

// 1.
// for (const p of participant) {
//      count = map.get(p) || 0
//      count += 1
//      map.put(p, count)
// }

// 2.
// for (const c of completion) {
//      count = map.get(c)
//      if (count === 1):
//          map.delete(c)
//      else 
//          map.put(c. count - 1)
// }

// 3.
// for (const key of map) {
//      return map.get(key)
// }
// return ""
function solution(participant, completion) {
    const map = new Map();
    // 1.
    for (const p of participant) {
        count = map.get(p) || 0;
        count += 1;
        map.set(p, count);
    }
    // 2.
    for (const c of completion) {
        count = map.get(c);
        count -= 1
        if (count <= 0) {
            map.delete(c)
        } else {
            map.set(c, count)
        }
    }
    // 3.
    for (const [key, value] of map.entries()) {
        return key;
    }
    return "";
}