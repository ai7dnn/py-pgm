with open("./data1.txt", "r") as f1 :
    print("-"*20)
    txt = f1.read(1)
    while txt != "" :
        print(txt, end = "")
        txt = f1.read(1)
    print("\n"+"-"*20)
