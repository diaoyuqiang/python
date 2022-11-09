def insert_sort(li):
    for i in range(1, len(li)): # i为摸到的牌
        j = i - 1 # j为手里牌的下标
        tem = li[i]
        while j >= 0 and li[j] > tem:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tem


li = [3,2,5,14,25,6,10,8]
insert_sort(li)
print(li)

# i = 2 val = 5
# j = 1 val = 3