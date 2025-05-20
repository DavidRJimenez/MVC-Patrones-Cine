from model.programacion import MovieScheduleComposite, Movie

class ProgramacionController:
    def __init__(self, schedule: MovieScheduleComposite):
        self.schedule = schedule

    def programar(self):
        self.schedule.schedule()
