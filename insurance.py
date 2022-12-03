a=input("Enter your gender (M/F): ")
b=int(input("Enter the price of the car you drive: "))
if a=='M':
    age=int(input("Please enter your age: "))
    if age<=23:
        print("Insurance: ",((23/100)*b))
    else:
        print("Insurance: ",((9/100)*b))
if a=='F':
    d=input("Please enter, for sports car(sc) ,for non sport car(nsc):")
    if d=='sc':
        print("Insurance: ",((21/100)*b))
    else:
        print("Insurance: ",((10/100)*b))
else:
    print("You are mad")
