from src.evaluation.feedback import feedback_signal
from src.evaluation.track_record import PredictionRecord
from src.training.example import TrainingExample


def build_training_example(
    record: PredictionRecord,
) -> TrainingExample:

    return TrainingExample(
        market=record.market,
        prediction=record.prediction,
        probability=record.probability,
        confidence=record.confidence,
        signal_quality=record.signal_quality,
        momentum=record.momentum,
        actual_result=record.actual_result,
        correct=record.correct,
        feedback=feedback_signal(record),
    )
