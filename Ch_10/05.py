
# booking cancel challange remaining


class Train:
    service = "Booking"
    seatsBooked = None

    def __init__(self, trainNo, seats, fare):
        self.trainNo = trainNo
        self.seats = seats
        self.fare = fare

    def seatsEnquiry(self):
        if self.seats > 0:
            print(f"{self.seats} seats are available in Train No. {self.trainNo}")
        else:
            print("Sorry no seats are available")

    def fareEnquiry(self):
        if self.seats > 0:
            print(f"Booking Price per seat is {self.fare}")
        else:
            pass

    def bookTicket(self):

        if self.seats > 0:
            print(f"Do you want to book ticket ?")
            confirm = input("Enter Y / N \n")
            if confirm == "Y":
                Train.seatsBooked = int(
                    input("Enter the number of seats you want to book : "))
                if Train.seatsBooked <= self.seats:
                    print(
                        f"Your {Train.seatsBooked} seats are booked for Train No. {self.trainNo} and your total fare is ₹{Train.seatsBooked*self.fare}")
                else:
                    print(f"Only {self.seats} seats are available.")
            else:
                pass

            self.seats = self.seats - Train.seatsBooked

        else:
            pass

    def newStatus(self):
        print(
            f"Numnber of seats remaining in Train No. {self.trainNo} is {self.seats}")


whichTrain = Train(21070, 10, 250)
whichTrain.seatsEnquiry()
whichTrain.fareEnquiry()
whichTrain.bookTicket()
whichTrain.newStatus()
whichTrain.bookTicket()
