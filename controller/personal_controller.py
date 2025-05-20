from model.personal import StaffAssigner, EmailSender

class PersonalController:
    def __init__(self, assigner: StaffAssigner):
        self.assigner = assigner

    def asignar(self, staff_name: str, room: str, shift: str):
        self.assigner.assign_staff(staff_name, room, shift)
