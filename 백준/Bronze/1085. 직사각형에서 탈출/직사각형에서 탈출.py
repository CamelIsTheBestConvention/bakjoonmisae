x, y, w, h = map(int, input().split())
minValue = min(min(x,y), min(w-x, h-y))
print(minValue)