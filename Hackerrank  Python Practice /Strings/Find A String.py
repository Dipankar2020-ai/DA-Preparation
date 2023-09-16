#Link->https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
def count_substring(string, sub_string):
    length=len(string)
    length1=len(sub_string)
    count=0
    for i in range(0,length-length1+1):
        if string[i:i+length1]==sub_string:
            
        
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_s
