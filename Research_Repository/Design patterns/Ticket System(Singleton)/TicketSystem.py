from enum import Enum


# An enum to represent the status of a ticket
class TicketStatus(Enum):
    OPEN = "Open"
    CLOSED = "Closed"
    REOPENED = "Reopened"


# Ticket class deal with the properties and behaviour of an individual ticket
class Ticket:
    # Class variables to assign ticket numbers from 2000
    ticket_counter = 2001
    # Class variables to track all tickets
    tickets = []

    # Initializes ticket instance containing common ticket information
    def __init__(self, staff_id, creator, email, description):
        # Set initial values for a new ticket
        self.staff_id = staff_id
        self.creator = creator
        self.email = email
        self.description = description
        self.response = "Not Yet Provided."
        # self.status = "Open"
        self.status = TicketStatus.OPEN  # Use TicketStatus enum for status
        self.ticket_num = Ticket.ticket_counter
        Ticket.ticket_counter += 1

    # Define change_password function to generate the new password with the first two characters of the staffID
    # followed by the first three characters of the ticket creator
    # for a 'Password Change' request and update status to closed
    def change_password(self):
        if "Password Change" in self.description:
            # Generate a new password
            new_password = self.staff_id[:2] + self.creator[:3]
            # Display a new password to the user
            self.response = "Your new password is: " + new_password
            # Update status
            # self.status = "Closed"
            self.status = TicketStatus.CLOSED  # Use TicketStatus enum for status

    # Define update_response function to updates the response for the ticket
    def update_response(self, response):
        # Update response and change status to 'Closed' regardless of the current status
        if (
            self.status == TicketStatus.REOPENED or TicketStatus.OPEN
        ):  # Use TicketStatus enum for status
            # self.status = "Closed"
            self.status = TicketStatus.CLOSED  # Use TicketStatus enum for status

    # Define reopen_ticket function to change status to 'Reopens' when the closed ticket is reopened
    def reopen_ticket(self):
        # if self.status == "Closed":
        #     self.status = "Reopened"
        # else:
        #     self.status = "Reopened"
        if self.status == TicketStatus.CLOSED:  # Use TicketStatus enum for status
            self.status = TicketStatus.REOPENED  # Use TicketStatus enum for status

    # Define printing_ticket function to prints the details of a ticket
    def printing_ticket(self):
        # Display details of a single ticket
        print("----------------------------------------")
        print("Printing Tickets: ")
        print("Ticket Number: %d" % self.ticket_num)
        print("Ticket Creator: %s" % self.creator)
        print("Staff ID: %s" % self.staff_id)
        print("Email Address: %s" % self.email)
        print("Description: %s" % self.description)
        print("Response: %s" % self.response)
        print("Ticket Status: %s\n" % self.status.value)
        print("----------------------------------------")


# Ticket class deal with managing tickets and displaying statistics
class TicketSystem:
    _instance = None

    def __new__(cls):
        # Singleton design pattern to ensure there's only one instance of the TicketSystem
        if not cls._instance:
            cls._instance = super(TicketSystem, cls).__new__(cls)
            cls._instance.tickets = []  # Shared tickets list
        return cls._instance

    def add_ticket(self, ticket):
        # Add a new ticket to the system
        self.tickets.append(ticket)

    def get_all_tickets(self):
        # Get all tickets in the system
        return self.tickets

    #  Displays ticket statistics
    # @staticmethod
    def displaying_ticket_statistics():
        # Count submitted, resolved, and open/reopened tickets
        submitted_tickets = len(Ticket.tickets)
        resolved_tickets = sum(
            1 for ticket in Ticket.tickets if ticket.status == TicketStatus.CLOSED
        )
        open_tickets = sum(
            1
            for ticket in Ticket.tickets
            if ticket.status == TicketStatus.OPEN  # Use TicketStatus enum for status
            or ticket.status
            == TicketStatus.REOPENED  # Use TicketStatus enum for status
        )

        # Display ticket statistics
        print("----------------------------------------")
        print("Displaying Ticket Statistics")
        print("Ticket Created: %d" % submitted_tickets)
        print("Tickets Resolved: %d" % resolved_tickets)
        print("Tickets To Solve: %d" % open_tickets)
        print("----------------------------------------")


if __name__ == "__main__":
    ticket_system = TicketSystem()

    while True:
        #  Displays choices to user to use ticket system
        print("----------------------------------------")
        print("Select from the following choices: ")
        print("0: Exit")
        print("1: Submit help desk ticket")
        print("2: Show all tickets")
        print("3: Respond to ticket by number")
        print("4: Re-open resolved ticket")
        print("5: Display ticket status")
        print("----------------------------------------")
        choice = input("Enter menu selection 0 - 5: ")

        # Exit from create a new ticket
        if choice == "0":
            break

        if choice == "1":
            while True:
                # Gather information for a new ticket
                staff_id = input("Enter your staff id: ")
                creator = input("Enter your name: ")
                email = input("Enter your email: ")
                description = input(
                    "If you require a new password type: Password Change\nEnter description of problem: "
                ).title()

                # Create a new ticket instance and append it to the list of tickets
                new_ticket = Ticket(staff_id, creator, email, description)
                Ticket.tickets.append(new_ticket)

                # Check if the ticket is a password change request and update accordingly
                if "Password Change" in description:
                    new_ticket.change_password()
                    print(new_ticket.response)
                else:
                    print("Ticket has been submitted to helpdesk queue.")

                # Ask if there's another problem to submit
                another_problem = input("Do you have another problem to submit? (Y/N)")
                if another_problem.upper() != "Y":
                    break

        elif choice == "2":
            # Display all tickets if there are any, else print a message
            if Ticket.tickets:
                for ticket in Ticket.tickets:
                    ticket.printing_ticket()
            else:
                print("There is no ticket to print")

        elif choice == "3":
            # Respond to a ticket by its number
            ticket_number = int(input("Please enter the ticket number of respond: "))
            for ticket in Ticket.tickets:
                if ticket_number == ticket.ticket_num:
                    # Check if the ticket is open or reopened before responding
                    if (
                        ticket.status
                        == TicketStatus.OPEN  # Use TicketStatus enum for status
                        or ticket.status
                        == TicketStatus.REOPENED  # Use TicketStatus enum for status
                    ):
                        print("Respond to ticket: %d" % ticket_number)
                        change_respond = input("")
                        ticket.update_response(change_respond)
                    else:
                        print("It is a closed ticket. Please reopen it.")

        elif choice == "4":
            # Reopen a resolved ticket
            ticket_number = int(input("Please enter the ticket number to reopen: "))
            for ticket in Ticket.tickets:
                if ticket_number == ticket.ticket_num:
                    # Check if the ticket is already open before reopening
                    if (
                        ticket.status == TicketStatus.OPEN
                    ):  # Use TicketStatus enum for status
                        print("Ticket is already opened.")
                    else:
                        print("Reopen ticket: %d" % ticket_number)
                    ticket.reopen_ticket()

        elif choice == "5":
            # Display ticket statistics
            TicketSystem.displaying_ticket_statistics()
