from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class PredictionRecord:
    timestamp: datetime
    market: str
    prediction: str
    probability: float
    confidence: float
    signal_quality: float
    momentum: float
    actual_result: Optional[str] = None
    correct: Optional[bool] = None


class TrackRecord:
    def __init__(self):
        self.records = []

    def add_prediction(
        self,
        market: str,
        prediction: str,
        probability: float,
        confidence: float,
        signal_quality: float,
        momentum: float,
    ) -> PredictionRecord:

        record = PredictionRecord(
            timestamp=datetime.utcnow(),
            market=market,
            prediction=prediction,
            probability=probability,
            confidence=confidence,
            signal_quality=signal_quality,
            momentum=momentum,
        )

        self.records.append(record)

        return record

    def update_result(
        self,
        record: PredictionRecord,
        actual_result: str,
    ) -> None:

        record.actual_result = actual_result
        record.correct = record.prediction == actual_result

    def total_predictions(self) -> int:
        return len(self.records)

    def accuracy(self) -> float:
        evaluated = [
            record
            for record in self.records
            if record.correct is not None
        ]

        if not evaluated:
            return 0.0

        correct = sum(record.correct for record in evaluated)

        return round((correct / len(evaluated)) * 100, 2)
