// <문제 설명>
// 명령어	           수신 탑(높이)
// I 숫자	       큐에 주어진 숫자를 삽입합니다.
// D 1	        큐에서 최댓값을 삭제합니다.
// D -1	        큐에서 최솟값을 삭제합니다.

// 아래 매개변수가 주어질 때 모든 연산 후 큐가 비어있으면 [0, 0] 비어있지 않으면 [최댓값, 최솟값]을 반환해 주세요.
// operations: 이중 우선순위 큐가 할 연산

// <제한사항>
// operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
// operations의 원소는 큐가 수행할 연산을 나타냅니다.
//      원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
// 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

// <문제 풀이>
// 배열을 선업합니다. 해당 배열은 오름차순 정렬되어 있습니다.
// 값 삽입 시 이분 탐색을 활용하여 삽입 합니다.
// 최솟값 삭제 시 pop(0) 합니다.
// 최댓값 삭제 시 pop() 합니다.
function binaryPush(arr, value) {
    // 중간 인덱스를 찾습니다.
    // 중간 인덱스에 해당되는 값보다 크면 start를 mid로 바꿉니다.
    // 중간 인덱스에 해당되는 값보다 작으면 end를 mid로 바꿉니다.
    // 중간 인덱스에 해당되는 값과 같으면 해당 인덱스를 반환합니다.
    let insertIndex = -1;
    let left = 0,
        right = arr.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] === value) {
            insertIndex = mid;
            break;
        } else if (arr[mid] < value) {
            left = mid + 1;
        } else {
            right = mid - 1;
            insertIndex = mid;
        }
    }

    if (insertIndex === -1) {
        insertIndex = left;
    }

    arr.splice(insertIndex, 0, value);
}

function solution(operations) {
    arr = []
    for (const o of operations) {
        [command, value] = o.split(' ');
        if (command === 'I') {
            binaryPush(arr, Number(value));
        } else {
            if (arr.length === 0) continue;

            if (value === '1') {
                arr.pop();
            } else {
                arr.shift();
            }
        }
    }
    return (arr.length >= 2) ? [arr[arr.length - 1], arr[0]] : [0, 0]
}
