// 현재 시간을 기준으로 가장 빨리 끝나는 작업을 먼저 처리한다.
class Heap {
    constructor(comparator) {
        this.heap = [];
        this.comparator = comparator;
    }

    getLeftChildIndex(parentIndex) {
        return 2 * parentIndex + 1;
    }

    getRightChildIndex(parentIndex) {
        return 2 * parentIndex + 2;
    }

    getParentIndex(childIndex) {
        return Math.floor((childIndex - 1) / 2);
    }

    hasLeftChild(index) {
        return this.getLeftChildIndex(index) < this.heap.length;
    }

    hasRightChild(index) {
        return this.getRightChildIndex(index) < this.heap.length;
    }

    hasParent(index) {
        return this.getParentIndex(index) >= 0;
    }

    leftChild(index) {
        return this.heap[this.getLeftChildIndex(index)];
    }

    rightChild(index) {
        return this.heap[this.getRightChildIndex(index)];
    }

    parent(index) {
        return this.heap[this.getParentIndex(index)];
    }

    swap(index1, index2) {
        const temp = this.heap[index1];
        this.heap[index1] = this.heap[index2];
        this.heap[index2] = temp;
    }

    peek() {
        if (this.heap.length === 0) {
            return null;
        }
        return this.heap[0];
    }

    poll() {
        if (this.heap.length === 0) {
            return null;
        }
        if (this.heap.length === 1) {
            return this.heap.pop();
        }
        const item = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown();
        return item;
    }

    add(item) {
        this.heap.push(item);
        this.heapifyUp();
    }

    heapifyUp() {
        let index = this.heap.length - 1;
        while (this.hasParent(index) && this.comparator(this.parent(index), this.heap[index]) > 0) {
            const parentIndex = this.getParentIndex(index);
            this.swap(parentIndex, index);
            index = parentIndex;
        }
    }

    heapifyDown() {
        let index = 0;
        while (this.hasLeftChild(index)) {
            let smallerChildIndex = this.getLeftChildIndex(index);
            if (
                this.hasRightChild(index) &&
                this.comparator(this.rightChild(index), this.leftChild(index)) < 0
            ) {
                smallerChildIndex = this.getRightChildIndex(index);
            }

            if (this.comparator(this.heap[index], this.heap[smallerChildIndex]) <= 0) {
                break;
            } else {
                this.swap(index, smallerChildIndex);
            }

            index = smallerChildIndex;
        }
    }
    size() {
        return this.heap.length;
    }
}

function solution(jobs) {
    jobs.sort((a, b) => {
        if (a[0] < b[0]) return -1;
        else if (a[0] == b[0]) return 0;
        else return 1;
    });
    const heap = new Heap((a, b) => {
        if (a[1] < b[1]) return -1;
        else if (a[1] === b[1]) return 0;
        else return 1;
    });
    let answer = 0;
    let time = 0;
    let cursor = 0;
    while (cursor < jobs.length || heap.size()) {
        while (cursor < jobs.length) {
            if (jobs[cursor][0] <= time) {
                heap.add(jobs[cursor])
                cursor += 1;
            } else {
                break
            }
        }
        
        if (heap.size()) {
            // 실행할 수 있는 작업 중 가장 빨리 끝나는 작업을 먼저 실행합니다.
            const job = heap.poll();
            answer += time - job[0] + job[1];
            time += job[1];
        } else {
            time += 1
        }
    }

    return Math.floor(answer / jobs.length);
}