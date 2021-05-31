def delete_nth(order, max_e):
    sum_1 = 0
    x = 0
    y = 0
    while x < len(order):
        if order.count(order[x]) > max_e:
            while y < len(order):
                if order[x] == order[y]:
                    sum_1 += 1
                    if sum_1 > max_e:
                        del order[y]
                        y -= 1
                y += 1
        sum_1 = 0
        y = 0
        x += 1
    return order


print(delete_nth([30, 48, 39, 49, 49, 30, 45, 45, 22, 39, 30, 22, 48, 49, 45, 7, 45, 30, 49, 30, 49, 45, 22, 39, 30, 30, 48, 22, 7, 30, 7, 39, 49, 7, 41, 41, 39, 48, 41, 49, 30, 30, 22, 30, 30, 30, 22, 45, 22, 30, 41, 41, 45, 45, 45, 39, 7, 48, 22, 39, 39, 49, 45],1))
