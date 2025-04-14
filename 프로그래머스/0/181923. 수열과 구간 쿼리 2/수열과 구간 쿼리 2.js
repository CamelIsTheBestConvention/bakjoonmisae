function solution(arr, queries) {
    const result = queries.map(([s,e,k]) => {
        const list = arr.slice(s, e + 1).filter(num => num > k);
        return list.length > 0 ? Math.min(...list) : -1;
    })
    
    return result;
}