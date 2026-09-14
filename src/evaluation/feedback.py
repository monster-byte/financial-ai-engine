from src.evaluation.track_record import PredictionRecord


def feedback_signal(record: PredictionRecord) -> float:
    if record.correct is None:
        return 0.0

    predicted = record.probability / 100

    if record.correct:
        return round(predicted, 4)

    return round(-(1 - predicted), 4)
