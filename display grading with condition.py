def grading():

    while True:
        try:
            subject1 = int(input("enter marks of subject1:"))
            subject2 = int (input ( "enter marks of subject2 :"))
            subject3 = int (input ( "enter mark of subject3 :"))
            subject4 = int (input ( "enter mark of subject4 :" ))
            subject5 = int (input ( "enter marks of subject5 :"))
        except ValueError:
            print("enter a valid number")
            continue
        average = (subject1+subject2+subject3+subject4+subject5)/5
        if average<50:
            print("grade C")
        elif average>50 and average<65:
            print(" Your Grade is B")
        elif average>65 and average<75:
            print(" Your Grade is A")
        elif average>75:
            print("Your are Honored")

        break

grading()







