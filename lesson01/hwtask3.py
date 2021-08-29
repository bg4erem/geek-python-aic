str_n = input("Input N: ")

int_n = int(str_n)

str_nn = str_n + str_n
int_nn = int(str_nn)

str_nnn = str_nn + str_n
int_nnn = int(str_nnn)

print(
    int_n,
    int_nn,
    int_nnn,
    int_n + int_nn + int_nnn
)