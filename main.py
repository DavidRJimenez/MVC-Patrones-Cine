# main.py

from model.personal import StaffAssigner, EmailSender, SmsSender
from model.programacion import MovieScheduleComposite, Movie
from service.panel_info_facade import PanelInfoFacade
from controller.personal_controller import PersonalController
from controller.programacion_controller import ProgramacionController
from controller.panel_info_controller import PanelInfoController


def main():
    print("\n--- Módulo Gestor de Personal (Bridge) ---")
    # Crear el sender para comunicación (puede ser EmailSender o SmsSender)
    email_sender = EmailSender("smtp.cine.com")
    sms_sender = SmsSender("API-KEY-123")
    
    # Asignar personal usando Email
    assigner_email = StaffAssigner(email_sender)
    personal_ctrl_email = PersonalController(assigner_email)
    personal_ctrl_email.asignar("Carlos", "Sala 1", "Mañana")

    # Asignar personal usando SMS
    assigner_sms = StaffAssigner(sms_sender)
    personal_ctrl_sms = PersonalController(assigner_sms)
    personal_ctrl_sms.asignar("Ana", "Sala 2", "Tarde")


    print("\n--- Módulo Programador de Películas (Composite) ---")
    # Crear películas y programación compuesta
    peli1 = Movie("Matrix", 120)
    peli2 = Movie("Inception", 140)
    peli3 = Movie("Interstellar", 165)

    programacion_dia1 = MovieScheduleComposite("Programación Día 1")
    programacion_dia1.add(peli1)
    programacion_dia1.add(peli2)

    programacion_dia2 = MovieScheduleComposite("Programación Día 2")
    programacion_dia2.add(peli3)

    # Programa completa que incluye los días
    programacion_semanal = MovieScheduleComposite("Programación Semanal")
    programacion_semanal.add(programacion_dia1)
    programacion_semanal.add(programacion_dia2)

    programacion_ctrl = ProgramacionController(programacion_semanal)
    programacion_ctrl.programar()


    print("\n--- Módulo Panel de Información (Facade) ---")
    facade = PanelInfoFacade()
    panel_ctrl = PanelInfoController(facade)
    panel_ctrl.mostrar_info()


if __name__ == "__main__":
    main()
