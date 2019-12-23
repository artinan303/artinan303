while 1 == 1:
    print("type end to end program")
    string = input("Insert Aromatic String Here: ")
    romanNums = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
    Arr1 = []
    Arr2 = []
    Arr3 = []
    total = 0
    if string.count("n") > 0:
        exit()
    if len(string) % 2 == 0:
        for i in string:
            try:
                Arr1.append(int(i))
            except ValueError:
                for x in romanNums:
                    if x == i:
                        i = romanNums[x]
                        Arr2.append(i)
        for i in range(len(Arr1)):
            Arr3.append(Arr1[i]*Arr2[i])
        for i in Arr3:
            total += i
        print(Arr3)
        print(total)
