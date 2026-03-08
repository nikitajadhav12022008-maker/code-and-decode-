#python based coder and decoder:
#input whether you want to code or decode
n = input("do you want to coding or decoding:")
#conditions
if(n == "coding"):
    n1 = input("enter a messege to code:")
    n2 = n1.split()
    for i in n2:
        if(len(i) <= 3):
            print(i[::1],end = " ")
        else:
            print("ght"+i[1:]+i[0]+"jhk",end = " ")
else:
    n1 = input("enter a messege to decode:")
    n2 = n1.split()
    for i in n2:
        if(len(i) <= 3):
            print(i[::i],end = " ")
        else:
            print(i[-4]+i[3:-4],end = " ")

