from typing import List

from src.training.example import TrainingExample


class TrainingDataset:

    def __init__(self):
        self.examples: List[TrainingExample] = []

    def add(self, example: TrainingExample) -> None:
        self.examples.append(example)

    def size(self) -> int:
        return len(self.examples)

    def all(self) -> List[TrainingExample]:
        return self.examples
