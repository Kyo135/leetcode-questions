class Solution:
    def partition(M, low, high):
        pivot = M[high]
        i = low - 1
        for j in range(low, high):
            if M[j]<=pivot:
                i+=1
                M[i], M[j] = M[j], M[i]
        M[i+1], M[high] = M[high], M[i+1]
        return i+1

    def quick(M, low, high):
        if low<high:
            p = Solution.partition(M, low, high)
            Solution.quick(M, low, p-1)
            Solution.quick(M, p+1, high)

    def dicts(L, k):    
        M = []
        N = []
        D = {}
        for item in L:
            
            if item in D:
                D[item]+=1
            else:
                D[item] = 1
        for key, value in D.items():
            print(key,"->",value)
        print(" ")    
        M = list(D.values())
        N = list(D.keys())
        D = {key: value for key, value in sorted(D.items(), key=lambda item: item[1])}
        Q = list(D.keys())[:k]        
        print(Q)
    

L= eval(input())
k = int(input("Enter k: "))
Solution.dicts(L, k)
Solution.quick(L, 0, len(L)-1)
