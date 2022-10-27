# try:
#     num1 = int(input("Enter the 1st number: "))
#     num2 = int(input("Enter the 2nd number: "))
#     result = num1 / num2
#     print(result)
# except (ValueError, ZeroDivisionError):
#     print("Incorrect Input")
# finally:
#     print("Thanks!!")

def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"
try:
    print(voter(17))
except ValueError as e:
    print(e)