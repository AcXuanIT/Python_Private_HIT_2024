

def Binary_Search(x , list, left, right):
    if left > right:
        return -1
    
    mid = int((left + right)/2)

    if list[mid] == x :
        return mid
    elif list[mid] > x:
        return Binary_Search(x, list, left, mid)
    else:
        return Binary_Search(x, list, mid+1, right)
    

list = [1,2,3,4,5,6,7,8,9,10]
x = 11

print(f"i = {Binary_Search(x,list,0,len(list)-1)}")
