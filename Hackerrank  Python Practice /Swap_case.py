#Link-https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    a=""
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            a=a+s[i].lower()
        elif s[i]>='a' and s[i]<='z':
            a=a+s[i].upper()
        else:
            a=a+s[i]
    return a
   
         
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
