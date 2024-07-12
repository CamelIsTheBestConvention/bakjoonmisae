def build_tree(nodes, depth, levels, current_level=0):
    if not nodes:
        return
    
    mid = len(nodes) // 2
    levels[current_level].append(nodes[mid])
    
    build_tree(nodes[:mid], depth, levels, current_level + 1)
    build_tree(nodes[mid + 1:], depth, levels, current_level + 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    K = int(data[0])
    nodes = list(map(int, data[1:]))
    
    levels = [[] for _ in range(K)]
    build_tree(nodes, K, levels)
    
    for level in levels:
        print(' '.join(map(str, level)))

if __name__ == "__main__":
    main()
