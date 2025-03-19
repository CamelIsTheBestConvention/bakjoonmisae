function solution(sizes) {
    let maxWidth = 0;
    let maxHeight = 0;
    
    for (let i = 0; i < sizes.length; i++) {
        let w = Math.max(sizes[i][0], sizes[i][1]);
        let h = Math.min(sizes[i][0], sizes[i][1]);
        
        maxWidth = Math.max(maxWidth, w);
        maxHeight = Math.max(maxHeight, h);
    } 
    return maxWidth * maxHeight;
}