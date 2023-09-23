import string, random
list1 = []
s0 = string.ascii_lowercase
s1 = string.ascii_uppercase
s2 = string.digits
s3 = string.punctuation
while True:
    print("***** Welcome to Codsoft Password Generator *****")
    print(" "*5 + "1)- Generate a new Password")
    print(" "*5 + "2)- Exit")
    z = input("Enter choice: ")
    if z not in ["1","2"]:
        print("Invalid choice!")
        p = input("<--Press Enter-->")
        continue
    if z == "1":
        while True:
            try:
                plen = int(input("Enter length of password: "))
                if plen <= 0:
                    print("Invalid input! Enter positive non zero value")
                    p = input("<--Press Enter-->")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter 'integer' value")
                p = input("<--Press Enter-->")
                continue
        while True:
            try:
                while True:
                    y = '''Select Password Complexity:
1)- Weak
2)- Moderate
3)- Strong'''
                    print(y)
                    compx = int(input("Enter choice: "))
                    if compx == 1:
                        list1.extend(s0)
                        break
                    elif compx == 2:
                        list1.extend(s0)
                        list1.extend(s1)
                        list1.extend(s2)
                        break
                    elif compx == 3:
                        list1.extend(s0)
                        list1.extend(s1)
                        list1.extend(s2)
                        list1.extend(s3)
                        break
                    else:
                        print("Invalid choice! Enter 'integer' value of corresponding choice")
                        p = input("<--Press Enter-->")
                        continue
                break    
            except ValueError:
                print("Invalid input! Enter 'integer' value of corresponding choice")
                p = input("<--Press Enter-->")
                continue
        password = "".join(random.sample(list1, plen))
        print("Generated password is: ", password, sep = "\n")
        p = input("<--Press Enter-->")
    else:
        break 