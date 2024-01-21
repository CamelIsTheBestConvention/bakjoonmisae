import sys
sys.setrecursionlimit(10**9)

preorder_arr = []

while True:
    try:
        preorder_arr.append(int(sys.stdin.readline().rstrip()))
    except:
        break

def postorder(root_idx, end_idx):
    if root_idx > end_idx:
        return
    
    global preorder_arr
    
    right_start = end_idx + 1

    for i in range(root_idx + 1, end_idx + 1):
        if preorder_arr[root_idx] < preorder_arr[i]:
            right_start = i
            break
    
    postorder(root_idx + 1, right_start - 1)

    postorder(right_start, end_idx)

    print(preorder_arr[root_idx])


postorder(0, len(preorder_arr) - 1)