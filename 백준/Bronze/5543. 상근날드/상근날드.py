import sys
input = sys.stdin.readline

hambuger = []
drink = []

for i in range(3):
    hambuger.append(int(input()))
    
for i in range(2):
    drink.append(int(input()))
    
print((min(hambuger) + min(drink))-50)
    
  
    