from src.evaluation.track_record import TrackRecord


def brier_score(tracker: TrackRecord) -> float:
    evaluated = [
        record
        for record in tracker.records
        if record.correct is not None
    ]

    if not evaluated:
        return 0.0

    total = 0.0

    for record in evaluated:
        predicted = record.probability / 100
        actual = 1.0 if record.correct else 0.0

        total += (predicted - actual) ** 2

    return round(total / len(evaluated), 4)
