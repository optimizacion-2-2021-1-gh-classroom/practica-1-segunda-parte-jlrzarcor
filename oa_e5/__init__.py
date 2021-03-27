import numpy as np

def cgm(A,b,x):
    """
    A: matrix
    b: vector
    x: soluction vector
    """
    r = np.dot(A,x)-b
    p = -r
    k = 0
    
    while True: 

        r_s = np.dot(np.transpose(r),r)
        alpha_k = r_s/np.dot(np.transpose(p),np.dot(A,p))
        
        x = x + np.dot(alpha_k,p)
        
        r = r + np.dot(alpha_k, np.dot(A,p))
        
        beta = np.dot(np.transpose(r),r)/r_s
        
        p = -r + beta*p
        
        k = k+1
        #print(x)
        if np.linalg.norm(r) < 1e-10:
            break
    
    return x
    