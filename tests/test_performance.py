from src.evaluation.track_record import TrackRecord
from src.evaluation.performance import performance_summary


def test_performance_summary():

    tracker = TrackRecord()

    record_1 = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_on",
        probability=75.0,
        confidence=80.0,
        signal_quality=85.0,
        momentum=72.0,
    )

    record_2 = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_off",
        probability=70.0,
        confidence=75.0,
        signal_quality=60.0,
        momentum=35.0,
    )

    tracker.update_result(record_1, "risk_on")
    tracker.update_result(record_2, "risk_on")

    summary = performance_summary(tracker)

    assert summary["evaluated"] == 2
    assert summary["correct"] == 1
    assert summary["incorrect"] == 1
    assert summary["accuracy"] == 50.0
