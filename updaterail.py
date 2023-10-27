import csv

def write(info):
    with open("data.csv","a") as csv_file:
        write=csv.writer(csv_file)
        write.writerow(info)

def read():
    with open("data.csv","r") as csv_file:
        read=csv.reader(csv_file)
        for rows in read:
            print(rows)

def city_enter():
    try:
        x=int(input("Select the city you want to visit from Rawalpindi :"))
        return x
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return city_enter()   

def bogie_enter():
    try:
        y=int(input("Select the Bogie please :"))
        return y
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return bogie_enter() 

def main():
    L_seat_limits = {
        "Executive Class": 30,
        "Lower A/C Bogie": 50,
        "Economy Class": 100,
        "First Class Sleeper": 40,
        "Economy Sleeper": 40
    }
    K_seat_limits = {
        "Executive Class": 20,
        "Lower A/C Bogie": 40,
        "Economy Class": 80,
        "First Class Sleeper": 50,
        "Economy Sleeper": 60
    }
    Q_seat_limits = {
        "Executive Class": 40,
        "Lower A/C Bogie": 60,
        "Economy Class": 50,
        "First Class Sleeper": 70,
        "Economy Sleeper": 30
    }
    seat_remaining = {
        "Executive Class": 30,
        "Lower A/C Bogie": 50,
        "Economy Class": 100,
        "First Class Sleeper": 40,
        "Economy Sleeper": 40
    }
    cities=["none","Lahore","Karachi","Quetta"]
    bogies=["none","Executive Class","Lower A/C Bogie","Economy Class","First Class Sleeper","Economy Sleeper"]

    while True:
        print("        WELCOME TO OUR PLATFORM")
        print("Press 1 for booking tickets")
        print("Press 2 for checking previous records")
        print("Press 3 for exit")
        key=int(input("Enter a number of key : ")) 
        if (key==1):
            name=str(input("Enter your name : "))
            print("1. Lahore")
            print("2. Karachi")
            print("3. Quetta")
            city=int(city_enter())
            if (city==1):
                print("You have selected to visit Lahore")
                print("1. Executive Class , price 1500 per person")
                print("2. Lower A/C Bogie ,  price 800 per person")
                print("3. Economy Class Bogie ,  price 1000 per person")
                bogie_class=int(bogie_enter())
                if (bogie_class==1):
                    bogie = "Executive Class"
                    price = 4000
                elif (bogie_class==2):
                    bogie = "Lower A/C Bogie"
                    price = 2500
                elif (bogie_class==3):
                    bogie = "Economy Class"
                    price = 1500
                else:
                    print("Invalid Bogie selection")
                    continue
                seat_limit = L_seat_limits[bogie]
                tickets=int(input("Enter number of seats you want: "))
                if (tickets > seat_limit):
                    print("Sorry, only {} seats are available in {} bogie.".format(L_seat_limits, bogie))
                    continue
                remaining_tic=seat_limit-tickets
                print("Remaining seats are: ",remaining_tic)
                if bogie_class==1:
                     L_seat_limits.update({"Executive Class": remaining_tic })
                elif bogie_class==2:
                     L_seat_limits.update({"Lower A/C Bogie": remaining_tic })
                elif bogie_class==3:
                     L_seat_limits.update({"Economy Class": remaining_tic })
                else:
                  continue
                tax=((price*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(price*tickets)+tax
                print("Your total bill is : ",bill)
                write([name,city,bogie,tickets,bill])
                print("Your tickets has been booked.")
            elif (city==2):
                print("You have selected to visit Karachi.")
                print("1. Executive Class , price 8000 per person")
                print("2. Lower A/C Bogie , price 2000 per person")
                print("3. Economy Class Bogie , price 3000 per person")
                print("4. First Class Sleeper bogie, 4500 per person")
                print("5. Economy Sleeper Bogie, price 6000 per person")
                bogie_class=int(bogie_enter())
                if (bogie_class==1):
                    bogie = "Executive Class"
                    price = 8000
                elif (bogie_class==2):
                    bogie = "Lower A/C Bogie"
                    price = 2000
                elif (bogie_class==3):
                    bogie = "Economy Class"
                    price = 3000
                elif (bogie_class==4):
                    bogie = "First Class Sleeper"
                    price = 4500
                elif (bogie_class==5):
                    bogie = "Economy Sleeper"
                    price = 6000
                else:
                    print("Invalid Bogie selection")
                    continue
                seat_limit = K_seat_limits[bogie]
                tickets=int(input("Enter number of seats you want : "))
                if tickets > seat_limit:
                    print("Sorry, only {} seats are available in {} bogie.".format(K_seat_limits, bogie))
                    continue
                remaining_tic=seat_limit-tickets
                print("Remaining seats are: ",remaining_tic)
                if bogie_class==1:
                     K_seat_limits.update({"Executive Class": remaining_tic })
                elif bogie_class==2:
                     K_seat_limits.update({"Lower A/C Bogie": remaining_tic })
                elif bogie_class==3:
                     K_seat_limits.update({"Economy Class": remaining_tic })
                elif bogie_class==4:
                     K_seat_limits.update({"First Class Sleeper": remaining_tic })
                elif bogie_class==5:
                     K_seat_limits.update({"Economy Sleeper": remaining_tic })
                else:
                  continue
                tax=((price*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(price*tickets)+tax
                print("Your total bill is : ",bill)
                write([name,city,bogie,tickets,bill])
                print("Your tickets has been booked.")
            elif (city==3):
                print("You have selected to visit Quetta")
                print("1. Executive Class , price 8000 per person")
                print("2. Lower A/C Bogie , price 2000 per person")
                print("3. Economy Class Bogie , price 3000 per person")
                bogie_class=int(bogie_enter())
                if (bogie_class==1):
                    bogie = "Executive Class"
                    price = 5000
                elif (bogie_class==2):
                    bogie = "Lower A/C Bogie"
                    price = 2500
                elif (bogie_class==3):
                    bogie = "Economy Class"
                    price = 2000
                else:
                    print("Invalid Bogie selection")
                    continue
                seat_limit = Q_seat_limits[bogie]
                tickets=int(input("Enter number of seats you want : "))
                print("Remaining seats are: ",seat_limit-tickets)
                if tickets > seat_limit:
                    print("Sorry, only {} seats are available in {} bogie.".format(Q_seat_limits, bogie))
                    continue
                remaining_tic=seat_limit-tickets
                if bogie_class==1:
                     Q_seat_limits.update({"Executive Class": remaining_tic })
                elif bogie_class==2:
                     Q_seat_limits.update({"Lower A/C Bogie": remaining_tic })
                elif bogie_class==3:
                     Q_seat_limits.update({"Economy Class": remaining_tic })
                else:
                  continue
                tax=((price*tickets)/100)*15
                print("Government tax is : ",tax)
                bill=(price*tickets)+tax
                print("Your total bill is : ",bill)
                write([name,city,bogie,tickets,bill])
                print("Your tickets has been booked.")
            else:
                print("Invalid City selection")
        elif (key==2):
            read()
        elif (key==3):
            print("Thanks for visiting our platform")
            break
        else:
            print("Invalid Key selection")
main()