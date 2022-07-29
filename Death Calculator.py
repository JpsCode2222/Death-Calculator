print("Death Calculator")
Age = 90
A = int(input("Enter your Age: "))
if A < Age:
    print(f"Years:{Age-A}  Months:{(Age-A)*12}  Weeks:{(Age-A)*52}")
else:
    print("Person is Dead")
