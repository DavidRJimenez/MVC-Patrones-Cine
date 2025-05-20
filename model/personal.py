from abc import ABC, abstractmethod

# Implementor del Bridge
class ICommunicationSender(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

class EmailSender(ICommunicationSender):
    def __init__(self, smtp_server: str):
        self.smtp_server = smtp_server

    def send_message(self, message: str) -> None:
        print(f"[Email via {self.smtp_server}]: {message}")

class SmsSender(ICommunicationSender):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def send_message(self, message: str) -> None:
        print(f"[SMS via API {self.api_key}]: {message}")

# Abstraction del Bridge
class StaffAssigner:
    def __init__(self, sender: ICommunicationSender):
        self.sender = sender

    def assign_staff(self, staff_name: str, room: str, shift: str) -> None:
        # lógica de asignación (simplificada)
        msg = f"Asignado {staff_name} a sala {room} para turno {shift}"
        self.sender.send_message(msg)
