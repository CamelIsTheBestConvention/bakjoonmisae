def backpack():
    n, k = map(int, input().split())
    item = [list(map(int, input().split())) for _ in range(n)]

    max_value_bag = {0:0}
    max_firth_wv = sorted(item, reverse=True)

    for w, v in max_firth_wv:
        backpack = {}
        for _v, _w in max_value_bag.items():
            w_if_added = _w + w
            v_if_added = _v + v
            
            if w_if_added < max_value_bag.get(v_if_added, k + 1):
                backpack[v_if_added] = w_if_added

        max_value_bag.update(backpack)
    return max(max_value_bag.keys())

print(backpack())