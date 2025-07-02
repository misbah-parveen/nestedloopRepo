#nested loop
for i in range (1,4):         
    for j in range (1,5):     
        # Code block inside inner loop
        print(f"i={i}, j={j}")

#break statment
for m in range(1, 6):
    if m == 3:
        break
    print(m)

#continue Statement
for m in range(1, 6):
    if m == 3:
        continue
    print(m)
