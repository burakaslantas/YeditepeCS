n = 17
blank = int((2*n + n-1)/2)
def s_num(i):
    star_num = 9
    c_line= str()
    for j in range(1, i-1, 2):
        star_num += j
    for k in range(i):
        star_num += 1
        c_line += str(star_num) + " "
    return c_line

for i in range(1, n+1, 2):
    print(" "*blank + str(s_num(i)))
    blank -= (1 + 2)
    print("\n", end='')