from src.evaluation.track_record import TrackRecord
from src.evaluation.confidence import (
    average_confidence,
    high_confidence_accuracy,
)


def test_confidence_metrics():

    tracker = TrackRecord()

    record_1 = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_on",
        probability=80.0,
        confidence=90.0,
        signal_quality=85.0,
        momentum=80.0,
    )

    record_2 = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_off",
        probability=60.0,
        confidence=50.0,
        signal_quality=60.0,
        momentum=40.0,
    )

    tracker.update_result(record_1, "risk_on")
    tracker.update_result(record_2, "risk_on")

    assert average_confidence(tracker) == 70.0
    assert high_confidence_accuracy(tracker) == 100.0
