str=input()
freq={}
for char in str:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1 
max_char=max(freq,key=freq.get)
print(max_char)
