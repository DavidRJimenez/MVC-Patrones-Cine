from service.panel_info_facade import PanelInfoFacade

class PanelInfoController:
    def __init__(self, facade: PanelInfoFacade):
        self.facade = facade

    def mostrar_info(self):
        info = self.facade.get_full_info()
        for key, val in info.items():
            print(f"{key.capitalize()}: {val}")
