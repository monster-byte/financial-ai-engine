from src.evaluation.track_record import TrackRecord
from src.evaluation.calibration import calibration_error


def evaluated_predictions(tracker: TrackRecord) -> int:
    return sum(
        1
        for record in tracker.records
        if record.correct is not None
    )


def correct_predictions(tracker: TrackRecord) -> int:
    return sum(
        1
        for record in tracker.records
        if record.correct is True
    )


def incorrect_predictions(tracker: TrackRecord) -> int:
    return sum(
        1
        for record in tracker.records
        if record.correct is False
    )


def performance_summary(tracker: TrackRecord) -> dict:
    evaluated = evaluated_predictions(tracker)

    if evaluated == 0:
        return {
            "evaluated": 0,
            "correct": 0,
            "incorrect": 0,
            "accuracy": 0.0,
            "calibration_error": 0.0,
        }

    return {
        "evaluated": evaluated,
        "correct": correct_predictions(tracker),
        "incorrect": incorrect_predictions(tracker),
        "accuracy": tracker.accuracy(),
        "calibration_error": calibration_error(tracker),
    }
