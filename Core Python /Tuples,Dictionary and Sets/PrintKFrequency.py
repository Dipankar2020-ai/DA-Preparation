def printkfrequency(s,k):
    words=s.split()
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)
s=input()
s=printkfrequency(s,2)
