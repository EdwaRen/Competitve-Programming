
def stars(num_stars):
    if num_stars <= 0:
        return

    print('*'*num_stars, sep='')
    stars(num_stars-1)
    print('*'*num_stars, sep='')

def sumListPos_rec(lst, lst_length):
    if lst_length-1 < 0:
        return 0
    cur_max = max(lst[lst_length-1], 0)
    return cur_max + sumListPos_rec(lst, lst_length-1)

stars(4)

lst = [1, -2, 5, 0 , -5]
z = sumListPos_rec(lst, len(lst))
print(z)
