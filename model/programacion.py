from abc import ABC, abstractmethod
from typing import List

class MovieComponent(ABC):
    @abstractmethod
    def schedule(self) -> None:
        pass

class Movie(MovieComponent):
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration

    def schedule(self) -> None:
        print(f"Programando película: {self.title} ({self.duration} min)")

class MovieScheduleComposite(MovieComponent):
    def __init__(self, name: str):
        self.name = name
        self.children: List[MovieComponent] = []

    def add(self, component: MovieComponent) -> None:
        self.children.append(component)

    def remove(self, component: MovieComponent) -> None:
        self.children.remove(component)

    def schedule(self) -> None:
        print(f"Programación compuesta: {self.name}")
        for child in self.children:
            child.schedule()
