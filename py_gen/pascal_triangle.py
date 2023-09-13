def create_pascal_triangle(level):
    counter = 1
    head = [1]
    upper_lvl = head
    pascal_triangle = []
    pascal_triangle.append(head)
    while level > 0:
        temp_arr = [head[0]]
        t = counter
        i =0
        while t - 1 > 0:
            temp_arr.append(upper_lvl[i] + upper_lvl[i+1])
            i += 1
            t -= 1
        temp_arr.append(1)
        pascal_triangle.append(temp_arr)
        upper_lvl = temp_arr
        counter += 1
        level -= 1
    return pascal_triangle

def n_level():
    level = int(input())
    print(create_pascal_triangle(level)[-1])

def pascal_triangle():
    level = int(input()) - 1
    output = ""
    p_t = create_pascal_triangle(level)
    for i in p_t:
        output += " ".join(list(map(str,i))) +"\n"
    print(output)

pascal_triangle()