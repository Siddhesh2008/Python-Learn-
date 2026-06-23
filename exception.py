#exception= An event that that interrupts the flow of aa program 
#           (zerodivisionerror,typeerror,valuerror)
#           1.try , 2.except, 3.finally            

try:
    number=int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("You must enter a number")
except:
    print("Something went wrong")
finally:
    print("This will always execute")