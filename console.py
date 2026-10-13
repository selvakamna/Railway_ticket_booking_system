trains={"pandiyan express" :{"tnumber":12637 ,"from":"coimbatore","to":"karaikudi","departure":"21:40","arrival":"05:40","seats":140 ,"fare":450},
        "coimbatore mail":{"tnumber":12623,"from":"coimbatore","to":"chennai","departure":"22:10","arrival":"06:20","seats":100,"fare":520},
        "karnataka express":{"tnumber":12627,"from":"coimbatore","to":"bengalure","departure":"23:30","arrival":"05:45","seats":170 , "fare":300},
        "guruvayur express":{"tnumber":16127,"from":"coimbatore","to":"trichy","departure":"22:30","arrival":"05:30","seats":110,"fare":350}}
d_user_name=["admin"]
d_password=["admin123"]
pessenger_name = input("enter pessenger name:")
pessenger_email = input("enter pessenger email:")
pessenger_mobile = input("enter pessenger mobile:")
pessenger_age = int(input("enter pessenger age:"))
pessenger_gender = (input("enter pessenger gender:"))
PNR = 100000
bookings ={}

def user_registration():
        your_username=input("Enter your username: ")
        your_password=input("Enter your password: ")
        d_user_name.append(your_username)
        d_password.append(your_password)
        print("Your username has been registered!")
        print("-------------- thanks for ur registeration------------")
def login():
    username = input("enter username:")
    password = input("enter password:")
    if username not in d_user_name and password not in d_password:
        print("login unsuccessful")
        print("---------------- Register Yours!------------")
    else:
        print("login successful")

def traindetails():
    print("------------- available trains --------------")
    for a,b in trains.items():
        print(f"{a}:{b}")
def trainbooking():
    global PNR
    train_name=input("enter train name:")
    if train_name in trains:
        print(f"{train_name}:{trains[train_name]}")
        no_of_seats=int(input("enter number of seats:"))
        PNR=100000

        if  trains[train_name]["seats"]>0 and trains[train_name]["seats"]>= no_of_seats:
            trains[train_name]["seats"]-=no_of_seats
            trains[train_name]["fare"]*=no_of_seats
            PNR+=1
            bookings[PNR] = {
                "train_name": train_name,
                "seats": no_of_seats,
                "fare": trains[train_name]["fare"] * no_of_seats
            }

            print("--------------- ticket booked successfully! --------------")
            print("--------------- ticket details ---------------")
            print(f"PNR:{PNR}")
            print(f"train name:{train_name}")
            print(f"train no:{trains[train_name]["tnumber"]}")
            print(f"ticket fare:{trains[train_name]["fare"]}")
            print(f"remaining seats:{trains[train_name]["seats"]}")
        else:
            print("sorry unavailable seats")
    else:
        print("---------------oops! invalid train name ------------------")


def cancellation():
        PNR = int(input("Enter PNR number: "))

        if PNR in bookings:
            train_name = bookings[PNR]["train_name"]
            seats = bookings[PNR]["seats"]

            trains[train_name]["seats"] += seats

            del bookings[PNR]

            print("Ticket cancelled successfully!")
            print(f"Train name: {train_name}")
            print(f"Cancelled seats: {seats}")
            print(f"Remaining seats: {trains[train_name]['seats']}")

        else:
            print("Invalid PNR! No booking found.")
def seatsavailablity():
    s_train_name=input("enter train name:")
    if s_train_name in trains:
        print(f"{trains[s_train_name]} have {trains[s_train_name]["seats"]} seats")
    else:
        print("----------------- oops! invalid train name-------------------")

def pessengerdetails():
    print("pessenger details:")
    print(f"PNR:{PNR}")
    print(f"pessenger name:{pessenger_name}")
    print(f"pessenger email:{pessenger_email}")
    print(f"pessenger mobile:{pessenger_mobile}")
    print(f"pessenger age:{pessenger_age}")
    print(f"pessenger gender:{pessenger_gender}")

while True:
    print("1.userregisteration")
    print("2.login")
    print("3.traindetails")
    print("4.trainbooking")
    print("5.cancellation")
    print("6.seatsavailablity")
    print("7.pessengerdetails")
    print("8.exit")
    num=int(input("enter number:"))

    if num==1:
        u=user_registration()
    elif num==2:
        l=login()
    elif num==3:
        t=traindetails()
    elif num==4:
        t2=trainbooking()
    elif num==5:
        c=cancellation()
    elif num==6:
        s=seatsavailablity()
    elif num==7:
        p=pessengerdetails()
    elif num==8:
        exit()

    print("--------------- thanks for ur time ----------------")







