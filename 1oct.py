prices = [7,2,1,3,6,4]
n=len(prices)-1
a=prices[0]
b=prices[n]
mini=max(prices)
maxi=0
i=0
while i<n:
    if a>b:
        i+=1
        a=prices[i]
        print('i=',a)
        mini=min(prices[i],mini)
        print('mini=',mini)
    else:
        n-=1
        b=prices[n]
        print('n=',b)
        maxi=max(maxi,prices[n])
        print('maxi=',maxi)
ans=maxi-mini
print('ans=',ans)