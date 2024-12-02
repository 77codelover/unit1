def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            return True
        else:
            False

list = [1,2,'Harsh',-1,8,9]
n = 'Harsh'
if search(list,n):
    print("Harsh")
else:
    print("NO")