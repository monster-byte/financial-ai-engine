from src.evaluation.track_record import TrackRecord
from src.training.builder import build_training_example


def test_build_training_example():

    tracker = TrackRecord()

    record = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_on",
        probability=80.0,
        confidence=90.0,
        signal_quality=85.0,
        momentum=80.0,
    )

    tracker.update_result(record, "risk_on")

    example = build_training_example(record)

    assert example.market == "NASDAQ-100"
    assert example.prediction == "risk_on"
    assert example.probability == 80.0
    assert example.confidence == 90.0
    assert example.signal_quality == 85.0
    assert example.momentum == 80.0
    assert example.actual_result == "risk_on"
    assert example.correct is True
    assert example.feedback == 0.8
