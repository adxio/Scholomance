def generate_numbers():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    while b == a:
        b = random.randint(0, 9)
    while c == a or c == b:
        c = random.randint(0, 9)
    while d == a or d == b or d == c:
        d = random.randint(0, 9)
    return [a,b,c,d]

if __name__ == '__main__':
    numbers = generate_numbers()
    print numbers
    result = False

    while result != True:
        user_nums = list(raw_input("input your numbers: "))
        na = 0
        nb = 0
        if int(user_nums[0]) in numbers:
            na += 1
            if numbers[0] == int(user_nums[0]):
                nb += 1
        if int(user_nums[1]) in numbers:
            na += 1
            if numbers[1] == int(user_nums[1]):
                nb += 1
        if int(user_nums[2]) in numbers:
            na += 1
            if numbers[2] == int(user_nums[2]):
                nb += 1
        if int(user_nums[3]) in numbers:
            na += 1
            if numbers[3] == int(user_nums[3]):
                nb += 1
        if nb == 4:
            result = True
        else:
            print "A:%s,B:%s" % (na, nb)

    print "SUCCESS!"
    