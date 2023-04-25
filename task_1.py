
def multiplicate(A):
    product_all_numbers = 1
    count_zero = 0
    for j in A:
        if j != 0:
            product_all_numbers *= j
        else:
            count_zero += 1

    print(product_all_numbers)

    lst2 = []
    for i in A:
        if i != 0 and count_zero==0:
            lst2.append(product_all_numbers / i)
        elif i == 0 and count_zero==1:
            lst2.append(product_all_numbers)
        else:
            lst2.append(0)

    return lst2



if __name__ == "__main__":

    input_arr = []
    while len(input_arr) == 0:
        input_arr = [int(i) for i in input("Введите целые значения массива ").split()]
        if len(input_arr) == 0:
            print("Пустой массив, введите снова")

    # print(input_arr)
    # print(type(input_arr))

    out_res = multiplicate(input_arr)
    print(out_res)



