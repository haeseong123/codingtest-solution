function getDictionary(alphabet) {
    function makeDictionary(d, size) {
        if (d.length === size) {
            dictionary.push(d.join(''))
            return
        }
        
        for (let i = 0; i < alphabet.length; i++) {
            d.push(alphabet[i])
            makeDictionary(d, size)
            d.pop()
        }
    }
    
    const dictionary = []
    for (let size = 1; size < alphabet.length + 1; size++) {
        makeDictionary([], size);
    }
    return dictionary;
}

function solution(word) {
    const alphabet = ["A", "E", "I" , "O", "U"]
    
    return getDictionary(alphabet).sort().indexOf(word) + 1
}