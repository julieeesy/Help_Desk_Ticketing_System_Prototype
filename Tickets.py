class Ticket:
    ticket_number = int(2000)

    def __init__(self, ticket_creator, staff_id, email, desc, response, ticket_status):
        Ticket.ticket_number += 1
        self.ticket_creator = ticket_creator
        self.staff_id = staff_id
        self.email = email
        self.desc = desc
        self.response = response
        self.ticket_status = ticket_status
        self.vStatus = True



