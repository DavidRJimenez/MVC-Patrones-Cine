class OccupationService:
    def get_occupation(self):
        # Simula obtener ocupación real
        return {"Sala 1": 80, "Sala 2": 60}

class ProgrammingService:
    def get_schedule(self):
        # Simula programación actual
        return {"Sala 1": "Película A - 7pm", "Sala 2": "Película B - 8pm"}

class StaffService:
    def get_staff_assignments(self):
        # Simula asignaciones
        return {"Sala 1": ["Juan", "Maria"], "Sala 2": ["Luis", "Ana"]}

class PanelInfoFacade:
    def __init__(self):
        self.occupation = OccupationService()
        self.programming = ProgrammingService()
        self.staff = StaffService()

    def get_full_info(self):
        return {
            "ocupacion": self.occupation.get_occupation(),
            "programacion": self.programming.get_schedule(),
            "personal": self.staff.get_staff_assignments()
        }
