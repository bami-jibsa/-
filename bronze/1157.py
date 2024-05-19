word = input().upper()
ls_word = list(set(word))

cnt = []
for i in ls_word:
    cnt.append(word.count(i))
    
if cnt.count(max(cnt)) > 1:
    print("?")
    
else:
    print(ls_word[(cnt.index(max(cnt)))])