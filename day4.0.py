# naive algorithm for pattern searching
def search(pat, txt): 
    M = len(pat) 
    N = len(txt) 

    for i in range(N - M + 1): 
        j = 0 
        for j in range(0, M): 
            if (txt[i + j] != pat[j]): 
                break
  
        if (j == M - 1):  
            print("Pattern found at index ", i) 
  
# Driver Code 
if __name__ == '__main__': 
    txt = "AABAACAADABABABAABAA"
    pat = "AABA"
    search(pat, txt) 