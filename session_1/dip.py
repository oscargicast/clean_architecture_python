from abc import ABC, abstractmethod
from typing import Protocol


# class EmailSender(ABC):
#     @abstractmethod
#     def send_email(self, body: str):
#         pass


class EmailSender(Protocol):

    def send_email(self, body: str):
        pass


# class MandrillSender(EmailSender):
class MandrillSender:
    def set_credentials(self, credentials: dict):
        pass

    def send_email(self, body: str):
        print("Using mandrill")
        print(f"Email sent with body: {body}")


# class SendgridSender(EmailSender):
class SendgridSender:
    def set_credentials(self, credentials: dict):
        pass

    def send_email(self, body: str):
        print("Using sendgrid")
        print(f"Email sent with body: {body}")


class Order:
    def __init__(self, id: int):
        self.id = id

    def compute_total(self):
        print(f"Computing total for order: {self.id}")

    # def send_email(self):
    #     print(f"Email sent with body: {self.id}")


def process_order(id: int, email_sender: EmailSender):
    order = Order(id)
    order.compute_total()
    print(f"Processing order: {order.id}")
    email_sender.send_email(f"Sending email to order: {order.id}")
    # mandrill_sender_obj = MandrillSender()
    # if isinstance(sender, MandrillSender):
    #     sender.send_email(f"Processing order: {order.id}")
    # elif isinstance(sender, SendGridSender):
    #     sender.send(f"Processing order: {order.id}")


if __name__ == "__main__":
    order = Order(123)
    # mandrill_sender_obj = MandrillSender()
    sendgrid_sender_obj = SendgridSender()
    process_order(id=order.id, email_sender=sendgrid_sender_obj)
