word = input()
letter = input()

result = -1
for i in range(len(word)):
    if word[i] == letter:
        result=i 
        break
    
print(result)



