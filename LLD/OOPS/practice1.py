class Movie:
    def __init__(self,movie_name:str,total_seats:int,ticket_price:int):
        self.movie_name=movie_name
        self.total_seats=total_seats
        self.ticket_price=ticket_price
        self.booked_seats=0


    def book_tickets(self,num_tickets:int)->None:

        if self.total_seats - self.booked_seats>=num_tickets:
            print(f"Tickets Reserved for {num_tickets}.Please pay {num_tickets*self.ticket_price} for confirmation")
            self.booked_seats+=num_tickets

        else:
            print("Sorry not enough seats available")

    def show_status(self):
        print(f"Movie : {self.movie_name} \n\n Seats_ Available : {self.total_seats - self.booked_seats} \n\n  seats_booked:{self.booked_seats}")            
