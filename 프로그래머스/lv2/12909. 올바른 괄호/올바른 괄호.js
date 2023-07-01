function solution(s){
    const stack = [];
    for (const c of s) {
        if (c === "(") {
            stack.push("(");
        } else {
            if (stack[stack.length - 1] === "(") {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    
    return stack.length === 0 ? true : false;
}