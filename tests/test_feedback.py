from src.evaluation.track_record import TrackRecord
from src.evaluation.feedback import feedback_signal


def test_feedback_signal():

    tracker = TrackRecord()

    correct_record = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_on",
        probability=80.0,
        confidence=90.0,
        signal_quality=85.0,
        momentum=80.0,
    )

    incorrect_record = tracker.add_prediction(
        market="NASDAQ-100",
        prediction="risk_off",
        probability=60.0,
        confidence=70.0,
        signal_quality=65.0,
        momentum=40.0,
    )

    tracker.update_result(correct_record, "risk_on")
    tracker.update_result(incorrect_record, "risk_on")

    assert feedback_signal(correct_record) == 0.8
    assert feedback_signal(incorrect_record) == -0.4
