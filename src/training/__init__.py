from dataclasses import dataclass
from typing import Optional


@dataclass
class TrainingExample:
    market: str
    prediction: str
    probability: float
    confidence: float
    signal_quality: float
    momentum: float
    actual_result: Optional[str]
    correct: Optional[bool]
    feedback: float
