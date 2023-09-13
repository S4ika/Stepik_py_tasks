def create_pascal_triangle():
    level = int(input())
    counter = 1
    head = [1]
    upper_lvl = head
    while level > 0:
        temp_arr = [head[0]]
        t = counter
        i =0
        while t - 1 > 0:
            temp_arr.append(upper_lvl[i] + upper_lvl[i+1])
            i += 1
            t -= 1
        temp_arr.append(1)
        upper_lvl = temp_arr
        counter += 1
        level -= 1
    print(upper_lvl)