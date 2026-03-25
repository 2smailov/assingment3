def printString(S, N):

    plaintext = [None] * 5
 
    f = [0] * 26

    fs = [None] * 26
    
    u = [0] * 26
    
    for i in range(N):
        if S[i] != ' ':
            f[ord(S[i]) - 65] += 1
            
    for i in range(26):
        fs[i] = f[i]
          
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    
    fs.sort(reverse = True)
    
    for i in range(5):
        ch = -1
        
        for j in range(26):
            if fs[i] == f[j] and u[j] == 0:
                u[j] = 1
                ch = j
                break
            
        if ch == -1:
            break
         
        x = ord(T[i]) - 65
        
        x = x - ch
        
        curr = ""
        
        for k in range(N):
            
            if S[k] == ' ':
                curr += " "
                continue
             
            y = ord(S[k]) - 65
            y += x
            
            if y < 0:
                y += 26
            if y > 25:
                y -= 26
    
            curr += chr(y + 65)
            
        plaintext[i] = curr
    
    for i in range(5):
        print(plaintext[i])
 
S = "B TJNQMF NFTTBHF"
N = len(S)
printString(S, N)

