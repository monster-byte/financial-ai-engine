from src.evaluation.track_record import TrackRecord


def average_confidence(tracker: TrackRecord) -> float:
    evaluated = [
        record
        for record in tracker.records
        if record.correct is not None
    ]

    if not evaluated:
        return 0.0

    total = sum(
        record.confidence
        for record in evaluated
    )

    return round(total / len(evaluated), 2)


def high_confidence_accuracy(
    tracker: TrackRecord,
    threshold: float = 70.0,
) -> float:

    evaluated = [
        record
        for record in tracker.records
        if record.correct is not None
        and record.confidence >= threshold
    ]

    if not evaluated:
        return 0.0

    correct = sum(
        record.correct
        for record in evaluated
    )

    return round((correct / len(evaluated)) * 100, 2)
